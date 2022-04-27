from .colors import *

def disp_error(*msg):
    for i,j in enumerate(msg):
        print(Red+j);
    print(Reset,end='');

def disp_msg(*msg):
    for i,j in enumerate(msg):
        print(Blue+msg);
    print(Reset,end='');

def disp_success(*msg):
    for i,j in enumerate(msg):
        print(Green+msg)
    print(Reset,end='');
