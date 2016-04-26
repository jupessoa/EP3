# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 10:45:26 2016

@author: Henrique
"""
import numpy as np

class JogoDaVelha:
    def __init__(self):
        self.limpa_jogadas()
        
    def recebe_jogada(self, linha, coluna):
        self.tabuleiro[linha][coluna]=self.jogador
        self.conta_jogadas += 1
        
        if self.jogador == 1:
            self.jogador = 2
        else:
            self.jogador = 1

    def verifica_ganhador(self):
        if self.tabuleiro[0][0] == 1 and self.tabuleiro[0][1] == 1 and self.tabuleiro[0][2] == 1:
            return 1
        elif self.tabuleiro[1][0] == 1 and self.tabuleiro[1][1] == 1 and self.tabuleiro[1][2] == 1:
            return 1    
        elif self.tabuleiro[2][0] == 1 and self.tabuleiro[2][1] == 1 and self.tabuleiro[2][2] == 1:
            return 1
        elif self.tabuleiro[0][0] == 2 and self.tabuleiro[0][1] == 2 and self.tabuleiro[0][2] == 2:
            return 2
        elif self.tabuleiro[1][0] == 2 and self.tabuleiro[1][1] == 2 and self.tabuleiro[1][2] == 2:
            return 2    
        elif self.tabuleiro[2][0] == 2 and self.tabuleiro[2][1] == 2 and self.tabuleiro[2][2] == 2:
            return 2
        elif self.tabuleiro[0][0] == 1 and self.tabuleiro[1][0] == 1 and self.tabuleiro[2][0] == 1:
            return 1
        elif self.tabuleiro[0][1] == 1 and self.tabuleiro[1][1] == 1 and self.tabuleiro[2][1] == 1:
            return 1    
        elif self.tabuleiro[0][2] == 1 and self.tabuleiro[1][2] == 1 and self.tabuleiro[2][2] == 1:
            return 1
        elif self.tabuleiro[0][0] == 2 and self.tabuleiro[1][0] == 2 and self.tabuleiro[2][0] == 2:
            return 2
        elif self.tabuleiro[0][1] == 2 and self.tabuleiro[1][1] == 2 and self.tabuleiro[2][1] == 2:
            return 2    
        elif self.tabuleiro[0][2] == 2 and self.tabuleiro[1][2] == 2 and self.tabuleiro[2][2] == 2:
            return 2
        elif self.tabuleiro[0][0] == 1 and self.tabuleiro[1][1] == 1 and self.tabuleiro[2][2] == 1:
            return 1
        elif self.tabuleiro[0][0] == 2 and self.tabuleiro[1][1] == 2 and self.tabuleiro[2][2] == 2:
            return 2
        elif self.tabuleiro[0][2] == 1 and self.tabuleiro[1][1] == 1 and self.tabuleiro[2][0] == 1:
            return 1
        elif self.tabuleiro[0][2] == 2 and self.tabuleiro[1][1] == 2 and self.tabuleiro[2][0] == 2:
            return 2
        elif self.conta_jogadas == 9:
            return 0
        else:
            return -1
        
            
    def limpa_jogadas(self):
        self.tabuleiro = np.zeros([3, 3])
        self.conta_jogadas = 0
        self.jogador = 1
        
    
