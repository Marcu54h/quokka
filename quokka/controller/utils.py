import re
import socket
import yaml

from datetime import datetime


def get_response_time(ping_output):
    m = re.search(r"time([d]?)[=<]?([0-9]*)", ping_output)
    if m is not None:
        if len(m.groups()) == 2 and m.group(2).isnumeric():
            return int(m.group(2))
        if len(m.groups()) == 2 and m.group(2) == '':
            return -1
    else:
        log_console("Wrong ping output, can't find timeout value!")


def import_devices():
    with open('quokka/data/devices.yaml') as devices_file:
        devices = yaml.safe_load(devices_file.read())
        return devices

def log_console(output):
    print(f"{str(datetime.now())[:-3]}: {output}")

def get_this_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP