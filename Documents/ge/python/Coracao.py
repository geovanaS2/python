import tkinter as tk                                                            
from tkinter import messagebox

# Criar a janela principal
window = tk.Tk()
window.title("Coração")

# Criar um widget de rótulo
label = tk.Label(window, text="!!!")
label.pack()

# func quando o botão é clicado
def button_click_handler():
    mensagem= "--000---000--\n-0000000000-\n--00000000--\n---000000---\n----0000----"
    messagebox.showinfo("<3",mensagem)

# Criar um widget de botão
button = tk.Button(window, text="Clique em mim", command=button_click_handler)
button.pack()

# Iniciar o loop de eventos principal
window.mainloop()