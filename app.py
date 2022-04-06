from asyncio import run_coroutine_threadsafe
from cProfile import label
from cgitb import text
from ctypes.wintypes import PCHAR
from email.mime import image
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font

# importando o pillow
from PIL import Image, ImageTk

import random

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima

app_1 = Label(frame_cima, text="Voce", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

app_ = Label(frame_cima, text=":", height=3, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="Bot", height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_bot = Label(frame_baixo, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_bot.place(x=190, y=10)

global voce
global bot
global rouds
global pntos_voce
global pontos_bot

pontos_voce = 0
pontos_bot = 0
rouds = 5

# Função Logica do Jogo
def jogar(i):
    global rouds
    global pontos_voce
    global pontos_bot

    if rouds >0:
        print(rouds)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        bot = random.choice(opcoes)
        voce = i

        app_bot['text'] = bot
        app_bot['fg'] = co1

        # caso for igual 
        if voce == "Pedra" and bot == "Pedra":
            print("Empate")
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co3
            app_linha['bg'] = co3

        elif voce == "Papel" and bot == "Papel":
            print("Empate")
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co3
            app_linha['bg'] = co3

        elif voce == "Tesoura" and bot == "Tesoura":
            print("Empate")
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co3
            app_linha['bg'] = co3

        # para frente.
        #Bot Ganhou.
        elif voce == "Pedra" and bot == "Papel":
            print("Bot Ganhou!")
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co5
            app_linha['bg'] = co5

            pontos_bot += 10

        elif voce == "Papel" and bot == "Tesoura":
            print("Bot Ganhou!")
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co5
            app_linha['bg'] = co5

            pontos_bot += 10

        elif voce == "Tesoura" and bot == "Pedra":
            print("Bot Ganhou!")
            app_1_linha['bg'] = co5
            app_2_linha['bg'] = co5
            app_linha['bg'] = co5

            pontos_bot += 10

        # Você Ganhou.
        elif voce == "Pedra" and bot == "Tesoura":
            print("Você Ganhou!")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co4
            app_linha['bg'] = co4

            pontos_voce += 10
        
        elif voce == "Papel" and bot == "Pedra":
            print("Você Ganhou!")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co4
            app_linha['bg'] = co4

            pontos_voce += 10

        elif voce == "Tesoura" and bot == "Papel":
            print("Você Ganhou!")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co4
            app_linha['bg'] = co4

            pontos_voce += 10

        # Atulizando a pontuação
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_bot

        # Atulizando a pontução
        rouds -= 1

        
    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_bot

        # Chamando a Função Terminar
        fim_do_jogo()

# Função Iniciar o Jogo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo,command=lambda: jogar('Pedra'), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0,  font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0,  font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0,  font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)

# Função Terminar o jogo
def fim_do_jogo():
    global rouds
    global pontos_voce
    global pontos_bot

    # Reiniciando as Variaveis para Zerar Novameentee o Jogo.
    pontos_voce = 0
    pontos_bot = 0
    rouds = 5

    # Destruindo os Botões de opcoes
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # Definindo o Ganhandor.
    jogador_voce = int(app_1_pontos['text'])
    jogador_bot = int(app_2_pontos["text"])

    if jogador_voce > jogador_bot: 
        app_vencedor = Label(frame_baixo, text="Parabéns Você Ganhou !!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif jogador_voce < jogador_bot: 
        app_vencedor = Label(frame_baixo, text="Infelizmentee Você perdeu !!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text="Foi um Empate !!!", height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_vencedor.place(x=5, y=60)

    # Jogar Denovo.
    def jogar_denovo():
        app_1_pontos['text'] ='0'
        app_2_pontos['text'] ='0'
        app_vencedor.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='Jogar Denovo?', bg=fundo, fg=co0,  font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=140)


# Botão de Jogar
b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0,  font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=140)



janela.mainloop()