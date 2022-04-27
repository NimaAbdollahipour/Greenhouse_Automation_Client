import json


def first_use():
    print("[FIRST USE]>>>")
    print("[USER INFO]")
    while True:
        username = input ("[ENTER YOUR USERNAME]: ")
        password = input ("[ENTER YOUR PASSWORD]: ")
        print("[CHECKING USERNAME AND PASSWORD ...]")
        valid = True    #Check password validity from server
        if valid:
            break
        else:
            usr_input = input("[IF YOU WANT TO EXIT ENTER EXIT(exit).]")
            if usr_input.strip().lower() == "exit":
                break
    print("[PASSWORD AND USERNAME VERIFIED SUCCESSFULLY.]")







