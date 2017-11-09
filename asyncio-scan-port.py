import asyncio
import time
import socket

async def sock_connect(address, s, ports=None, loop=None):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(False)
    sock.settimeout(1)
    if loop is None:
        loop = asyncio.get_event_loop()
    try:
        async with s:
            await loop.sock_connect(sock, address)
    except (ConnectionRefusedError, Exception) as err:
        return False, None
    print(address)
    ports.append(address)
    return True, address

def port_scan(host, ports, pool):
    a, b = ports.split('-')
    a, b = int(a), int(b)
    s = asyncio.Semaphore(10)
    loop = asyncio.get_event_loop()
    tasks = []
    for port in range(a, b+1):
        tasks.append(sock_connect((host, port), s, pool, loop))
    return tasks

def main():
    host = '144.168.61.37'
    ports = '1-65535'
    pool = []
    tasks = port_scan(host, ports, pool)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    print('\n\n')
    for i in pool:
        print(i)

if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time() - t1
    print("elapsed time: ", t2)


