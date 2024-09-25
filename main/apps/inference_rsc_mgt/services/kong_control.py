import requests, json
from main.utils.env_loader import customized_env
    
def add_kong(position_route_host, payload):
    
    dataflow_mgt_version=customized_env.DATAFLOW_MGT_VERSION
    url = f"""http://{position_route_host}/api/{dataflow_mgt_version}/inference_unit_routing_mgt/RoutingMgtHandler/add_routing_data""" 
    headers = {'Accept': 'application/json'}
    response = ''
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if(json.loads(response.content.decode('utf-8'))['status'] == 'success'):
            return True
        else:
            return False
    except:
        return False

def remove_kong(position_route_host, payload):
    
    dataflow_mgt_version=customized_env.DATAFLOW_MGT_VERSION
    url = f"""http://{position_route_host}/api/{dataflow_mgt_version}/inference_unit_routing_mgt/RoutingMgtHandler/remove_routing_data""" 
    headers = {'Accept': 'application/json'}
    response = ''
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        if(json.loads(response.content.decode('utf-8'))['status'] == 'success'):
            return True
        else:
            return False
    except:
        return False
