import asyncio
import datetime as dt
import os

clients_folder = "./clients/"
port = 8888

async def handle_ping(reader, writer):
    data = await reader.read(100)
    client_hostname = data.decode()
    client_address = writer.get_extra_info("peername")
    
    with open(clients_folder + client_hostname + ".txt", "w") as f:
        f.write("%s: %s" %(client_hostname, client_address[0]))
        f.write("Pinged at " + dt.datetime(2000, 1, 1).now().strftime("%m/%d/%Y %H:%M:%S"))

    message = "Good to see you, %s @ %s" %(client_hostname, client_address[0])
    writer.write(message.encode())
    await writer.drain()
    writer.close()

if __name__ == "__main__":
    if not os.path.exists(clients_folder):
        os.mkdir(clients_folder)

    loop = asyncio.get_event_loop()
    coroutine = asyncio.start_server(handle_ping, port=port, loop=loop)
    server = loop.run_until_complete(coroutine)
    print("Started")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()