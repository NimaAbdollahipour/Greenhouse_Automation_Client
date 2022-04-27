import json


def read_file():
    try:
        json_file = open('../client.json','r+')
        data = json_file.read()
        data = json.loads(data)
        json_file.close()
    except :
        print("[AN ERROR OCCURED WHILE READING JSON FILE]")
    return data


def write_file(data):
    try:
        json_file = open('../client.json','w+')
        data = json.dumps(data)
        json_file.writelines(data)
    except:
        print("[AN ERROR OCCURED WHILE WRITING TO JSON FILE]")


def save_plant():
    pass


def save_config():
    pass


def save_user():
    pass


def save_settings():
    pass


def save_raw():
    pass


def save_data():
    pass


def read_data():
    pass


def read_raw():
    pass


def read_user():
    pass


def read_settings():
    pass


def read_plant():
    pass


def read_config():
    pass


def get_port():
    return 0