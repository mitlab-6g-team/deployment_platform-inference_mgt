"""
RscMonitor
"""
import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger, log_writer
from main.apps.inference_rsc_monitoring.services.rsc_monitoring import get_num_of_deployment, get_CPU_Mem_usage_in_limitation, get_CPU_Mem_usage_in_node

@require_POST 
@log_trigger("INFO")
def position_deployment_number(request):
    """
    position_deployment_number 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    #get the number of deployment in specific position_uid
    response = json.dumps({'status' : get_num_of_deployment(position_uid=data['position_uid'])})
    
    return HttpResponse(response)

@require_POST 
@log_trigger("INFO")
def position_usage_in_node(request):
    """
    position_usage_in_node 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    #get the number of deployment in specific position_uid
    response = json.dumps(get_CPU_Mem_usage_in_node(data['position_uid']))
    
    return HttpResponse(response)

@require_POST 
@log_trigger("INFO")
def position_usage_in_limitation(request):
    """
    position_usage_in_limitation 
    """
    data = json.loads(request.body.decode('utf-8'))
    
    #get the number of deployment in specific position_uid
    response = json.dumps({'inference_hosts' : get_CPU_Mem_usage_in_limitation(data['position_uid'])})
    
    return HttpResponse(response)