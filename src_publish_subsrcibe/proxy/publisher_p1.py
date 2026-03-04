import zmq
import time
from datetime import datetime

context = zmq.Context()
pub = context.socket(zmq.PUB)
pub.connect("tcp://proxy:5555") 

while True:
    hora = datetime.now().strftime("%H:%M:%S")
    message = f"hora {hora}"
    pub.send_string(message)
    print(f"P1 enviando: {message}", flush=True)
    time.sleep(1)