"""
InferenceRscMgtHandler
"""
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger, log_writer
from main.apps.inference_rsc_mgt.services.inference_unit import deploy_inference_host, delete_inference_host, create_service, remove_service, check_service, update_inference_host
from main.apps.inference_rsc_mgt.services.kong_control import add_kong, remove_kong
from main.utils.env_loader import customized_env


@require_POST
@log_trigger("INFO")
def executing_test(request):
    """
    executing_test
    """
    return HttpResponse(json.dumps({'status': 'success', 'msg': 'connected'}))


@require_POST
@log_trigger("INFO")
def inference_unit_deploy(request):
    """
    inference_unit_deploy 
    """
    data = json.loads(request.body.decode('utf-8'))

    if (not check_service(data['position_uid'])):
        # deploy the service if the service of inference_host isn't existed.
        create_service(data['position_uid'], data['external_port'])
        # add new routing of the service of inference_host
        payload = {
            "service_type": "inference-service",
            "position_uid": data['position_uid'],
            "service_url": f"http://{customized_env.K8S_SERVICE_IP}:{data['external_port']}/api/inference_exe/InferenceServiceHandler/get_inference_result",
        }

        add_kong(payload)

    # deploy slave pod
    count = deploy_inference_host(data['application_uid'], data['position_uid'],
                                  data['num_of_deployment'], data['model_uid'], data['file_extension'])

    response = json.dumps({'status': 'success', 'num_of_deployment': count})

    return HttpResponse(response)


@require_POST
@log_trigger("INFO")
def inference_unit_remove(request):
    """
    inference_unit_remove 
    """
    data = json.loads(request.body.decode('utf-8'))

    if (data['num_of_deployment'] == '0'):
        # shutdown all the slave pods

        count = delete_inference_host(
            data['position_uid'], data['num_of_deployment'])
        # check if the service is created
        if (check_service(data['position_uid'])):
            # remove the service of inference hosts
            remove_service(data['position_uid'])
            # remove the routing data of the service of inference hosts
            payload = {
                "service_type": f'inference-service',
                "position_uid": data['position_uid']
            }
            remove_kong(payload=payload)

    else:
        # shutdown slave pods
        count = delete_inference_host(
            data['position_uid'], data['num_of_deployment'])

    response = json.dumps(
        {'status': 'success', 'actual_num_of_removing': count})

    return HttpResponse(response)


@require_POST
@log_trigger("INFO")
def inference_unit_update(request):
    """
    inference_unit_update 
    """
    data = json.loads(request.body.decode('utf-8'))

    resp = update_inference_host(data['position_uid'], data['model_uid'])

    response = json.dumps(
        {'status': 'success', 'model_uid': data['model_uid']})

    return HttpResponse(response)
