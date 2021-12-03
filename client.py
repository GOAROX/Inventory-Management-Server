import socket

HOST = '192.168.1.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def recv_all(s):
    data = ''
    while True:
        d = s.recv(1024)
        data += d.decode()
        if len(d) < 1024:
            break
    return data


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    req = 'Sorted Name'
    request = 'Request\n' + req
    s.sendall(request.encode())
    data = recv_all(s)

s = data
lines = s.split('\n')
if lines[0].strip() == 'Response':
    # the inventory file was returned
    if lines[1].strip() == 'data':
        file_text = lines[2]
        # replace all ';' with \n as that is how the file was sent to us
        new_str = file_text.replace(';', '\n')
        # write this string to a file to get our new inventory
        with open('receiver/inventory.txt', 'w') as f:
            f.write(new_str)
        print('file written to receiver/inventory.txt')
    # Success message
    elif lines[1].strip() == 'success':
        print('Success')
    # Some sort of error received
    elif lines[1].strip() == 'error':
        print('Error received: ' + lines[2])
    else:
        # Unknown response
        print('Unknown error received from server')