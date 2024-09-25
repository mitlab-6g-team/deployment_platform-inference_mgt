from django.urls import path
from main.apps.inference_rsc_mgt.actors import InferenceRscMgtHandler

module_name = 'inference_rsc_mgt'

urlpatterns = [
    path(f'{module_name}/InferenceRscMgtHandler/inference_unit_deploy', InferenceRscMgtHandler.inference_unit_deploy),
    path(f'{module_name}/InferenceRscMgtHandler/inference_unit_remove', InferenceRscMgtHandler.inference_unit_remove),
    path(f'{module_name}/InferenceRscMgtHandler/inference_unit_update', InferenceRscMgtHandler.inference_unit_update),
    path(f'{module_name}/InferenceRscMgtHandler/executing_test', InferenceRscMgtHandler.executing_test)
]