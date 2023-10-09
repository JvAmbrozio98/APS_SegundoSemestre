from tkinter import *

def numerosCra(pa, al):
    
    for i in range(len(pa)):
        for j in range(len(al)):
            if pa[i] == al[j]:
                pa[i] = j
    return pa

def vigenere():

    global alfabeto

    crip= cript.get()

    palavra= list(caixa_palavra.get())
    palavraNU= numerosCra(palavra, alfabeto)

    chave = list(caixa_chave.get())
    chaveNU= numerosCra(chave, alfabeto)

    mensagen = ''
    mensagenNU=[]

    while (len(palavraNU) > len(chave)):
        for i in range(len(chaveNU)):
            chaveNU.append(chaveNU[i])
            if len(palavraNU) == len(chave):
                break

    if crip == 1:
        for j in range(len(palavraNU)):
            
            mensagenNU.append(palavraNU[j]+chaveNU[j])
            if (mensagenNU[j]>25):
                mensagenNU[j] = mensagenNU[j]-26
    else:
        for j in range(len(palavraNU)):
            
            mensagenNU.append(palavraNU[j]-chaveNU[j]+26)
            if (mensagenNU[j]>25):
                mensagenNU[j] = mensagenNU[j]-26

    for k in range(len(mensagenNU)):
        mensagen = mensagen + (alfabeto[mensagenNU[k]])
    
    resultado["text"] = "Resultado: " + mensagen.upper()

def cesar():
    global alfabeto
    crip= cript.get()
    palavra= list(caixa_palavra.get())
    palavraNU= numerosCra(palavra, alfabeto)
    chave = int(caixa_chave.get())
    mensagen = ''
    mensagenNU=[]
    print (crip)

    if crip == 1:
        for j in range(len(palavraNU)):
            mensagenNU.append(palavraNU[j]+chave)
            if (mensagenNU[j]>25):
                    mensagenNU[j] = mensagenNU[j]-26
    else:
        for j in range(len(palavraNU)):
            mensagenNU.append(palavraNU[j]-chave)
            if (mensagenNU[j]<0):
                mensagenNU[j] = mensagenNU[j]+26

    for k in range(len(mensagenNU)):
        mensagen = mensagen + (alfabeto[mensagenNU[k]])    
    
    resultado["text"] = "Resultado: " + mensagen.upper()


alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

janela = Tk()

cript = IntVar()

janela.title("APS")

texto = Label(janela, text = "aaaaaaaaaaa", font="Arial 25")
texto.grid(columnspan=3,row=0, padx=10, pady=0)

texto = Label(janela, text = "partisipantes: Carlos, Giovane, João, Ottávio, Sárley", font="Arial 10")
texto.grid(column=1, columnspan=2,row=1, padx=5, pady=0)

resultado = Label(janela, text = "", font="Arial 20")
resultado.grid(columnspan=3, row=2, padx=10, pady=10)

text_palavra = Label(janela, text = "Palavra:", font="Arial 20")
text_palavra.grid(column=0, row=3, padx=10, pady=10)
caixa_palavra = Entry(janela, background="gray", font="Arial 20")
caixa_palavra.grid(column=1, columnspan=2, row=3, padx=10, pady=10)

text_chave = Label(janela, text = "Chave:", font="Arial 20")
text_chave.grid(column=0, row=4, padx=10, pady=10)
caixa_chave = Entry(janela, background="gray", font="Arial 20")
caixa_chave.grid(column=1, columnspan=2, row=4, padx=10, pady=10)

Radiocript1 = Radiobutton(janela, text="Cripitografar", variable = cript, value=1, font="Arial 15")
Radiocript1.grid(column=0, row=5, padx=10, pady=10)
Radiocript2 = Radiobutton(janela, text="Descripitografar", variable = cript, value=2, font="Arial 15")
Radiocript2.grid(column=2, row=5, padx=10, pady=10)

botaoCésar = Button(janela, text="César",font="Arial 15", command=cesar)
botaoCésar.grid(column=0, row=6, padx=10, pady=20)

botaoVigenere = Button(janela, text="Vigener", font="Arial 15", command=vigenere)
botaoVigenere.grid(column=1, row=6, padx=10, pady=20)

botaoRC4 = Button(janela, text="RC4", font="Arial 15")
botaoRC4.grid(column=2, row=6, padx=10, pady=20)


janela.mainloop()
