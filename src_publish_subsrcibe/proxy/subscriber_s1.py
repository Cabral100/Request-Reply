import zmq

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.setsockopt_string(zmq.SUBSCRIBE, "hora")
sub.connect("tcp://proxy:5556")

print("S1: Aguardando apenas a hora")

while True:
    message = sub.recv_string()
    print(f"S1 recebeu: {message}", flush=True)