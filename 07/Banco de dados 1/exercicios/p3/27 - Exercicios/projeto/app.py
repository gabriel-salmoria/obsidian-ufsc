import tkinter as tk
from tkinter import ttk, messagebox

from pessoa_dao import cadastrar_pessoa, listar_pessoas
from profissao_dao import listar_profissoes


# ==============================
# FUNÇÕES DA INTERFACE
# ==============================

def carregar_profissoes_na_tela():
    """
    Carrega as profissões do banco de dados
    e coloca no Combobox da interface.
    """

    global profissoes_dict

    profissoes = listar_profissoes()

    profissoes_dict = {}

    for profissao_id, nome in profissoes:
        profissoes_dict[nome] = profissao_id

    combo_profissao["values"] = list(profissoes_dict.keys())


def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    combo_profissao.set("")


def cadastrar():
    """
    Pega os dados da tela, valida e envia para o banco.
    """

    nome = entrada_nome.get().strip()
    idade = entrada_idade.get().strip()
    email = entrada_email.get().strip()
    profissao_nome = combo_profissao.get().strip()

    if nome == "":
        messagebox.showwarning("Atenção", "O campo nome é obrigatório.")
        return

    if profissao_nome == "":
        messagebox.showwarning("Atenção", "Selecione uma profissão.")
        return

    if idade == "":
        idade = None
    else:
        try:
            idade = int(idade)
        except ValueError:
            messagebox.showerror("Erro", "A idade deve ser um número.")
            return

    profissao_id = profissoes_dict[profissao_nome]

    try:
        cadastrar_pessoa(nome, idade, email, profissao_id)

        messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")

        limpar_campos()
        atualizar_tabela()

    except Exception as erro:
        messagebox.showerror("Erro", f"Erro ao cadastrar pessoa:\n{erro}")


def atualizar_tabela():
    """
    Busca as pessoas no banco e mostra na tabela da interface.
    """

    for item in tabela.get_children():
        tabela.delete(item)

    pessoas = listar_pessoas()

    for pessoa in pessoas:
        tabela.insert("", tk.END, values=pessoa)


# ==============================
# JANELA PRINCIPAL
# ==============================

janela = tk.Tk()
janela.title("Cadastro de Pessoas e Profissões")
janela.geometry("800x500")


# ==============================
# TÍTULO
# ==============================

titulo = tk.Label(
    janela,
    text="Cadastro de Pessoas e Profissões",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)


# ==============================
# FORMULÁRIO
# ==============================

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)


label_nome = tk.Label(frame_formulario, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entrada_nome = tk.Entry(frame_formulario, width=35)
entrada_nome.grid(row=0, column=1, padx=5, pady=5)


label_idade = tk.Label(frame_formulario, text="Idade:")
label_idade.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entrada_idade = tk.Entry(frame_formulario, width=35)
entrada_idade.grid(row=1, column=1, padx=5, pady=5)


label_email = tk.Label(frame_formulario, text="E-mail:")
label_email.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entrada_email = tk.Entry(frame_formulario, width=35)
entrada_email.grid(row=2, column=1, padx=5, pady=5)


label_profissao = tk.Label(frame_formulario, text="Profissão:")
label_profissao.grid(row=3, column=0, padx=5, pady=5, sticky="e")

combo_profissao = ttk.Combobox(frame_formulario, width=32, state="readonly")
combo_profissao.grid(row=3, column=1, padx=5, pady=5)


botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar Pessoa",
    width=20,
    command=cadastrar
)

botao_cadastrar.pack(pady=10)


# ==============================
# TABELA
# ==============================

colunas = ("ID", "Nome", "Idade", "E-mail", "Profissão")

tabela = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings"
)

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=140)

tabela.pack(pady=10, fill="both", expand=True)


# ==============================
# INICIALIZAÇÃO
# ==============================

profissoes_dict = {}

carregar_profissoes_na_tela()
atualizar_tabela()

janela.mainloop()