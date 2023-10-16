from tkinter import *
from tkinter import filedialog

def numerosCra(pa, al):
    
    for i in range(len(pa)):
        for j in range(len(al)):
            if pa[i] == al[j]:
                pa[i] = j
    return pa

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])
    if arquivo:
        with open(arquivo, 'r') as file:
            caixa_palavra.delete(0, END)
            caixa_palavra.insert(0, file.read())

# ------------------------------------------------------------------------------------------------------------------
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
    
    resultado.delete(0, END)
    resultado.insert(0, mensagen.upper())

# -----------------------------------------------------------------------------------------------------------
def cesar():
    global alfabeto
    crip= cript.get()
    palavra= list(caixa_palavra.get())
    palavraNU= numerosCra(palavra, alfabeto)
    chave = int(caixa_chave.get())
    mensagen = ''
    mensagenNU=[]

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
    
    resultado.delete(0, END)
    resultado.insert(0, mensagen.upper())

# ----------------------------------------------------------------------------------------------------
def rc4(chave, txt_secreto):
    S = list(range(256))
    j = 0
    codigo = []
 
    for i in range(256):
        j = (j + S[i] + chave[i % len(chave)]) % 256
        S[i], S[j] = S[j], S[i]
 
    i = j = 0
    for letra in txt_secreto:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        codigo.append(chr(ord(letra) ^ k))
    return ''.join(codigo)

def encriptar_mensagem():
    chave = caixa_chave.get().encode('utf-8')
    txt_secreto = caixa_palavra.get()
    textocifrado = rc4(chave, txt_secreto)
    resultado.delete(0, END)
    resultado.insert(0, textocifrado)
# ----------------------------------------------------------------------------------------------------------

alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

janela = Tk()

cript = IntVar()

janela.title("APS")

texto = Label(janela, text = "APS", font="Arial 25")
texto.grid(columnspan=3,row=0, padx=10, pady=0)

texto = Label(janela, text = "partisipantes: Carlos, Giovane, João, Ottávio, Sárley", font="Arial 10")
texto.grid(column=1, columnspan=2,row=1, padx=5, pady=0)

resultado = Entry(janela, background="white", text = "", font="Arial 20")
resultado.grid(columnspan=3, row=2, padx=10, pady=10)

botaopalavra = Button(janela, text="Palavra:", font="Arial 15", command=abrir_arquivo)
botaopalavra.grid(column=0, row=3, padx=10, pady=10)
caixa_palavra = Entry(janela, background="gray", font="Arial 20")
caixa_palavra.grid(column=1, columnspan=2, row=3, padx=10, pady=10)

botaochave = Label(janela, text = "Chave:", font="Arial 15")
botaochave.grid(column=0, row=4, padx=10, pady=10)
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

botaoRC4 = Button(janela, text="RC4", font="Arial 15", command=encriptar_mensagem)
botaoRC4.grid(column=2, row=6, padx=10, pady=20)


janela.mainloop()
