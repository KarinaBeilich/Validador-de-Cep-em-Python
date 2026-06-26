import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage

from validadorcep import buscar_por_cep, buscar_por_endereco


def format_endereco(dados):
    return (
        f"CEP:     {dados.get('cep', '-') }\n"
        f"Rua:     {dados.get('logradouro', '-') or '-'}\n"
        f"Bairro:  {dados.get('bairro', '-') or '-'}\n"
        f"Cidade:  {dados.get('localidade', '-') or '-'}\n"
        f"Estado:  {dados.get('uf', '-') or '-'}\n"
    )


def cep_valido(cep):
    cep_limpo = cep.replace("-", "").strip()
    return len(cep_limpo) == 8 and cep_limpo.isdigit()


def cep_termina_em_000(cep):
    cep_limpo = cep.replace("-", "").strip()
    return cep_limpo.endswith("000") and len(cep_limpo) == 8


def mostrar_resultado(texto, status="ok"):
    result_text.configure(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, texto)
    result_text.configure(state="disabled")
    if status == "error":
        result_label.configure(text=texto, foreground="red")
    else:
        result_label.configure(text="", foreground="black")


def buscar_cep_interface():
    cep = cep_entry.get().strip()
    if not cep_valido(cep):
        mostrar_resultado("CEP inválido. Digite 8 números.", status="error")
        address_frame.grid_remove()
        return

    cep_limpo = cep.replace("-", "")
    dados = buscar_por_cep(cep_limpo)

    if dados:
        mostrar_resultado(format_endereco(dados))
        address_frame.grid_remove()
        return

    if cep_termina_em_000(cep_limpo):
        mostrar_resultado(
            "CEP não encontrado no ViaCEP. Preencha o endereço abaixo para buscar o CEP correspondente.",
            status="error",
        )
        address_frame.grid()
    else:
        mostrar_resultado("CEP não encontrado ou inválido.", status="error")
        address_frame.grid_remove()


def buscar_endereco_interface():
    uf = uf_entry.get().strip().upper()
    cidade = cidade_entry.get().strip()
    logradouro = logradouro_entry.get().strip()

    if not uf or not cidade or not logradouro:
        messagebox.showwarning("Atenção", "Preencha UF, cidade e logradouro para a busca por endereço.")
        return

    resultados = buscar_por_endereco(uf, cidade, logradouro)
    if not resultados:
        mostrar_resultado("Endereço não encontrado. Verifique os dados e tente novamente.", status="error")
        return

    if len(resultados) == 1:
        mostrar_resultado(format_endereco(resultados[0]))
    else:
        lista = [
            f"[{i}] CEP: {item.get('cep', '-') }\n"
            f"     {item.get('logradouro', '-') or '-'}, {item.get('bairro', '-') or '-'}, {item.get('localidade', '-') or '-'} / {item.get('uf', '-') or '-'}\n"
            for i, item in enumerate(resultados, 1)
        ]
        mostrar_resultado("Resultados encontrados:\n\n" + "\n".join(lista))


def criar_interface():
    global cep_entry, uf_entry, cidade_entry, logradouro_entry, result_text, result_label, address_frame

    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("640x460")
    root.configure(bg="#F3F3F3")

    title_bar = tk.Frame(root, bg="#D9D9D6", height=32)
    title_bar.pack(fill="x")

    icon_image = PhotoImage(file="assets/redstone_capital.png")
    icon_label = tk.Label(title_bar, image=icon_image, bg="#D9D9D6")
    icon_label.image = icon_image
    icon_label.pack(side="left", padx=(4, 2), pady=2)

    title_label = tk.Label(
        title_bar,
        text="Redstone Capital - Validador de CEP",
        bg="#D9D9D6",
        fg="Black",
        font=(None, 8, "bold")
    )
    title_label.pack(side="left", padx=4)

    def fechar():
        root.destroy()

    close_button = tk.Button(
        title_bar,
        text="✕",
        bg="#ff0000",
        fg="white",
        bd=0,
        padx=8,
        pady=2,
        command=fechar
    )
    close_button.pack(side="right", padx=4, pady=4)

    root.update_idletasks()
    largura = 640
    altura = 460
    x = (root.winfo_screenwidth() - largura) // 2
    y = (root.winfo_screenheight() - altura) // 2
    root.geometry(f"{largura}x{altura}+{x}+{y}")

    # ------------------------------------

    main_frame = ttk.Frame(root, padding=16)
    main_frame.pack(fill="both", expand=True)


    title = ttk.Label(main_frame, text="Validador de CEP", font=(None, 16, "bold"))
    title.grid(row=0, column=0, columnspan=3, pady=(0, 14), sticky="w")


    ttk.Label(main_frame, text="Digite o CEP:").grid(row=1, column=0, sticky="w")
    cep_entry = ttk.Entry(main_frame, width=20)
    cep_entry.grid(row=1, column=1, sticky="w")
    cep_entry.focus()

    buscar_button = ttk.Button(main_frame, text="Buscar CEP", command=buscar_cep_interface)
    buscar_button.grid(row=1, column=2, padx=(10, 0), sticky="w")

    result_label = ttk.Label(main_frame, text="", foreground="red")
    result_label.grid(row=2, column=0, columnspan=3, pady=(10, 0), sticky="w")

    result_text = tk.Text(main_frame, width=72, height=10, wrap="word", state="disabled", background="#f4f4f4")
    result_text.grid(row=3, column=0, columnspan=3, pady=(6, 12), sticky="w")

    address_frame = ttk.LabelFrame(main_frame, text="Busca por endereço (CEP geral)")
    address_frame.grid(row=4, column=0, columnspan=3, pady=(0, 10), sticky="ew")
    address_frame.grid_remove()

    ttk.Label(address_frame, text="UF:").grid(row=0, column=0, sticky="w", padx=(8, 4), pady=4)
    uf_entry = ttk.Entry(address_frame, width=8)
    uf_entry.grid(row=0, column=1, sticky="w", pady=4)

    ttk.Label(address_frame, text="Cidade:").grid(row=0, column=2, sticky="w", padx=(16, 4), pady=4)
    cidade_entry = ttk.Entry(address_frame, width=24)
    cidade_entry.grid(row=0, column=3, sticky="w", pady=4)

    ttk.Label(address_frame, text="Logradouro:").grid(row=1, column=0, sticky="w", padx=(8, 4), pady=4)
    logradouro_entry = ttk.Entry(address_frame, width=40)
    logradouro_entry.grid(row=1, column=1, columnspan=3, sticky="w", pady=4)

    endereco_button = ttk.Button(address_frame, text="Buscar por Endereço", command=buscar_endereco_interface)
    endereco_button.grid(row=2, column=0, columnspan=4, pady=(8, 10))

    info_label = ttk.Label(main_frame, text="Se o CEP terminar em 000 e não for encontrado, use a busca por endereço.")
    info_label.grid(row=5, column=0, columnspan=3, sticky="w")

    root.mainloop()


if __name__ == "__main__":
    criar_interface()
