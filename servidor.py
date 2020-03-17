import socket
import time

# Informacoes do socket, socket.SOCK_STREAM indica que este utiliza TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 5450))

# Espera e conecta com os 2 clientes
s.listen(2)
cliente1, endereco1 = s.accept()
print(endereco1)
cliente2, endereco2 = s.accept()
print('Conectado')

# Define o numero de linhas da tabela
cliente1.send(str.encode('5'))
cliente2.send(str.encode('5'))
time.sleep(0.5)

# Define o colunas de linhas da tabela
cliente1.send(str.encode('5'))
cliente2.send(str.encode('5'))
time.sleep(0.5)

# Define a chance de minas na tabela
cliente1.send(str.encode('4'))
cliente2.send(str.encode('4'))
time.sleep(0.5)

# Variaveis de inicio e fim
ready = 0
stop = 0

while stop == 0:

    # Recebe a mensagem de que o cliente esta pronto pra jogar
    info1 = cliente1.recv(1024)
    info2 = cliente2.recv(1024)

    if info1.decode('utf-8') == 'ready':
        # Um cliente conectado com sucesso
        ready += 1

    if info2.decode('utf-8') == 'ready':
        # Dois clientes conectados com sucesso
        ready += 1

    if ready == 2:
        cliente1.send(str.encode(
            ' ---------------------------------------------- \n|                                             |\n|           VOCE EH O JOGADOR 1               |\n|                                             |\n --------------------------------------------- \n\nPreparado?\n'))
        cliente2.send(str.encode(
            ' ---------------------------------------------- \n|                                             |\n|           VOCE EH O JOGADOR 2               |\n|                                             |\n --------------------------------------------- \n\nPreparado?\n'))
        stop = 1

