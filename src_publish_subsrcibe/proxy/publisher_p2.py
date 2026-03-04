import zmq
import time
import random

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555")

while True:
    num = random.randint(1, 6)
    message = f"random {num}"
    pub.send_string(message)
    print(f"P2 enviando: {message}", flush=True)
    time.sleep(1)