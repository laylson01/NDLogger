import tkinter as tk
from tkinter import ttk
# Lista para armazenar os resultados
resultados = []


########FUNCTIONS########
def mostrar_informacoes():
    nome = entry_nome.get()
    range_valor = entry_range.get()  # Campo RANGE
    gateway = entry_gateway.get()
    oam = entry_oam.get()
    vlan = entry_vlan.get()


    info = f"Nome: {nome}\nRange: {range_valor}\nGateway: {gateway}\nOAM: {oam}\nVLAN: {vlan}"
    resultados.append(info)
    atualizar_resultados()
    limpar_inputs()  # Limpa apenas os campos de entrada
    copiar_todos_dados()  # Copia todos os dados para a área de transferência


def limpar_inputs():
    entry_nome.delete(0, tk.END)
    entry_range.delete(0, tk.END)  # Limpa o campo RANGE
    entry_gateway.delete(0, tk.END)
    entry_oam.delete(0, tk.END)
    entry_vlan.delete(0, tk.END)


def limpar_resultados():
    resultados.clear()  # Limpa a lista de resultados
    atualizar_resultados()  # Atualiza a interface


def copiar_todos_dados():
    # Cria uma string com todos os resultados
    todos_dados = "\n\n".join(resultados)
    janela.clipboard_clear()  # Limpa a área de transferência
    janela.clipboard_append(todos_dados)  # Adiciona todos os dados à área de transferência


def atualizar_resultados():
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    for i, resultado in enumerate(resultados):
        label = tk.Label(frame_resultados, text=resultado, anchor="w", justify="left", bg="white", relief="solid",
                         padx=10, pady=5)
        label.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="ew")

    janela.update_idletasks()
    janela.geometry(f"{janela.winfo_width()}x{janela.winfo_height() + 20}")

########FUNCTIONS########

# Criação da janela principal
janela = tk.Tk()
janela.title("NDLogger")
janela.geometry("500x400")

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))

# Criação dos campos de entrada
frame_entrada = ttk.Frame(janela, padding="10")
frame_entrada.grid(row=0, column=0, sticky="ew")

ttk.Label(frame_entrada, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = ttk.Entry(frame_entrada)
entry_nome.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(frame_entrada, text="Range:").grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Campo RANGE
entry_range = ttk.Entry(frame_entrada)
entry_range.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(frame_entrada, text="Gateway:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_gateway = ttk.Entry(frame_entrada)
entry_gateway.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(frame_entrada, text="OAM:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_oam = ttk.Entry(frame_entrada)
entry_oam.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

ttk.Label(frame_entrada, text="VLAN:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_vlan = ttk.Entry(frame_entrada)
entry_vlan.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

##Criar mais um campo para WO


# Botões para mostrar e limpar as informações
frame_botoes = ttk.Frame(janela, padding="10")
frame_botoes.grid(row=1, column=0, sticky="ew")

botao_mostrar = ttk.Button(frame_botoes, text="Get Information", command=mostrar_informacoes)
botao_mostrar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

botao_limpar = ttk.Button(frame_botoes, text="Clear Results", command=limpar_resultados)
botao_limpar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Campo para mostrar o resultado
frame_resultados = ttk.Frame(janela, padding="10")
frame_resultados.grid(row=2, column=0, sticky="nsew")

# Tornar a interface responsiva
janela.grid_columnconfigure(0, weight=1)
frame_entrada.grid_columnconfigure(1, weight=1)
frame_resultados.grid_columnconfigure(0, weight=1)
frame_resultados.grid_columnconfigure(1, weight=1)

# Iniciar o loop principal da interface
janela.mainloop()