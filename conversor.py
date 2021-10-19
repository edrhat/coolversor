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
        self.bt.place(x=260, y=48, width=120)
        self.bt.bind("<Button-1>", self.baixar)

        #.bt3 = tk.Button(janela, text="Baixar MP4")
        #self.bt3["font"] = ("Lucida Console", "13")
        #self.bt3.config(bg="green", foreground="white")
        #self.bt3.place(x=400, y=48, width=120)
        #self.bt3.bind("<Button-1>", self.baixar2)

        self.bt2 = tk.Button(janela, text="Limpar")
        self.bt2["font"] = ("Lucida Console", "13")
        self.bt2.config(bg="black", foreground="red")
        self.bt2.place(x=170, y=48, width=80)
        self.bt2.bind("<Button-1>", self.limpar)





    def baixar(self, event):

        lnk = self.linkE.get()

        lk = ("youtube-dl --extract-audio --audio-format mp3 ")+(lnk)
        os.system(lk)

   # def baixar2(self, event):

      #  lnk = self.linkE.get()

      #  lk = ("youtube-dl  --excract-audio --audio-format mp4 ") + (lnk)
      #  os.system(lk)

    def limpar(self, event):

        self.linkE.delete(0, "end")



janela = tk.Tk()

Tela(janela)
janela.config(bg="black")
janela.geometry("700x100")
janela.title("Conversor de vídeos do Youtube")
janela.resizable(width=False, height=False)
janela.mainloop()
