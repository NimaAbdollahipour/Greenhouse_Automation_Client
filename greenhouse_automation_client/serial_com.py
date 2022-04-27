import serial.tools.list_ports as ls_port
import serial


def get_ports():
    portList = []
    ports = ls_port.comports()
    for one_port in ports:
        portList.append(str(one_port))
    return portList


def connect(port):
    serialInst = serial.Serial()
    serialInst.baudrate = 9600
    serialInst.port = "COM"+port
    serialInst.open()
    return serialInst


def handle(serial_instance,mode):
    value = None
    if serial_instance.in_waiting:
        packet = serial_instance.readline()
        data =  packet.decode("utf-8")
    if data == "start":
        set_initial(serial_instance)
        if mode=="test":
            test(serial_instance)
    elif data.startswith("light"):
        try:
            value = int((data.split(":")[1]).strip())
        except:
            print("[ERROR CONVERTING LIGHT VALUE]")
    elif data.startswith("temperature"):
        try:
            value = int((data.split(":")[1]).strip())
        except:
            print("[ERROR CONVERTING TEMPERATURE VALUE]")
    elif data.startswith("moisture"):
        try:
            value = int((data.split(":")[1]).strip())
        except:
            print("[ERROR CONVERTING MOISTURE VALUE]")
    elif data.startswith("tank"):
        try:
            value = int((data.split(":")[1]).strip())
        except:
            print("[ERROR CONVERTING TANK VALUE]")
    elif data.startswith("instructions"):
        send_settings()
    else:
        print("[INVALID DATA FROM ARDUINO]")
    
    return value


def set_initial(serial_instance,min_temp,max_temp,moisture):
    string_to_write = "p{}&{}&{}".format(min_temp,max_temp,moisture)
    serial_instance.write(string_to_write.encode())


def test(serial_instance):
    serial_instance.write("test".encode())
    

def send_settings(serial_instance,config,plant):
    string_to_write = "p{}&{}&{}c{}&{}&{}".format(plant[0],plant[1],plant[2],config[0],config[1],config[2])
    serial_instance.write(string_to_write.encode())