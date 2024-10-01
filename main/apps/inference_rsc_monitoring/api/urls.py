from django.urls import path
from main.apps.inference_rsc_monitoring.actors import RscMonitor

module_name = 'inference_rsc_monitoring'

urlpatterns = [
    path(f'{module_name}/RscMonitor/position_deployment_number', RscMonitor.position_deployment_number),
    path(f'{module_name}/RscMonitor/position_usage_in_node', RscMonitor.position_usage_in_node),
    path(f'{module_name}/RscMonitor/position_usage_in_limitation', RscMonitor.position_usage_in_limitation)
]