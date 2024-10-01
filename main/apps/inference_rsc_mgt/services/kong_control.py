import requests
import json
from main.utils.env_loader import customized_env
from main.utils.api_caller import call_api


def add_kong(payload):

    try:
        response = call_api(
            "dataflow_mgt",
            "RoutingMgtHandler",
            "add_routing_data",
            payload
        )

        return json.loads(response.content.decode('utf-8'))['status'] == 'success'
    except:
        return False


def remove_kong(payload):

    try:
        response = call_api(
            "dataflow_mgt",
            "RoutingMgtHandler",
            "remove_routing_data",
            payload
        )

        return json.loads(response.content.decode('utf-8'))['status'] == 'success'
    except:
        return False
