import asyncio
import json
import persistance
from datetime import datetime
from nats.aio.client import Client as NATS

# Connection to NATS
nc = NATS()

prices = [
    ('200', '2020-10-28'),
    ('205', '2020-10-29')
]

class Message:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

test_data = [
    Message("subject-1", prices[0]),
    Message("subject-2", prices[1]),
]

async def disconnected_cb():
   print("Got disconnected!")

async def reconnected_cb():
   # See who we are connected to on reconnect.
   print("Got reconnected to {url}".format(url=nc.connected_url.netloc))

async def error_cb(e):
    print("Error:", e)

async def connect(loop):
    await nc.connect(
        servers=["nats://127.0.0.1:4222"],
        reconnect_time_wait=10,
        reconnected_cb=reconnected_cb,
        disconnected_cb=disconnected_cb,
        error_cb=error_cb,
        io_loop=loop,
    )

    print("Connected to NATS at {}...".format(nc.connected_url.netloc))

async def close_connection():
    await nc.close()

async def send_message(message):
    timestamp = datetime.utcnow().isoformat()
    event = {'msg': message.body, 'timestamp': timestamp}
    await nc.publish("%s" % message.subject, json.dumps(event).encode())
    print('message sent to [%s]' % message.subject)


async def pub(loop):
    await connect(loop)
    con = persistance.connect()
    persistance.init(con)

    await asyncio.sleep(3)
    await send_message(test_data[0])
    persistance.insert(con, prices[0])
    
    await asyncio.sleep(3)
    await send_message(test_data[1])
    persistance.insert(con, prices[1])

    persistance.fetch(con)

    await close_connection()


def init():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pub(loop))
    loop.close()
