import tkinter as tk
from tkinter import ttk

# Lista para armazenar os resultados
resultados = []


def mostrar_informacoes():
    nome = entry_nome.get()
    range_valor = entry_range.get()
    gateway = entry_gateway.get()
    oam = entry_oam.get()
    vlan = entry_vlan.get()

    # Verificar se o range termina com /30
    if range_valor.endswith("/30"):
        # Pegar o número antes da barra e acrescentar 1 para o Gateway
        base_ip = range_valor.split("/")[0]
        partes_ip = base_ip.split(".")
        partes_ip[-1] = str(int(partes_ip[-1]) + 1)
        novo_gateway_ip = ".".join(partes_ip)

        # Preencher o campo Gateway com o novo IP
        entry_gateway.delete(0, tk.END)
        entry_gateway.insert(0, novo_gateway_ip)

        # Pegar o número antes da barra e acrescentar 2 para o OAM
        partes_ip[-1] = str(int(partes_ip[-1]) + 1)
        novo_oam_ip = ".".join(partes_ip)

        # Preencher o campo OAM com o novo IP
        entry_oam.delete(0, tk.END)
        entry_oam.insert(0, novo_oam_ip)

        # Atualizar as variáveis gateway e oam com os novos valores
        gateway = novo_gateway_ip
        oam = novo_oam_ip

    info = f"Name: {nome}\nRange: {range_valor}\nGateway: {gateway}\nOAM: {oam}\nVLAN: {vlan}"
    resultados.append(info)
    atualizar_resultados()
    limpar_inputs()
    copiar_todos_dados()


def limpar_inputs():
    for entry in [entry_nome, entry_range, entry_gateway, entry_oam, entry_vlan]:
        entry.delete(0, tk.END)


def limpar_resultados():
    resultados.clear()
    atualizar_resultados()


def copiar_todos_dados():
    todos_dados = "\n\n".join(resultados)
    janela.clipboard_clear()
    janela.clipboard_append(todos_dados)


def atualizar_resultados():
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    for i, resultado in enumerate(resultados):
        frame = tk.Frame(frame_resultados, bg="white", relief="solid", padx=10, pady=5)
        frame.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky="ew")

        label = tk.Label(frame, text=resultado, anchor="w", justify="left", bg="white")
        label.pack(side="left", fill="both", expand=True)

        botao_apagar = tk.Button(frame, text="Delete", command=lambda i=i: apagar_resultado(i), bg="#EE3023",
                                 fg="white")
        botao_apagar.pack(side="right")

    janela.update_idletasks()
    janela.geometry(f"{janela.winfo_width()}x{janela.winfo_height() + 20}")


def apagar_resultado(index):
    del resultados[index]
    atualizar_resultados()


def reload_app():
    janela.destroy()
    main()


def main():
    global janela
    global entry_nome, entry_range, entry_gateway, entry_oam, entry_vlan
    global frame_resultados

    # Criação da janela principal
    janela = tk.Tk()
    janela.title("Network Device Logger")
    janela.geometry("600x580")

    # Estilo
    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TButton", font=("Helvetica", 12), background="Black", foreground="BLACK")
    style.map("TButton", background=[("active", "red")])

    # Criação dos campos de entrada
    frame_entrada = ttk.Frame(janela, padding="10", relief="solid")
    frame_entrada.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    ttk.Label(frame_entrada, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry_nome = ttk.Entry(frame_entrada)
    entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(frame_entrada, text="Range:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry_range = ttk.Entry(frame_entrada)
    entry_range.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(frame_entrada, text="Gateway:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry_gateway = ttk.Entry(frame_entrada)
    entry_gateway.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(frame_entrada, text="OAM:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry_oam = ttk.Entry(frame_entrada)
    entry_oam.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    ttk.Label(frame_entrada, text="VLAN:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry_vlan = ttk.Entry(frame_entrada)
    entry_vlan.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    # Botões para mostrar e limpar as informações
    frame_botoes = ttk.Frame(janela, padding="10")
    frame_botoes.grid(row=1, column=0, pady=10, sticky="ew")

    botao_mostrar = ttk.Button(frame_botoes, text="Get Information", command=mostrar_informacoes)
    botao_mostrar.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    botao_limpar = ttk.Button(frame_botoes, text="Clear Results", command=limpar_resultados)
    botao_limpar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Botão para recarregar a aplicação
    botao_reload = ttk.Button(frame_botoes, text="Reload App", command=reload_app)
    botao_reload.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    # Campo para mostrar o resultado
    frame_resultados = ttk.Frame(janela, padding="10", relief="solid")
    frame_resultados.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # Tornar a interface responsiva
    janela.grid_columnconfigure(0, weight=1)
    frame_entrada.grid_columnconfigure(1, weight=1)
    frame_resultados.grid_columnconfigure(0, weight=1)
    frame_resultados.grid_columnconfigure(1, weight=1)

    # Iniciar o loop principal da interface
    janela.mainloop()


# Chamar a função principal
main()
