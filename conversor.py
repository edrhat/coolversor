import os
import tkinter as tk

class Tela:

    def __init__(self, master):

        self.link = tk.Label(janela, text="Link do vídeo:")
        self.link["font"] = ("Lucida Console", 14)
        self.link.config(foreground="white", bg="black")
        self.link.place(x=7, y=14)

        self.linkE = tk.Entry(janela)
        self.linkE["font"] = ("Arial", 17)
        self.linkE.config(foreground="#A52A2A")
        self.linkE.place(x=170, y=10, width=300)

        self.bt = tk.Button(janela, text="Baixar MP3")
        self.bt["font"] = ("Lucida Console", "13")
        self.bt.config(bg="red", foreground="white")
        self.bt.place(x=320, y=48, width=120)
        self.bt.bind("<Button-1>", self.baixar)

        self.bt2 = tk.Button(janela, text="Limpar")
        self.bt2["font"] = ("Lucida Console", "13")
        self.bt2.config(bg="black", foreground="red")
        self.bt2.place(x=210, y=48, width=80)
        self.bt2.bind("<Button-1>", self.baixar2)





    def baixar(self, event):

        lnk = self.linkE.get()

        lk = ("start youtube-dl --extract-audio --audio-format mp3 ")+(lnk)
        os.system(lk)

    def baixar2(self, event):

        self.linkE.delete(0, "end")



janela = tk.Tk()

Tela(janela)
janela.config(bg="black")
janela.geometry("500x100")
janela.resizable(width=False, height=False)
janela.mainloop()
