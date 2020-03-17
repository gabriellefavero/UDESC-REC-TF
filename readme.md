Trabalho final realizado em novembro de 2018, no sexto semestre da faculdade.

Linguagem: Python <br>
Disciplina: Redes <br>
Curso: Tecnologia em análise e desenvolvimento de sistemas <br>
Instituição: UDESC - Universidade do Estado de Santa Catarina <br>

Desenvolvimento prático de uma aplicação com Sockets Cliente-Servidor. <br>

Para executar em apenas um computador (1 terminal para servidor, 2 para clientes):
* Não é necessária nenhuma alteração no código

Para executar em computadores diferentes:
* Primeiramente deve-se copiar o ip do computador que será o servidor.
* O ip deverá ser inserido na linha de número 7 do arquivo servidor.py (entre as aspas) e cliente.py (substituindo o comando socket.gethostname() e entre aspas).
*A porta pode se manter a mesma a não ser que coincidentalmente esteja sendo usada por outro programa.

* Deve ser executado o arquivo servidor.py com o comando "python servidor.py" no terminal, ele ficará esperando a conexão dos clientes.
* Deve ser executado o arquivo cliente.py com o comando "python cliente.py", se o servidor imprimir o ip do cliente, significa que o cliente 1 foi conectado com sucesso.
	- O cliente 1 ficará aguardando a conexão do segundo para mostrar o jogo.
* Ao conectar o segundo cliente, o servidor mostrará a mensagem "conectado" e o jogo iniciará para ambos clientes.
* É mostrada após a contagem regressiva, a tabela do jogo, com linhas e colunas enumeradas.
* O jogador deve então inserir as coordenadas da posição que deseja selecionar. É solicitado primeiro o número da coluna e após, o número da linha.
* A matriz aparece atualizada com a posição selecionada representada pelo número de minas presentes aos arredores da posição selecionada. Com esta informação o jogador deve planejar suas próximas jogadas.
* O mesmo passo é repetido até que o cliente atinja uma mina ou até que ele ganhe, selecionando todas as posições em que não hajam minas.
* Em ambos os casos um dos clientes aguarda o outro terminar o jogo.
* O Jogo pode acabar de três formas:
	- Os dois jogadores atingem minas, ambos perdem.
	- Um jogador atige uma mina, o outro completa o jogo, vencendo
	- Ambos completam o jogo sem atingir minas, neste caso o vencedor será o jogador que completou o jogo em menos tempo.
* Ao acabar o jogo, o servidor mostra dados do resultado para o cliente 1 e cliente 2 consecutivamente (o resultado consiste no tempo total de jogo ou "fail"), depois o servidor e os clientes se desconectam automaticamente.
