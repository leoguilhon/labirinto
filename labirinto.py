ponto_de_chegada = 10
frente = 3
direita = 2
esquerda = -1
posicao = 0
posicao_anterior = 0
chegou = False

def checarPosicao(posicao):
    posicao = int(posicao)
    if (posicao > posicao_anterior and posicao < ponto_de_chegada) or (posicao < posicao_anterior and posicao > ponto_de_chegada):
        print('Você está se aproximando da saída.')
        return False
    if (posicao > posicao_anterior and posicao > ponto_de_chegada) or (posicao < posicao_anterior and posicao < ponto_de_chegada):
        print('Você está se afastando da saída.')
        return False
    if posicao == ponto_de_chegada:
        print('Você chegou ao final do labirinto! Parabéns!')
        return True


while chegou is False:

    escolha = int(input('Escolha uma direção para seguir no labirinto: (1) frente (2) direita (3) esquerda'))

    if escolha == 1:
        posicao_anterior = posicao
        posicao += frente
        chegou = checarPosicao(posicao)
    if escolha == 2:
        posicao_anterior = posicao
        posicao += direita
        chegou = checarPosicao(posicao)
    if escolha == 3:
        posicao_anterior = posicao
        posicao += esquerda
        chegou = checarPosicao(posicao)