while stop == 1:
    # Essas variaveis recebem o resultado de cada partida
    info3 = cliente1.recv(1024)
    info4 = cliente2.recv(1024)

    if not info1 and not info2:
        # Caso nao tenha confirmacao de conexao
        stop = 2
        print('Os dois jogadores deixaram a partida.')
        break

    # Resultados das partidas
    info3 = info3.decode('utf-8')
    info4 = info4.decode('utf-8')
    print(info3)
    print(info4)

    # Os dois jogadores explodiram minas e ambos perderam
    if info3 == 'fail' and info4 == 'fail':
        mensagem_final = '\n       ___   ___    ___    ___  ___  ___      \n       / _ \ / __|  |   \  / _ \|_ _|/ __|     \n      | (_) |\__ \  | |) || (_) || | \__ \     \n  ___  \___/_|___/__|___/_ \___/|___||___/  __ \n | _ \| __|| _ \|   \ | __|| _ \  /_\  |  \/  |\n |  _/| _| |   /| |) || _| |   / / _ \ | |\/| |\n |_|  |___||_|_\|___/ |___||_|_\/_/ \_\|_|  |_|\n'
        cliente1.send(str.encode(mensagem_final))
        cliente2.send(str.encode(mensagem_final))
        stop = 2

    # O jogador 1 acertou uma mina e o jogador 2 ganhou pois nao acertou nenhuma
    elif info3 == 'fail' and info4 != 'fail':
        mensagem_final1 = (
                    '     __   __ ___    ___  ___      \n     \ \ / // _ \  / __|| __|     \n      \ V /| (_) || (__ | _|      \n  ___  \_/  \___/__\___||___|   _ \n | _ \| __|| _ \|   \ | __|| | | |\n |  _/| _| |   /| |) || _| | |_| |\n |_|  |___||_|_\|___/ |___| \___/ \n\n  O Jogador 2 nao acertou nenhuma mina!\n   O tempo dele foi de: ' + str(
                info4))
        mensagem_final2 = (
                    '  ___   _    ___    _    ___  ___  _  _  ___ \n | _ \ /_\  | _ \  /_\  | _ )| __|| \| |/ __| \n |  _// _ \ |   / / _ \ | _ \| _| | .` |\__ \ \n |_| /_/ \_\|_|_\/_/ \_\|___/|___||_|\_||___/ \n   \n Voce venceu!!\n  O Jogador 1 acertou uma mina.\n   Seu tempo foi de: ' + str(
                info4))
        cliente1.send(str.encode(mensagem_final1))
        cliente2.send(str.encode(mensagem_final2))
        stop = 2

    # O jogador 2 acertou uma mina e o jogador 2 ganhou pois nao acertou nenhuma
    elif info3 != 'fail' and info4 == 'fail':
        mensagem_final1 = (
                    '  ___   _    ___    _    ___  ___  _  _  ___ \n | _ \ /_\  | _ \  /_\  | _ )| __|| \| |/ __| \n |  _// _ \ |   / / _ \ | _ \| _| | .` |\__ \ \n |_| /_/ \_\|_|_\/_/ \_\|___/|___||_|\_||___/ \n   \nVoce venceu!!\n\nO Jogador 2 acertou uma mina.\nSeu tempo foi de: ' + str(
                info3))
        mensagem_final2 = (
                    '     __   __ ___    ___  ___      \n     \ \ / // _ \  / __|| __|     \n      \ V /| (_) || (__ | _|      \n  ___  \_/  \___/__\___||___|   _ \n | _ \| __|| _ \|   \ | __|| | | |\n |  _/| _| |   /| |) || _| | |_| |\n |_|  |___||_|_\|___/ |___| \___/ \n\nO Jogador 1 nao acertou nenhuma mina!\nO tempo dele foi de: ' + str(
                info3))
        cliente1.send(str.encode(mensagem_final1))
        cliente2.send(str.encode(mensagem_final2))
        stop = 2

    # Nenhum dos jogadores acertaram minas, o jogador 1 teve o menor tempo e ganhou
    elif float(info3) < float(info4):
        ganhador = str(
            '  ___   _    ___    _    ___  ___  _  _  ___ \n | _ \ /_\  | _ \  /_\  | _ )| __|| \| |/ __| \n |  _// _ \ |   / / _ \ | _ \| _| | .` |\__ \ \n |_| /_/ \_\|_|_\/_/ \_\|___/|___||_|\_||___/ \n   \nVoce venceu!!\nO seu tempo foi o menor!\n\nSeu tempo: ' + str(
                info3) + '\n\nTempo do Jogador 2: ' + str(info4))
        perdedor = str(
            '     __   __ ___    ___  ___      \n     \ \ / // _ \  / __|| __|     \n      \ V /| (_) || (__ | _|      \n  ___  \_/  \___/__\___||___|   _ \n | _ \| __|| _ \|   \ | __|| | | |\n |  _/| _| |   /| |) || _| | |_| |\n |_|  |___||_|_\|___/ |___| \___/ \n\nO seu tempo foi o maior\n\nSeu tempo: ' + str(
                info4) + '\n\nTempo do Jogador 1: ' + str(info3))
        cliente1.send(str.encode(ganhador))
        cliente2.send(str.encode(perdedor))
        stop = 2

    # Nenhum dos jogadores acertaram minas, o jogador 2 teve o menor tempo e ganhou
    else:
        ganhador = str(
            '  ___   _    ___    _    ___  ___  _  _  ___ \n | _ \ /_\  | _ \  /_\  | _ )| __|| \| |/ __| \n |  _// _ \ |   / / _ \ | _ \| _| | .` |\__ \ \n |_| /_/ \_\|_|_\/_/ \_\|___/|___||_|\_||___/ \n   \nVoce venceu!!\nO seu tempo foi o menor!\n\nSeu tempo: ' + str(
                info4) + '\n\nTempo do Jogador 2: ' + str(info3))
        perdedor = str(
            '     __   __ ___    ___  ___      \n     \ \ / // _ \  / __|| __|     \n      \ V /| (_) || (__ | _|      \n  ___  \_/  \___/__\___||___|   _ \n | _ \| __|| _ \|   \ | __|| | | |\n |  _/| _| |   /| |) || _| | |_| |\n |_|  |___||_|_\|___/ |___| \___/ \n\nO seu tempo foi o maior\n\nSeu tempo: ' + str(
                info3) + '\n\nTempo do Jogador 1: ' + str(info4))
        cliente1.send(str.encode(perdedor))
        cliente2.send(str.encode(ganhador))
        stop = 2
