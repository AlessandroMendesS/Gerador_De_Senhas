import customtkinter as ct
import secrets
import string
import pyperclip 

def gerar_senha():
    caixa_senha.delete('1.0', 'end') 
    qtd_caracteres = menu.get()
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for i in range(int(qtd_caracteres)))
    caixa_senha.insert("1.0", senha) 

def copiar_senha():
    senha = caixa_senha.get("1.0", "end-1c") 
    pyperclip.copy(senha)  

ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")
janela = ct.CTk()
janela.title("Gerador de senhas")
janela.resizable(False, False)
janela.geometry("315x400")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

tabview = ct.CTkTabview(janela, width=305, height=360)
tabview.grid()
tabview.add("Gerador de senhas")
tabview.tab("Gerador de senhas").grid_columnconfigure(0, weight=1)

valores = [str(i) for i in range(1, 26)] 

entrada1 = ct.CTkLabel(tabview.tab("Gerador de senhas"), text="Defina a quantidade de caracteres:")
entrada1.grid(row=0, column=0, padx=10, pady=10)

menu = ct.CTkOptionMenu(tabview.tab("Gerador de senhas"), values=valores)
menu.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

botaogerador = ct.CTkButton(tabview.tab("Gerador de senhas"), text="Gerar senha", command=gerar_senha)
botaogerador.grid(row=2, column=0, padx=10, pady=10)

entrada_senhaGerada = ct.CTkLabel(tabview.tab("Gerador de senhas"), text="Sua senha:")
entrada_senhaGerada.grid(row=3, column=0, padx=10, pady=10)

caixa_senha = ct.CTkTextbox(tabview.tab("Gerador de senhas"), width=250, height=100)
caixa_senha.grid(row=4, column=0, padx=10, pady=10, sticky='nsew')

botaocopiar = ct.CTkButton(tabview.tab("Gerador de senhas"), text="Copiar", command=copiar_senha)
botaocopiar.grid(row=5, column=0, padx=10, pady=10)

janela.mainloop()
