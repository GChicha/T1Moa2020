#! /bin/env python

import heapq
import time

tabuleiroFinal = (1,2,3,4,12,13,14,5,11,0,15,6,10,9,8,7)

class Peca():
    def __init__(self, tabuleiro, indexZero, pai = None, g = 0):
        self.tabuleiro = tabuleiro
        self.indexZero = indexZero
        self.pai = pai
        self.g = g
        self.f = g + heuristicaUm(tabuleiro)

    def __eq__(self, other):
        return self.tabuleiro == other.tabuleiro

    def __lt__(self,other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __hash__(self):
        return hash(self.tabuleiro)

def readInput():
    #entrada = tuple(map(int, input().split()))
    entrada = tuple(map(int, ('  12 1 3 0 11 2 15 14 10 13 8 4 9 7 6 5').split()))
    return entrada

def heuristicaUm(tabuleiro):
    return len(list(filter(lambda x: x[0] != x[1], zip(tabuleiro, tabuleiroFinal))))

def swap_tuple(set_to_swap, index_origin, index_dest):
    to_list = list(set_to_swap)
    to_list[index_dest], to_list[index_origin] = to_list[index_origin], to_list[index_dest]
    return tuple(to_list)

def geraSucessores(noPai):
    if noPai.indexZero >= 4:
        newIndexNulo = noPai.indexZero - 4
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero <12 :
        newIndexNulo = noPai.indexZero + 4
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero %4 != 3:
        newIndexNulo = noPai.indexZero + 1
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

    if noPai.indexZero %4 != 0:
        newIndexNulo = noPai.indexZero - 1
        yield swap_tuple(noPai.tabuleiro, noPai.indexZero, newIndexNulo), newIndexNulo

def AEstrela(noI):
    start = time.process_time()

    listaAberta = []        #heapq 
    listaFechada = set()   #set

    heapq.heappush(listaAberta, noI)

    while (selecionado := heapq.heappop(listaAberta)) and selecionado.tabuleiro != tabuleiroFinal:
        listaFechada.add(selecionado.tabuleiro)

        for filho, indexZero in geraSucessores(selecionado):
            if filho not in listaFechada:
                heapq.heappush(listaAberta, Peca(filho, indexZero, selecionado, selecionado.g + 1))

    print(time.process_time() - start)

    return selecionado.g


def main():
    inicial = Peca(readInput(), 3)
    resultado = AEstrela(inicial)
    print(resultado)

if __name__ == '__main__':
    main()
