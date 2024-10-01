"""
load env
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv('.env.common')
load_dotenv()


@dataclass
class Default:
    """
        load default env
    """
    LOGS_FOLDER_PATH: str
    DJANGO_SETTINGS_MODULE: str
    DEBUG: str
    ALLOWED_HOSTS: str
    API_ROOT: str
    API_VERSION: str


default_env = Default(
    LOGS_FOLDER_PATH=os.environ.get('LOGS_FOLDER_PATH'),
    DJANGO_SETTINGS_MODULE=os.environ.get('DJANGO_SETTINGS_MODULE'),
    DEBUG=os.environ.get('DEBUG'),
    ALLOWED_HOSTS=os.environ.get('ALLOWED_HOSTS'),
    API_ROOT=os.environ.get('API_ROOT'),
    API_VERSION=os.environ.get('API_VERSION'),
)


@dataclass
class Customized:
    """
        load customized env
    """
    K8S_SERVICE_IP: str
    HOST_IP: str
    ROUTE_MGT_PORT: str
    HARBOR_HOST: str
    DATAFLOW_MGT_HOST_IP: str
    DATAFLOW_MGT_PORT: str
    DATAFLOW_MGT_VERSION: str
    DATAFLOW_MGT_NAME: str


customized_env = Customized(
    K8S_SERVICE_IP=os.environ.get('K8S_SERVICE_IP'),
    HOST_IP=os.environ.get('HOST_IP'),
    ROUTE_MGT_PORT=os.environ.get('ROUTE_MGT_PORT'),
    HARBOR_HOST=os.environ.get('HARBOR_HOST'),
    DATAFLOW_MGT_HOST_IP=os.environ.get('DATAFLOW_MGT_HOST_IP'),
    DATAFLOW_MGT_PORT=os.environ.get('DATAFLOW_MGT_PORT'),
    DATAFLOW_MGT_VERSION=os.environ.get('DATAFLOW_MGT_VERSION'),
    DATAFLOW_MGT_NAME=os.environ.get('DATAFLOW_MGT_NAME'),
)
