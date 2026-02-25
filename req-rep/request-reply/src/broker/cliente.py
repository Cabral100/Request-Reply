import zmq
import json
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

i = 0
while True:

    print("==== MENU ====")
    print("1 - Criar")
    print("2 - Deletar")
    print("3 - Listar")
    
    
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        msg = {"funcao": "criar", "dados": "teste"}
        msg = json.dumps(msg)
        print(f"{msg}", flush = True)
        socket.send_string(msg)
        mensagem = socket.recv()
        print(f"{mensagem}", flush=True)
        sleep(0.5)

    elif opcao == "2":
        msg = {"funcao": "deletar", "dados": "teste"}
        msg = json.dumps(msg)
        print(f"{msg}", flush = True)
        socket.send_string(msg)
        mensagem = socket.recv()
        print(f"{mensagem}", flush=True)
        sleep(0.5)

    elif opcao == "3":
        msg = {"funcao": "listar", "dados": "teste"}
        msg = json.dumps(msg)    
        print(f"{msg}", flush = True)
        socket.send_string(msg)
        mensagem = socket.recv()
        print(f"{mensagem}", flush=True)
        sleep(0.5)
