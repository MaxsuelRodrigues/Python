from tkinter import *


def Numeros(numero):
    visor.insert(END, str(numero))


def Mais():
    global n1
    global funcao
    n1 = float(visor.get())
    funcao = '+'
    visor.delete(0, END)


def Menos():
    global n1
    global funcao
    n1 = float(visor.get())
    funcao = '-'
    visor.delete(0, END)


def Mult():
    global n1
    global funcao
    n1 = float(visor.get())
    funcao = '*'
    visor.delete(0, END)


def Div():
    global n1
    global funcao
    n1 = float(visor.get())
    funcao = '/'
    visor.delete(0, END)


def CE():
    visor.delete(0, END)


def igual():
    n2 = float(visor.get())
    visor.delete(0, END)
    if funcao == '+':
        n3 = n1 +n2
        if n3 // 1 == n3:
            visor.insert(END, int(n3))
        else:
            visor.insert(END, n3)
    if funcao == '-':
        n3 = n1 - n2
        if n3 // 1 == n3:
            visor.insert(END, int(n3))
        else:
            visor.insert(END, n3)
    if funcao == '*':
        n3 = n1 * n2
        if n3 // 1 == n3:
            visor.insert(END, int(n3))
        else:
            visor.insert(END, n3)
    if funcao == '/':
        n3 = n1 / n2
        if n3 // 1 == n3:
            visor.insert(END, int(n3))
        else:
            visor.insert(END, n3)



# criar a interface
tela = Tk()
tela.geometry('280x390')
tela.title('Calculadora')
tela.resizable(False, False)
tela.configure(bg='#FFFFFF')
# botões numeros
bt0 = Button(text='0', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(0))
bt0.place(x=75, y=320)
bt1 = Button(text='1', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(1))
bt1.place(x=15, y=260)
bt2 = Button(text='2', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(2))
bt2.place(x=75, y=260)
bt3 = Button(text='3', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(3))
bt3.place(x=135, y=260)
bt4 = Button(text='4', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(4))
bt4.place(x=15, y=200)
bt5 = Button(text='5', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(5))
bt5.place(x=75, y=200)
bt6 = Button(text='6', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(6))
bt6.place(x=135, y=200)
bt7 = Button(text='7', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(7))
bt7.place(x=15, y=140)
bt8 = Button(text='8', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(8))
bt8.place(x=75, y=140)
bt9 = Button(text='9', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=lambda: Numeros(9))
bt9.place(x=135, y=140)

# botões operações
btmais = Button(text='+', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=Mais)
btmais.place(x=195, y=260)
btmenos = Button(text='-', padx=22, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=Menos)
btmenos.place(x=195, y=200)
btmulti = Button(text='X', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold',command=Mult)
btmulti.place(x=195, y=140)
btmulti = Button(text='÷', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold',command=Div)
btmulti.place(x=195, y=80)


# botões especiai
btce = Button(text='CE', padx=75, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=CE)
btce.place(x=15, y=80)
bt = Button(text=',', padx=20, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold',command= lambda: Numeros(','))
bt.place(x=15, y=320)
# botão igual
btigual = Button(text='=', padx=50, pady=15, bg='#003B45', fg='#FFFFFF', font='arial 10 bold', command=igual)
btigual.place(x=135, y=320)
# visor
visor = Entry(tela, bg='#005c6b', fg='#FFFFFF', font='arial 20 bold')
visor.place(x=15, y=20, width=239, height=50)

tela.mainloop()