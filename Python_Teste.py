import os
import tkinter as tk
from tkinter import ttk
from docx import Document
from datetime import datetime

# Função para preencher o documento
def preencher_documento(dados):
    # Carregar o modelo de documento
    doc = Document('Amigos_Burger_Nota.docx')  # Substitua pelo caminho correto do seu modelo

    # Obter a data e hora atuais
    data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Substituir os campos no documento sem alterar a formatação
    for p in doc.paragraphs:
        if '{Data}' in p.text:
            for run in p.runs:
                if '{Data}' in run.text:
                    run.text = run.text.replace('{Data}', data_hora_atual)
        if '{Cliente}' in p.text:
            for run in p.runs:
                if '{Cliente}' in run.text:
                    run.text = run.text.replace('{Cliente}', dados['cliente'])
        if '{Pedido}' in p.text:
            for run in p.runs:
                if '{Pedido}' in run.text:
                    run.text = run.text.replace('{Pedido}', dados['pedido'])
        if '{Valor}' in p.text:
            for run in p.runs:
                if '{Valor}' in run.text:
                    run.text = run.text.replace('{Valor}', dados['valor_total'])
        if '{Observacoes}' in p.text:
            for run in p.runs:
                if '{Observacoes}' in run.text:
                    run.text = run.text.replace('{Observacoes}', dados['observacoes'])

    # Gerar um novo nome de arquivo com base no número do pedido
    novo_nome_arquivo = f"Pedido_{dados['numero_pedido']}_{dados['cliente']}_{data_hora_atual.replace('/', '-').replace(':', '-')}.docx"

    # Salvar o novo documento com o nome gerado
    doc.save(novo_nome_arquivo)  # Cria um novo arquivo sem sobrescrever o original

    print(f"Documento gerado: {novo_nome_arquivo}")

    # Enviar para impressão automaticamente
    os.startfile(novo_nome_arquivo, "print")


# Função que é chamada ao clicar no botão
def gerar_documento():
    # Dados coletados da interface
    cliente = entry_cliente.get()
    observacoes = entry_observacoes.get()
    pedido = []
    total_pedido = 0

    # Coletando itens, quantidades e preços
    for item, var in pedidos.items():
        quantidade = var.get()  # Obter a quantidade do Spinbox
        if quantidade > 0:  # Adicionar apenas se a quantidade for maior que 0
            valor_item = preco_item[item]  # Preço do item
            valor_total_item = valor_item * quantidade  # Cálculo do valor total do item
            pedido.append(f"{quantidade} x {item} - R${valor_total_item:.2f}")  # Adicionando ao pedido
            total_pedido += valor_total_item  # Atualizando o valor total do pedido
    
    # Modificar para separar cada item com uma nova linha
    pedido_str = '\n'.join(pedido)
    
    # Dados do pedido
    dados_pedido = {
        'numero_pedido': obter_numero_pedido(),
        'cliente': cliente,
        'pedido': pedido_str,  # Agora com quebras de linha
        'valor_total': f"R${total_pedido:.2f}",
        'observacoes': observacoes
    }

    # Chama a função para preencher o modelo
    preencher_documento(dados_pedido)

    # Atualizar o valor total na interface
    entry_valor.delete(0, tk.END)
    entry_valor.insert(0, f"R${total_pedido:.2f}")


# Função para obter e atualizar o número do pedido
def obter_numero_pedido():
    try:
        # Tenta ler o número atual do pedido do arquivo
        with open("pedido_counter.txt", "r") as file:
            numero_pedido = int(file.read())
    except FileNotFoundError:
        # Caso o arquivo não exista, começa do número 0
        numero_pedido = 0
    
    # Atualiza o número do pedido para o próximo valor
    with open("pedido_counter.txt", "w") as file:
        file.write(str(numero_pedido + 1))
    
    return numero_pedido


# Função para atualizar o valor total
def atualizar_valor_total():
    total_pedido = 0

    # Coletando itens, quantidades e preços
    for item, var in pedidos.items():
        quantidade = var.get()  # Obter a quantidade do Spinbox
        if quantidade > 0:  # Adicionar apenas se a quantidade for maior que 0
            valor_item = preco_item[item]  # Preço do item
            valor_total_item = valor_item * quantidade  # Cálculo do valor total do item
            total_pedido += valor_total_item  # Atualizando o valor total do pedido

    # Atualizar o valor total na interface
    entry_valor.delete(0, tk.END)
    entry_valor.insert(0, f"R${total_pedido:.2f}")


# Preço dos itens do cardápio (exemplo)
preco_item = {
    "Hambúrguer Clássico": 15.00,
    "Cheeseburger": 18.00,
    "Batata Frita": 8.00,
    "Refrigerante": 5.00,
    "Suco Natural": 7.00
}

# Criação da interface gráfica
root = tk.Tk()
root.title("Gerenciamento de Pedidos")

# Layout
label_cliente = tk.Label(root, text="Cliente:")
label_cliente.grid(row=0, column=0, padx=10, pady=5)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=0, column=1, padx=10, pady=5)

label_observacoes = tk.Label(root, text="Observações:")
label_observacoes.grid(row=1, column=0, padx=10, pady=5)
entry_observacoes = tk.Entry(root)
entry_observacoes.grid(row=1, column=1, padx=10, pady=5)

label_valor = tk.Label(root, text="Valor Total:")
label_valor.grid(row=2, column=0, padx=10, pady=5)
entry_valor = tk.Entry(root)
entry_valor.grid(row=2, column=1, padx=10, pady=5)

# Cardápio (lista de itens para o pedido)
itens_cardapio = [
    "Hambúrguer Clássico", 
    "Cheeseburger", 
    "Batata Frita", 
    "Refrigerante",
    "Suco Natural"
]

label_pedido = tk.Label(root, text="Pedido:")
label_pedido.grid(row=3, column=0, padx=10, pady=5)

# Dicionário para armazenar os itens e suas variáveis associadas
pedidos = {}

# Criação de Spinbox para cada item do cardápio
for idx, item in enumerate(itens_cardapio):
    var = tk.IntVar(value=0)  # Inicializa a quantidade como 0
    pedidos[item] = var
    
    # Spinbox para a quantidade de cada item (de 0 a 10)
    spinbox_quantidade = tk.Spinbox(root, from_=0, to=10, textvariable=var, command=atualizar_valor_total)
    spinbox_quantidade.grid(row=4 + idx, column=0, padx=10, pady=5)
    label_quantidade = tk.Label(root, text=f"{item}:")
    label_quantidade.grid(row=4 + idx, column=1, padx=10, pady=5)

# Botão para gerar o documento
botao_gerar = tk.Button(root, text="Gerar Documento", command=gerar_documento)
botao_gerar.grid(row=9, column=0, columnspan=4, pady=10)

# Iniciar a interface
root.mainloop()
