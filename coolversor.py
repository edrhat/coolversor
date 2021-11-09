import os
from tkinter import *
from tkinter import messagebox


messagebox.showinfo("Verificando youtubue-dl", "Preparando-se para iniciar CoolVersor.\n\nO arquivo será salvo na mesma pasta do programa.")
os.system("pip install youtube-dl")

janela = Tk()
cab = PhotoImage(file="cab.png")
img = Label(janela, image=cab)
img.cab = cab
img.config(bg="#696969")
img.place(x=50,y=10)

rodape = PhotoImage(file="rodape.png")
img2 = Label(janela, image=rodape)
img2.rodape = rodape
img2.config(bg="#696969")
img2.place(x=0,y=235)


linkE = Entry(janela)
linkE["font"] = ("Arial", 17)
linkE.config(foreground="#A52A2A")
linkE.place(x=50, y=100, width=300)

def baixar(event):

    lnk = linkE.get()

    if (lnk)=="" or (lnk)==" ":
        messagebox.showwarning("Campo vazio", "Insira o link do vídeo a ser convertido.")
            
    os.system("youtube-dl --extract-audio --audio-format mp3 {}".format(lnk))
        

def baixarmp4(event):

    lnk = linkE.get()

    os.system("youtube-dl {}".format(lnk))
        

def limpar(event):

    linkE.delete(0, "end")

bt = Button(janela, text="Baixar MP3")
bt["font"] = ("Lucida Console", "13")
bt.config(bg="red", foreground="white")
bt.place(x=200, y=142, width=120)
bt.bind("<Button-1>", baixar)


bt2 = Button(janela, text="Limpar")
bt2["font"] = ("Lucida Console", "13")
bt2.config(bg="black", foreground="red")
bt2.place(x=80, y=142, width=80)
bt2.bind("<Button-1>", limpar)

bt3 = Button(janela, text="Baixar MP4")
bt3["font"] = ("Lucida Console", "13")
bt3.config(bg="darkgreen", foreground="white")
bt3.place(x=200, y=185, width=120)
bt3.bind("<Button-1>", baixarmp4)











janela.config(bg="#696969")
janela.geometry("400x280")
janela.title("Conversor de vídeos do Youtube")
janela.resizable(width=False, height=False)
janela.mainloop()
