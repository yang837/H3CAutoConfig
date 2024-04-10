from netmiko import ConnectHandler


# ip username password
def get_info() -> list:
    info = []
    return info


# cmd
def get_command() -> list:
    cmds = []
    return cmds


# ping
def alive(ip) -> bool:
    is_alive = False

    return is_alive


# ssh telnet
def login(ip, username, password) -> ConnectHandler():
    device = {
        'device_type': 'huawei',
        'ip': ip,
        'username': username,
        'password': password,
        'port': 22
    }
    with ConnectHandler(**device) as con:
        return con


# send conf
def config(con, command):
    for cmd in command:
        con.send_config_set(cmd)


if __name__ == '__main__':
    device_info = get_info()
    commands = get_command()
    for info in device_info:
        if alive(info[0]):
            con = login(info[0], info[1], info[2])
            config(con, commands)
