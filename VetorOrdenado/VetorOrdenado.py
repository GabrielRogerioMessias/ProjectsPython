import numpy as np


class VetorOrdenado():
    def __init__(self, tamanhoVetor):
        self.tamanhoVetor = tamanhoVetor
        self.ultimaPosicao = -1
        self.valores = np.empty(self.tamanhoVetor, dtype=int)

    def imprimir(self):
        if self.ultimaPosicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(f'Posição {i} valor {self.valores[i]}')
