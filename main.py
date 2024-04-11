from netmiko import ConnLogOnly
from threading import Thread


# ip username password
def get_info() -> list:
    info = ["ip", "user", "pwd"]
    return info


# cmd
def get_command() -> list:
    commands = []
    try:
        with open("config/config.txt") as f:
            commands = f.readlines()
    except Exception as e:
        print(e)
    return commands


# ping
def alive(ip) -> bool:
    is_alive = False

    return is_alive


# ssh telnet
def login(ip, username, password):
    device_ssh = {
        'device_type': 'huawei',
        'ip': ip,
        'username': username,
        'password': password,
        'port': 22
    }
    device_telnet = {
        'device_type': 'huawei',
        'ip': ip,
        'username': username,
        'password': password,
        'port': 21
    }
    try:
        with ConnLogOnly(**device_ssh) as con_ssh:
            if con_ssh is None:
                with ConnLogOnly(**device_telnet) as con_telnet:
                    return con_telnet
            else:
                return con_ssh
    except Exception as e:
        print(e)


# send conf
def config(info, command):
    if alive(info[0]):
        con = login(info[0], info[1], info[2])
        print(con)
        for cmd in command:
            con.send_config_set(cmd)
    else:
        print("offline")


if __name__ == '__main__':
    device_info = get_info()
    command = get_command()
    for info in device_info:
        t = Thread(target=config, args=(device_info, command))
        t.start()
        t.join()
