import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
window = tk.Tk()
window.geometry("200x100")
window.title("Num")

# Criar um widget de rótulo
label = tk.Label(window, text="Número aleatório")
label.pack()

# func quando o botão é clicado
import random
def button_click_handler():

    num=random.randint(0,6)

    label["text"]= num

# Criar um widget de botão
button = tk.Button(window, text="Enviar", command=button_click_handler)
button.pack()

label=tk.Label(text="  ")
label.pack()

# Iniciar o loop de eventos principal
window.mainloop()
