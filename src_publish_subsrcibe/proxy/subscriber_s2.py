import zmq

context = zmq.Context()
sub = context.socket(zmq.SUB)
sub.setsockopt_string(zmq.SUBSCRIBE, "random")
sub.connect("tcp://proxy:5556")

print("S2: Aguardando apenas números aleatórios")

while True:
    message = sub.recv_string()
    print(f"S2 recebeu: {message}", flush=True)