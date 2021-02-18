from tkinter import *

app = Tk()
app.title("Calculadora")

Finalmente_achei = 0

#Comando

def clicar_botao(valor):
    global Finalmente_achei
    texto.insert(Finalmente_achei, valor)
    Finalmente_achei +=1

def apagar():
    texto.delete(0, END)   
    Finalmente_achei = 0 

def Motor_da_calculadora():
    equacao = texto.get()
    resultado = eval(equacao)
    texto.delete(0, END)
    texto.insert(0, resultado)
    Finalmente_achei = 0

#Entrada
texto = Entry(app, width=11, font= ("Century 20"))
texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

#Botões

botao1 = Button(app, text="1", width = 5, height=2, command= lambda: clicar_botao(1))
botao2 = Button(app, text="2", width = 5, height=2, command= lambda: clicar_botao(2))
botao3 = Button(app, text="3", width = 5, height=2, command= lambda: clicar_botao(3))
botao4 = Button(app, text="4", width = 5, height=2,command= lambda: clicar_botao(4))
botao5 = Button(app, text="5", width = 5, height=2,command= lambda: clicar_botao(5))
botao6 = Button(app, text="6", width = 5, height=2,command= lambda: clicar_botao(6))
botao7 = Button(app, text="7", width = 5, height=2,command= lambda: clicar_botao(7))
botao8 = Button(app, text="8", width = 5, height=2,command= lambda: clicar_botao(8))
botao9 = Button(app, text="9", width = 5, height=2,command= lambda: clicar_botao(9))
botao0 = Button(app, text="0", width = 13, height=2,command= lambda: clicar_botao(0))

# Botões2


botao_apagar = Button(app, text="Ac", width = 5, height=2,command= lambda: apagar())
botao_pare = Button(app, text="(", width = 5, height=2,command= lambda: clicar_botao("("))
botao_pare2 = Button(app, text=")", width = 5, height=2,command= lambda: clicar_botao(")"))
botao_pon = Button(app, text=".", width = 5, height=2,command= lambda: clicar_botao("."))

# Botões 3

botao_multi = Button(app, text="x", width = 5, height=2,command= lambda: clicar_botao("*"))
botao_div = Button(app, text="/", width = 5, height=2,command= lambda: clicar_botao("/"))
botao_mais = Button(app, text="+", width = 5, height=2,command= lambda: clicar_botao("+"))
botao_menos = Button(app, text="-", width = 5, height=2,command= lambda: clicar_botao("-"))
botao_igual = Button(app, text="=", width = 5, height=2,command= lambda: Motor_da_calculadora())

#Posicionamento
botao_apagar.grid(row =1 , column =0 , padx = 5, pady = 5)
botao_pare.grid(row =1 , column =1 , padx = 5, pady = 5)
botao_pare2.grid(row =1 , column =2 , padx = 5, pady = 5)
botao_div.grid(row =1 , column =3 , padx = 5, pady = 5)

botao7.grid(row =2 , column =0 , padx = 5, pady = 5)
botao8.grid(row =2 , column =1 , padx = 5, pady = 5)
botao9.grid(row =2 , column =2 , padx = 5, pady = 5)
botao_multi.grid(row =2 , column =3 , padx = 5, pady = 5)

botao4.grid(row =3 , column =0 , padx = 5, pady = 5)
botao5.grid(row =3 , column =1 , padx = 5, pady = 5)
botao6.grid(row =3 , column =2 , padx = 5, pady = 5)
botao_mais.grid(row =3 , column =3 , padx = 5, pady = 5)

botao1.grid(row =4 , column =0 , padx = 5, pady = 5)
botao2.grid(row =4 , column =1 , padx = 5, pady = 5)
botao3.grid(row =4 , column =2 , padx = 5, pady = 5)
botao_menos.grid(row =4 , column =3 , padx = 5, pady = 5)

botao0.grid(row =5 , column =0, columnspan=2 , padx = 5, pady = 5)
botao_pon.grid(row =5 , column =2 , padx = 5, pady = 5)
botao_igual.grid(row =5 , column =3 , padx = 5, pady = 5)


app.mainloop()