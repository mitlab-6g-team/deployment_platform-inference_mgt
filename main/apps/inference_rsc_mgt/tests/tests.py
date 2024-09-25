from django.test import TestCase
from unittest.mock import patch
from django.test import TestCase, Client
from main.utils.env_loader import default_env
import json

# Create your tests here.
class TestInferenceRscMgtHandler(TestCase):
    """_summary_
    
    unittest for services in InferenceRscMgtHandler

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        """
        unittest request initialize
        """
        self.client = Client()
        
    def test_executing_test(self):
        """
        test to check the master container work
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_mgt/InferenceRscMgtHandler/executing_test")

        # build the payload and header
        payload_dict  = {}
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_inference_unit_deploy(self):
        """
        test to deploy new inference hosts in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_mgt/InferenceRscMgtHandler/inference_unit_deploy")

        # build the payload and header
        payload_dict  = {
            'position_uid' : '2129792a-e670-494c-90fe-d4e38e8b365d',
            'num_of_deployment': '1',
            'resource_requirement':{
                "cpu_requests": "",
                "cpu_limits": "",
                "memory_requests": "",
                "memory_limits": ""
            }
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_inference_unit_remove(self):
        """
        test to remove a number of inference host in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_mgt/InferenceRscMgtHandler/inference_unit_remove")

        # build the payload and header
        payload_dict  = {
            'position_uid' : 'test_position_uid',
            'num_of_deployment': '1'
            }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
    def test_inference_unit_update(self):
        """
        test to update all the inference hosts in specific position
        """
        API_version = default_env.API_VERSION
        
        # build the complete API path
        url_str = (f"/api/{API_version}/"
                   f"inference_rsc_mgt/InferenceRscMgtHandler/inference_unit_update")

        # build the payload and header
        payload_dict  = {
            'position_uid' : '2129792a-e670-494c-90fe-d4e38e8b365d',
            'model_uid': 'aaaabbbb-4459-461c-8b8e-b3b154f8e5d7',
            'resource_requirement':{
                "cpu_requests": "",
                "cpu_limits": "",
                "memory_requests": "",
                "memory_limits": ""
            }
        }
        
        headers_str='application/json'

        # unit test begin
        response = self.client.post(
            path = url_str,
            data = json.dumps(payload_dict),
            content_type = headers_str
        )
        
        print(response.content)