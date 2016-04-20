# -*- coding: utf-8 -*-

import tkinter as tk

from JogoDaVelha import JogoDaVelha

class Tabuleiro:
    def __init__(self):
        self.jogo = JogoDaVelha()
        self.jogo.limpa_jogadas()        
        
        self.window = tk.Tk()
        self.window.geometry("300x350+100+100")
        self.window.rowconfigure(0, minsize=100)
        self.window.rowconfigure(1, minsize=100)
        self.window.rowconfigure(2, minsize=100)
        self.window.rowconfigure(3, minsize=50)
        self.window.columnconfigure(0, minsize=100)
        self.window.columnconfigure(1, minsize=100)
        self.window.columnconfigure(2, minsize=100)

        self.chama_jogador = tk.Label(self.window)
        self.chama_jogador.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.chama_jogador.configure(text="Jogador X")
        
        self.botao1 = tk.Button(self.window)
        self.botao1.configure(command=self.botao1_clicado)
        self.botao1.grid(row=0, column=0, sticky="nsew")
        
        self.botao2 = tk.Button(self.window)
        self.botao2.configure(command=self.botao2_clicado)
        self.botao2.grid(row=0, column=1, sticky="nsew")
        
        self.botao3 = tk.Button(self.window)
        self.botao3.configure(command=self.botao3_clicado)
        self.botao3.grid(row=0, column=2, sticky="nsew")
        
        self.botao4 = tk.Button(self.window)
        self.botao4.configure(command=self.botao4_clicado)
        self.botao4.grid(row=1, column=0, sticky="nsew")
        
        self.botao5 = tk.Button(self.window)
        self.botao5.configure(command=self.botao5_clicado)
        self.botao5.grid(row=1, column=1, sticky="nsew")
        
        self.botao6 = tk.Button(self.window)
        self.botao6.configure(command=self.botao6_clicado)
        self.botao6.grid(row=1, column=2, sticky="nsew")
        
        self.botao7 = tk.Button(self.window)
        self.botao7.configure(command=self.botao7_clicado)
        self.botao7.grid(row=2, column=0, sticky="nsew")
        
        self.botao8 = tk.Button(self.window)
        self.botao8.configure(command=self.botao8_clicado)
        self.botao8.grid(row=2, column=1, sticky="nsew")
        
        self.botao9 = tk.Button(self.window)
        self.botao9.configure(command=self.botao9_clicado)
        self.botao9.grid(row=2, column=2, sticky="nsew")
    
    def botao1_clicado(self):
        if self.jogo.jogador == 1:
            self.botao1.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(0,0)
            
        else:
            self.botao1.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(0,0)
            
    def botao2_clicado(self):
        if self.jogo.jogador == 1:
            self.botao2.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(0,1)
            
        else:
            self.botao2.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(0,1)
        self.jogo.limpa_jogadas()    
            
    def botao3_clicado(self):
        if self.jogo.jogador == 1:
            self.botao3.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(0,2)
            
        else:
            self.botao3.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(0,2)
        self.jogo.limpa_jogadas()
            
    def botao4_clicado(self):
        if self.jogo.jogador == 1:
            self.botao4.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(1,0)
            
        else:
            self.botao4.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(1,0)
        self.jogo.limpa_jogadas()    
            
    def botao5_clicado(self):
        if self.jogo.jogador == 1:
            self.botao5.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(1,1)
            
        else:
            self.botao5.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(1,1)
        self.jogo.limpa_jogadas()    
            
    def botao6_clicado(self):
        if self.jogo.jogador == 1:
            self.botao6.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(1,2)
            
        else:
            self.botao6.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(1,2)
        self.jogo.limpa_jogadas()    
            
    def botao7_clicado(self):
        if self.jogo.jogador == 1:
            self.botao7.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(2,0)
            
        else:
            self.botao7.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(2,0)
        self.jogo.limpa_jogadas()   
            
    def botao8_clicado(self):
        if self.jogo.jogador == 1:
            self.botao8.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(2,1)
            
        else:
            self.botao8.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(2,1)
        self.jogo.limpa_jogadas()
            
    def botao9_clicado(self):
        if self.jogo.jogador == 1:
            self.botao9.configure(text="X")
            self.chama_jogador.configure(text="Jogador O")
            self.jogo.recebe_jogada(2,2)
            
        else:
            self.botao9.configure(text="O")
            self.chama_jogador.configure(text="Jogador X")
            self.jogo.recebe_jogada(2,2)
        self.jogo.limpa_jogadas()
        
    def iniciar(self):
        self.window.mainloop()
        
app = Tabuleiro()
app.iniciar()
    
        