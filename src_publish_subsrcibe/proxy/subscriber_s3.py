import zmq

context = zmq.Context()
sub = context.socket(zmq.SUB)

sub.setsockopt_string(zmq.SUBSCRIBE, "")
sub.connect("tcp://proxy:5556")

print("S3: Aguardando todas as publicações")

while True:
    message = sub.recv_string()
    print(f"S3 recebeu: {message}", flush=True)