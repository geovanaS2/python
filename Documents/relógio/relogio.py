import tkinter as tk
from datetime import datetime

fundo='#3d3d3d'
fonte='#1A9B49'

#janela
root=tk.Tk()
root.geometry("450x180")
root.resizable(width=False, height=False)
root.configure(bg=fundo)

def relogio():
    agora =datetime.now()
    hora=agora.strftime('%H:%M:%S')
    data=agora.strftime(f'%A')
    dia=agora.day
    mes=agora.strftime(f"%b")
    ano=agora.strftime(f"%y")

    l1.config(text=hora)
    l1.after(1000, relogio)
    l2.config(text=data + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1=tk.Label(root, text=" ", font=("Arial 80"), bg=fundo, fg=fonte) 
l1.grid(row=0 ,column=0, sticky=tk.NW, padx=20, pady=5)

l2=tk.Label(root, text=" ", font=("Arial 20"), bg=fundo, fg=fonte) 
l2.grid(row=1 ,column=0, sticky=tk.NW, padx=20, pady=5 )

relogio()
root.mainloop()