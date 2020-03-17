import time
import random
import socket

# Conecta no socket
s = socket.socket()
s.connect((socket.gethostname(), 5450))

# Recebe e mostra o numero de linhas
rows = s.recv(1024)
rows = int(rows.decode('utf-8'))
print(
    '        ___    _    __  __  ___   ___      \n       / __|  /_\  |  \/  || _ \ / _ \     \n      | (__  / _ \ | |\/| ||  _/| (_) |    \n     __\___|/_/_\_\|_|  |_||_| __\___/___  \n    |  \/  ||_ _|| \| |  /_\  |   \  / _ \ \n    | |\/| | | | | .` | / _ \ | |) || (_) |\n    |_|  |_||___||_|\_|/_/ \_\|___/  \___/ \n\n')
print('Numero de linhas: ' + str(rows))
time.sleep(0.5)

# Recebe e mostra o numero de colunas
columns = s.recv(1024)
columns = int(columns.decode('utf-8'))
print('Numero de Colunas: ' + str(columns))
time.sleep(0.5)

# Recebe e mostra a chance de minas em cada linha
chance_mina = s.recv(1024)
chance_mina = int(chance_mina.decode('utf-8'))
print('A chance de minas por linha vai de 0 a ' + str(chance_mina))
time.sleep(0.5)

# Envia informacao de que o cliente esta pronto para jogar
s.send(str.encode('ready'))
print('\nEsperando o outro jogador se conectar\n')
time.sleep(0.5)

# Recebe e mostra qual o numero do jogador
Numero_jogador = s.recv(1024)
Numero_jogador = Numero_jogador.decode('utf-8')
print(Numero_jogador)
time.sleep(0.5)

# Contagem regressiva para o jogo comecar
for x in range(5):
    print(5 - x)
    time.sleep(1)
print('\nVAI!\n')

# Inicia o tempo e o tabuleiro
tempo_inicio = time.time()
Tabuleiro = []

# Montagem do tabuleiro
# Passa linha por linha
for x in range(rows):
    Tabuleiro.append(["-"] * columns)
    # Coloca um - na linha para cada coluna

# Inicia as minas
Minas = []

# Passa linha por linha
for x in range(rows):
    Minas.append([random.randint(0, chance_mina) for x in range(columns)])
    # Gera um numero (posicao) aleatoria para a mina

# Variavel que finaliza o jogo
game_over = False
print('')

espacos_restantes = 0

# Passa por cada linha do array com as minas
for row in Minas:
    for num in row:
        if num != chance_mina:
            # Faz a contagem de quantos espacos SEM minas existem
            espacos_restantes += 1

# Enquanto o jogo nao acaba
while game_over == False:

    # Imprime a primeira linha com os numeradores das colunas
    for x in range(columns):
        indice_coluna = x + 1
        try:
            if indice_coluna == 1:
	        # Se a numeracao da coluna for 1, coloca um espaco antes para alinhar os numeros
                print('  ' + str(indice_coluna)),
            else:
		# Printa a numeracao das colunas
                print(str(indice_coluna)),
        except:
            print(' ')
    print(' ')

    #Variavel da numeracao das linhas
    indice_linha = 0

    #Para cada linha imprime o numero dela
    for row in Tabuleiro:
        indice_linha += 1
        print(str(indice_linha) * ((len(str(rows)) + 1) - len(str(indice_linha)))),
        print(" ".join(row)) #Concatena as strings e coloca um espaco entre elas

    # Variaveis que guardam as linhas e colunas escolhidas
    linha_escolhida = 0
    coluna_escolhida = 0

    while coluna_escolhida not in range(1, columns + 1):
        try:
            coluna_escolhida = int(input('\nEscolha uma coluna: '))
        except:
            pass

    while linha_escolhida not in range(1, rows + 1):
        try:
            linha_escolhida = int(input('\nEscolha uma linha: '))
        except:
            pass

    # Diminui 1 das linhas e colunas pois elas iniciam a contagem no 0
    linha_escolhida -= 1
    coluna_escolhida -= 1
    # Variavel que guarda a quantidade de minas ao redor da posicao escolhida
    minas_perto = 0

    # Posicao escolhida igual a de uma mina, explode a mina
    if Minas[linha_escolhida][coluna_escolhida] == chance_mina:
        print(
            '\n\n     _.-^^---....,,--\n _--                  --_\n<          BUMMM         >)\n|                         |\n \._                   _./\n    ```--. . , ; .--```\n          | |   |\n       .-=||  | |=-.\n       `-=#$%&%$#=-`\n          | ;  :|\n _____.,-#%&$@%#&#~,._____')
        print('\n  Voce explodiu uma mina!\n\n')
        game_over = 2

    else:
        # Posicao sem mina, verifica se ha minas ao redor da posicao escolhida
        try:
            if Minas[linha_escolhida - 1][
                coluna_escolhida - 1] == chance_mina and linha_escolhida > 0 and coluna_escolhida > 0:
                # Verifica se ha uma mina na POSICAO DIAGONAL ACIMA ESQUERDA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida][coluna_escolhida - 1] == chance_mina and coluna_escolhida > 0:
                # Verifica se ha uma mina na POSICAO A ESQUERDA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida + 1][coluna_escolhida - 1] == chance_mina and coluna_escolhida > 0:
                # Verifica se ha uma mina na POSICAO DIAGONAL ABAIXO ESQUERDA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida - 1][coluna_escolhida] == chance_mina and linha_escolhida > 0:
                # Verifica se ha uma mina na POSICAO ACIMA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida + 1][coluna_escolhida] == chance_mina:
                # Verifica se ha uma mina na POSICAO ABAIXO da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:

            if Minas[linha_escolhida - 1][coluna_escolhida + 1] == chance_mina and linha_escolhida > 0:
                # Verifica se ha uma mina na POSICAO DIAGONAL ACIMA DIREITA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida][coluna_escolhida + 1] == chance_mina:
                # Verifica se ha uma mina na POSICAO A DIREITA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass
        try:
            if Minas[linha_escolhida + 1][coluna_escolhida + 1] == chance_mina:
                # Verifica se ha uma mina na POSICAO DIAGONAL ABAIXO DIREITA da escolhida e se a posicao existe
                minas_perto += 1
        except:
            pass

        # Coloca o numero total de minas perto da posicao escolhida
        Tabuleiro[linha_escolhida][coluna_escolhida] = str(minas_perto)
        # Diminui os espacos restantes
        espacos_restantes -= 1

        # Se nao ha espacos restantes, o jogador ganhou
        if espacos_restantes == 0:
            game_over = 1

if game_over == 1:
    # Informa que o jogador nao atingiu nenhuma mina e terminou o jogo
    tempo_fim = time.time()
    # Calcula o tempo da partida
    tempo_partida = tempo_fim - tempo_inicio
    s.send(str.encode(str(tempo_partida)))
    print('\nEsperando o outro jogador terminar a partida\n')
    time.sleep(0.5)
    resultado_final = s.recv(1024)
    print(resultado_final.decode('utf-8'))

else:
    # Informa que o jogador atingiu uma mina e perdeu
    s.send(str.encode('fail'))
    time.sleep(0.5)
    resultado_final = s.recv(1024)
    print(resultado_final.decode('utf-8'))
