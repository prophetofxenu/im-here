import asyncio
from socket import gethostname, socket

server_address = "127.0.0.1"
port = 8888

async def ping(loop):
    reader, writer = await asyncio.open_connection(server_address, port, loop=loop)

    hostname = gethostname()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    writer.write("%s,%s", hostname, local_ip)

    response = await reader.read(200)
    print("Response: " + response.decode())

    writer.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ping(loop))
    loop.close()

