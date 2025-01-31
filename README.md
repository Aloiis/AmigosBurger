# AmigosBurger - Sistema de Gerenciamento de Pedidos

Este projeto foi desenvolvido para automatizar a criação de documentos de pedidos para uma hamburgueria. Ele utiliza um modelo pré-definido em `.docx` para gerar notas fiscais personalizadas e imprimi-las automaticamente. O sistema também inclui uma interface gráfica simples para facilitar a inserção dos dados do pedido.

## 📖 Índice

1. [Funcionalidades](#-funcionalidades)
2. [Como Usar](#-como-usar)
   - [Preparação](#-Preparação)
   - [Execução](#-Execução)
   - [Inserção de Dados](#-inserção-de-dados)
   - [Geração do Documento](#-geração-do-documento)
   - [Visualização do Valor Total](#-visualização-do-valor-total)
3. [Requisitos](#-requisitos)
4. [Estrutura do Código](#-estrutura-do-código)
5. [Personalização](#-personalização)
6. [Exemplo de Uso](#-exemplo-de-uso)
7. [Contribuição](#-contribuição)
8. [Licença](#-licença)
   
## 📌 Funcionalidades

- **📄 Preenchimento Automático de Documentos**: O sistema preenche automaticamente um modelo de documento `.docx` com as informações do pedido, como cliente, itens pedidos, valor total e observações.
- **📂 Geração de Nomes de Arquivos Únicos**: Cada pedido gera um arquivo único com um nome baseado no número do pedido, nome do cliente e data/hora.
- **🖨️ Impressão Automática**: Após a geração do documento, ele é enviado automaticamente para a impressora configurada.
- **🖥️ Interface Gráfica Amigável**: Uma interface simples e intuitiva permite a inserção de dados do cliente, seleção de itens do cardápio e visualização do valor total do pedido.
- **🔢 Contador de Pedidos**: O sistema mantém um contador de pedidos, garantindo que cada pedido tenha um número único.

## 🚀 Como Usar

### 🛠️ Preparação

1. Certifique-se de ter um modelo de documento `.docx` nomeado `Amigos_Burger_Nota.docx` no mesmo diretório do script.
2. Este modelo deve conter os seguintes campos de substituição:

   ```
   {Data} → Data e hora do pedido.
   {Cliente} → Nome do cliente.
   {Pedido} → Itens do pedido.
   {Valor} → Valor total do pedido.
   {Observacoes} → Observações adicionais.
   ```

### ▶️ Execução

1. Execute o script `AmigosBurger.py`.
2. Uma janela da interface gráfica será aberta, permitindo que você insira os dados do cliente, selecione os itens do cardápio e adicione observações.

### ✏️ Inserção de Dados

- **Cliente**: Insira o nome do cliente.
- **Observações**: Adicione quaisquer observações relevantes.
- **Itens do Pedido**: Selecione a quantidade de cada item do cardápio usando os `Spinbox`.

### 📑 Geração do Documento

1. Clique no botão **"Gerar Documento"** para criar o arquivo `.docx` com as informações do pedido.
2. O documento será salvo com um nome único e enviado automaticamente para a impressora.

### 💰 Visualização do Valor Total

- O valor total do pedido é atualizado automaticamente conforme os itens são selecionados e pode ser visualizado na interface.

## 🔧 Requisitos

- **Python 3.x**
- Bibliotecas necessárias:
  - `tkinter` (já incluída na instalação padrão do Python)
  - `python-docx` (para manipulação de documentos `.docx`)

Para instalar as dependências, execute:

```bash
pip install python-docx
```

## 📂 Estrutura do Código

- `preencher_documento(dados)`: Função que preenche o modelo de documento com os dados do pedido e salva o arquivo.
- `gerar_documento()`: Função que coleta os dados da interface e chama `preencher_documento`.
- `obter_numero_pedido()`: Função que mantém um contador de pedidos e retorna o próximo número disponível.
- `atualizar_valor_total()`: Função que atualiza o valor total do pedido na interface.
- **Interface Gráfica**: Criada usando `tkinter`, com campos para inserção de dados, seleção de itens e botão para gerar o documento.

## 🎨 Personalização

- **Cardápio**: Os itens do cardápio e seus preços podem ser personalizados no dicionário `preco_item`.
- **Modelo de Documento**: O modelo `.docx` pode ser modificado para incluir mais campos ou alterar a formatação, desde que os campos de substituição sejam mantidos.

## 📌 Exemplo de Uso

1. Abra o script `AmigosBurger.py`.
2. Insira o nome do cliente e as observações.
3. Selecione a quantidade de cada item do cardápio.
4. Clique em **"Gerar Documento"**.
5. O documento será criado e enviado para impressão.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorar o projeto.

## 📜 Licença

Este projeto está licenciado sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

---

🔧 *Desenvolvido para otimizar o gerenciamento de pedidos da AmigosBurger!* 🍔🔥
