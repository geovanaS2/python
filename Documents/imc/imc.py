import tkinter as tk 


#root = ThemedTk(theme="equilux")
root = tk.Tk()
root.geometry("400x200")
root.resizable(width=False, height=False)

label=tk.Label(text="Altura")
label.pack()
entry = tk.Entry(root)
entry.pack(pady=10)

label=tk.Label(text="Peso")
label.pack()
entry1 = tk.Entry(root)
entry1.pack(pady=10)

def cal_imc():

    altura = float(entry.get())
    peso = float(entry1.get())
    
    imc= peso / (altura * altura)    
    
    if imc < 18.5:
        mensagem ="Abaixo do peso"
    elif imc < 24.9:
        mensagem="Peso normal"
    elif imc < 29.9:
        mensagem="Sobre peso"
    elif imc < 34.9:
        mensagem="Obesidade gral I"
    elif imc < 39.9:
        mensagem="Obesidade gral II"
    elif imc >= 40:
        mensagem="Obesidade III (Mórbida)"

    texto = f'''Imc : {imc:.2f}\n {mensagem}'''

    label1["text"]= texto

    entry.delete(0,tk.END)
    entry1.delete(0,tk.END)

    print("-------------------")
    print(f"Mensagem enviada !")
    print("-------------------")

button=tk.Button(root, text="calcular", command=cal_imc, padx=5)
button.pack()

label1=tk.Label(text=" ")
label1.pack()

root.mainloop()