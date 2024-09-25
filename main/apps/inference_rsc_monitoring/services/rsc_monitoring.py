from kubernetes import client, config

#only support one node from now (master and worker altogether)
#only support one pod one container

namespace = """default"""
config.load_kube_config()

core_v1 = client.CoreV1Api()
custom_api = client.CustomObjectsApi()


def get_num_of_deployment(position_uid, namespace=namespace):
    
    return len(core_v1.list_namespaced_pod(namespace, label_selector=f"app={position_uid}",watch=False).items)
    

def get_CPU_Mem_usage_in_limitation(position_uid):
    
    pod_info = core_v1.list_namespaced_pod(namespace, label_selector=f"app={position_uid}" ,watch=False)
    
    mem_limit = 0
    cpu_limit = 0
    
    #get the limitation of pod in spec
    #unit m/Mi
    for a in pod_info.to_dict()['items']:
        for i in a['spec']['containers']:
            if(i['resources']['limits']):
                
                if(i['resources']['limits']['memory']):
                    mem_limit = float(i['resources']['limits']['memory'].split('Mi')[0])
                
                if(i['resources']['limits']['cpu']):
                    cpu_limit = float(i['resources']['limits']['cpu'].split('m')[0])
            
                
    result_list = []
    usage = get_Pod_current_resources_usage(position_uid)
    #get the current usage of Memory
    #unit n/Ki
    for i in usage:
        cpu_per = float(i[0].split('n')[0]) / (cpu_limit*1000000) * 100
        mem_per = float(i[1].split('Ki')[0]) / (mem_limit*1000) * 100
        pod = {
            "pod_name" : i[2],
            "cpu" : {
                "percentage": cpu_per,
                "actual": i[0]
                },
            "mem" : {
                "percentage" : mem_per,
                "actual": i[1]
                }
        }
        
        result_list.append(pod)
    
    return result_list
    
# the unit cannot be changed. 
def get_CPU_Mem_usage_in_node(position_uid):
    
    Node_info = core_v1.list_node()
    # get node capacity
    node_cpu_limit = Node_info.to_dict()['items'][0]['status']['allocatable']['cpu'] # int
    node_mem_limit = Node_info.to_dict()['items'][0]['status']['allocatable']['memory'] # Ki
    
    usage = get_Pod_current_resources_usage(position_uid)

    usage_list = [] # cpu:n mem: Ki
    
    position_cpu_total = 0
    position_mem_total = 0
    
    for i in usage:
        position_cpu_total = position_cpu_total + float(i[0].split('n')[0]) 
        position_mem_total = position_mem_total + float(i[1].split('Ki')[0]) 
        usage_list.append({"cpu": i[0], "mem": i[1]})
        
    position_cpu_usage = position_cpu_total / (float(node_cpu_limit)*1000000000) * 100
    position_mem_usage = position_mem_total / (float(node_mem_limit.split('Ki')[0])) * 100
    
    result_dict = {
        "node_cpu_limit": node_cpu_limit,
        "node_mem_limit": node_mem_limit,
        "position_cpu_usage": position_cpu_usage,
        "position_mem_usage": position_mem_usage,
        "position_cpu_total": position_cpu_total,
        "position_mem_total": position_mem_total,
        "usage_list": usage_list
    }
    
    return result_dict
        

def get_Pod_current_resources_usage(position_uid):
    
    pod = custom_api.list_cluster_custom_object_with_http_info("metrics.k8s.io", "v1beta1", "pods", label_selector=f'app={position_uid}')
    
    result_list = []
    
    for i in pod[0]['items']:
        cpu = i['containers'][0]['usage']['cpu']
        mem = i['containers'][0]['usage']['memory']
        name = i['metadata']['name']

        result_list.append([cpu, mem, name])

    return result_list