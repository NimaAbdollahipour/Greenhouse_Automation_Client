import json
from .console import disp_error,disp_success


def read_file():
    try:
        json_file = open('../client.json','r+')
        data = json_file.read()
        data = json.loads(data)
        json_file.close()
    except :
        disp_error("[AN ERROR OCCURED WHILE READING JSON FILE]")
    return data


def write_file(data):
    try:
        json_file = open('../client.json','w+')
        data = json.dumps(data)
        json_file.writelines(data)
        json_file.close()
        disp_success("SAVED SUCCESSFULLY")
    except:
        disp_error("[AN ERROR OCCURED WHILE WRITING TO JSON FILE]")


def save_plant(plant):
    data = read_file()
    data["plant"]["min_temp"] = plant[0]
    data["plant"]["max_temp"] = plant[1]
    data["plant"]["moisture"] = plant[2]
    data["plant"]["changed"] = True
    write_file(data)


def save_config(config):
    data = read_file()
    data["config"]["fan"] = config[0]
    data["config"]["heater"] = config[1]
    data["config"]["pump"] = config[2]
    data["config"]["changed"] = True
    write_file(data)


def save_user(username,password):
    data = read_file()
    data["user"]["username"] = username
    data["user"]["password"] = password
    write_file(data)


def save_settings(settings):
    data = read_file()
    data["settings"]["irrigation_auto"] = settings[0]
    data["settings"]["irrigation_on_specific_hour"] = settings[1]
    data["settings"]["time_1"] = settings[2]
    data["settings"]["time_2"] = settings[3]
    write_file(data)


def save_raw(arduino_data):
    data = read_file()
    data["raw_data"]["light"].append(arduino_data[0]) 
    data["raw_data"]["temperature"].append(arduino_data[1])
    data["data"]["tank"] = arduino_data[1]
    data["data"]["moisture"] = arduino_data[2]
    write_file(data)


def save_data():
    data = read_file()
    data["data"]["light"].append(round(sum(data["raw_data"]["light"])/len(data["raw_data"]["light"]))) 
    data["data"]["temperature"].append(round(sum(data["raw_data"]["temperature"])/len(data["raw_data"]["temperature"]))) 
    write_file(data)


def read_data():
    data = read_file()
    return data["data"]


def read_raw():
    data = read_file()
    return data["raw"]


def read_user():
    data = read_file()
    return data["user"]


def read_settings():
    data = read_file()
    return data["settings"]


def read_plant():
    data = read_file()
    return data["plant"]


def read_config():
    data = read_file()
    return data["config"]


def save_token(token):
    data = read_file()
    data["user"]["token"] = token
    write_file(data)


def get_port():
    data = read_file()
    return data["port"]


def read_token():
    data = read_file()
    return data["user"]["token"]