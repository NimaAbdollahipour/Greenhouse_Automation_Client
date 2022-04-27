import requests
from greenhouse_automation_client.file_op import *

GA_SERVER = "greenhouse_automation.com"


def send_data():
    data = read_data()
    ga_token = read_token()
    data_to_send = {
        "light":data.get("light"),
        "temp":data.get("temperature"),
        "tank":data.get("tank"),
        "moisture":data.get("moisture")
        }
    msg = requests.post(GA_SERVER+"/dataexchange/data",json=data_to_send,headers={"token":ga_token})
    return msg.json.get("message")
    

def validate():

    pass


def get_token():
    pass


def get_configurations():
    pass


def get_commands():
    pass