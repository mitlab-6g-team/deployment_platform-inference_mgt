from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from main.utils.env_loader import default_env
import json

# Create your tests here.
class TestRscMonitor(TestCase):
    """_summary_
    
    unittest for RscMonitor

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        """
        unittest request initialize
        """
        self.client = Client()
        
    def test_position_deployment_number(self):
        """
        test to get the number of inference hosts in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_monitoring/RscMonitor/position_deployment_number")

        # build the payload and header
        payload_dict  = {
            "position_uid": "hello-world"
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        print(response.content)
        
    def test_position_usage_in_node(self):
        """
        test to get the capacity of node 
        and the current usage of inference hosts in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_monitoring/RscMonitor/position_usage_in_node")

        # build the payload and header
        payload_dict  = {
            "position_uid": "4e39b436-cce0-499d-af71-9fab79910fbe"
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        print(response.content)
        
    def test_position_usage_in_limitation(self):
        """
        test to get the ratio of cpu and memory usage and limitation of pod
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_monitoring/RscMonitor/position_usage_in_limitation")

        # build the payload and header
        payload_dict  = {
            "position_uid": "hello-world"
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        print(response.content)