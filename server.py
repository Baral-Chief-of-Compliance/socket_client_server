import socket
from for_requests import get_timetable
from for_parser import timetable_on_week, timetable_on_today

get_timetable()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()

conn.send('connect'.encode())
while True:
    message = conn.recv(4000)
    message = message.decode()
    print('client: ', message)

    if message == 'сегодня':
        conn.send(timetable_on_today().encode())
    elif message == 'неделя':
        conn.send(timetable_on_week().encode())
    else:
        conn.send('сообщение получено'.encode())



