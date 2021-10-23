import os
import tkinter as tk
os.system("pip install youtube-dl")
class Tela:

    def __init__(self, master):

        cab = tk.PhotoImage(file="cab.png")
        self.img = tk.Label(janela, image=cab)
        self.img.cab = cab
        self.img.config(bg="#696969")
        self.img.place(x=50,y=10)

        rodape = tk.PhotoImage(file="rodape.png")
        self.img2 = tk.Label(janela, image=rodape)
        self.img2.rodape = rodape
        self.img2.config(bg="#696969")
        self.img2.place(x=0,y=200)


        self.linkE = tk.Entry(janela)
        self.linkE["font"] = ("Arial", 17)
        self.linkE.config(foreground="#A52A2A")
        self.linkE.place(x=50, y=100, width=300)

        self.bt = tk.Button(janela, text="Baixar MP3")
        self.bt["font"] = ("Lucida Console", "13")
        self.bt.config(bg="red", foreground="white")
        self.bt.place(x=200, y=142, width=120)
        self.bt.bind("<Button-1>", self.baixar)


        self.bt2 = tk.Button(janela, text="Limpar")
        self.bt2["font"] = ("Lucida Console", "13")
        self.bt2.config(bg="black", foreground="red")
        self.bt2.place(x=80, y=142, width=80)
        self.bt2.bind("<Button-1>", self.limpar)





    def baixar(self, event):

        lnk = self.linkE.get()

        os.system("youtube-dl --extract-audio --audio-format mp3 {}".format(lnk))
        

    def limpar(self, event):

        self.linkE.delete(0, "end")



janela = tk.Tk()

Tela(janela)
janela.config(bg="#696969")
janela.geometry("400x230")
janela.title("Conversor de vídeos do Youtube")
janela.resizable(width=False, height=False)
janela.mainloop()
