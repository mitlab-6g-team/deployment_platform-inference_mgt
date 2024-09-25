from main.utils.env_loader import customized_env
from kubernetes import client, config
import time, os


namespace = """default"""

#TODO
"""
create namespace
"""
config.load_kube_config()
core_v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

def check_service(position_uid):
    
    services = core_v1.list_service_for_all_namespaces(watch=False)
    
    for i in services.to_dict()['items']:
        if f'inference-host-{position_uid}' == i['metadata']['name'] : return True
    
    return False

def create_service(position_uid, external_port):
    
    body = client.V1Service(

        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name=f"inference-host-{position_uid}"
        ),

        spec = client.V1ServiceSpec(
            selector={"position_uid": f"{position_uid}"},
            type="LoadBalancer",
            ports=[client.V1ServicePort(
                port=int(external_port),
                target_port=30305
            )],
            external_i_ps=["10.1.1.5"]
        )

    )
    
    resp = core_v1.create_namespaced_service(namespace=namespace, body=body)
    
    return resp

def remove_service(position_uid):
   
    return core_v1.delete_namespaced_service(name=f'inference-host-{position_uid}', namespace=namespace)
    

def deploy_inference_host(application_uid, position_uid, num, model_uid, file_extension):
    
    image_pull_secret = client.V1LocalObjectReference(name='harbor-secret')
    harbor_host = customized_env.HARBOR_HOST
    model_name = f'{harbor_host}/inference_host/{position_uid}:{model_uid}'
    timestamp = int(time.time()*1000)
    
    for i in range(int(num)) :
        yaml = {
            "apiVersion": "apps/v1",
            "kind": "Deployment", 
            "metadata": {
                "name": f"{position_uid}-{timestamp}",
                    "labels": {
                        "position_uid": f"{position_uid}"
                    }
            },
            "spec": {
                "replicas": 1,
                "selector": {
                    "matchLabels": {
                        "position_uid": f"{position_uid}"
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "position_uid": f"{position_uid}"
                        }
                    },
                    "spec": {
                        "imagePullSecrets": [image_pull_secret],
                        "containers": [
                            {
                                "name": f"{position_uid}-{timestamp}",
                                "image": f"{model_name}",
                                "imagePullPolicy": "Always",
                                "env": [
                                    {
                                        "name": "POSITION_UID",
                                        "value": position_uid
                                    },
                                    {
                                        "name": "APPLICATION_UID",
                                        "value": application_uid
                                    } ,
                                    {
                                        "name": "FILE_EXTENSION",
                                        "value": file_extension
                                    } ,{
                                        "name": "DEPLOYMENT_PF_HOST_IP",
                                        "value": os.environ.get('DEPLOYMENT_PF_HOST_IP')
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        } 
        
        apps_v1.create_namespaced_deployment(body=yaml, namespace=namespace)
       
    return num
    
def delete_inference_host(position_uid, num):
    
    pod_info = _get_pod_list(position_uid, namespace=namespace)
    
    temp = []
    count = 0
    for i in pod_info:
        temp.append(i.to_dict()['metadata']['generate_name'].rsplit('-', 2)[0])
    
    if(num == '0'):
        for i in temp:
            apps_v1.delete_namespaced_deployment(i, namespace)
            count+=1
        return count
    
    else :
        for i in range(int(num)) :
            apps_v1.delete_namespaced_deployment(temp[i], namespace)
            count += 1
            
    return count

def update_inference_host(position_uid, model_uid):
    
    harbor_host = customized_env.HARBOR_HOST
    deployments = _get_deployment_list(position_uid)
    
    for deploy in deployments:
        
        deploy_dict = deploy.to_dict()
        deploy_name = deploy_dict['metadata']['name']
        
        deploy.spec.template.spec.containers[0].image = f'{harbor_host}/inference_host/{position_uid}:{model_uid}'
        
        apps_v1.patch_namespaced_deployment(
            name=deploy_name, namespace=namespace, body=deploy
        )
    
    return True
    
   
#private function 
def _get_pod_list(position_uid, namespace=namespace):
    
    return core_v1.list_namespaced_pod(namespace, label_selector=f"position_uid={position_uid}",watch=False).items

def _get_deployment_list(position_uid):
    
    return apps_v1.list_namespaced_deployment(namespace=namespace, label_selector=f'position_uid={position_uid}').items
   

