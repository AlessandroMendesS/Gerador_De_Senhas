# Gerador de Senhas

Este projeto é uma aplicação GUI (Interface Gráfica de Usuário) que gera senhas seguras e permite copiá-las para a área de transferência. Ele foi desenvolvido utilizando a biblioteca `customtkinter` para a interface, `secrets` para a geração de senhas seguras e `pyperclip` para copiar as senhas.

![image](https://github.com/user-attachments/assets/accb1390-1815-43ef-a957-222e953d7c45)


## Funcionalidades

- Geração de senhas aleatórias com letras, números e símbolos.
- Seleção da quantidade de caracteres da senha.
- Exibição da senha gerada em uma caixa de texto.
- Função para copiar a senha gerada para a área de transferência com apenas um clique.

## Tecnologias Utilizadas

- **Python 3.10+**
- **customtkinter**: Para criar uma interface gráfica moderna e customizável.
- **secrets**: Para gerar senhas seguras, com forte nível de aleatoriedade.
- **string**: Para fornecer os conjuntos de caracteres utilizados na geração da senha.
- **pyperclip**: Para copiar a senha diretamente para a área de transferência.

## Instalação

1. Clone este repositório em seu ambiente local:

    ```bash
    git clone https://github.com/seu-usuario/gerador-de-senhas.git
    ```

2. Instale as dependências necessárias. Execute o comando abaixo para instalar o `pyperclip` e `customtkinter`:

    ```bash
    pip install customtkinter pyperclip
    ```

3. Execute o arquivo Python:

    ```bash
    python gerador_de_senhas.py
    ```

## Como Usar

1. Ao iniciar a aplicação, você verá uma interface com um menu para selecionar a quantidade de caracteres da senha.
2. Escolha a quantidade de caracteres desejada (de 1 a 25).
3. Clique no botão **"Gerar senha"** para gerar uma senha aleatória.
4. A senha gerada aparecerá em uma caixa de texto abaixo.
5. Para copiar a senha gerada para a área de transferência, clique no botão **"Copiar"**.

## Exemplo de Interface

A interface consiste em uma aba de geração de senhas com uma opção para definir o número de caracteres, um botão para gerar a senha e outro para copiá-la.

---

## Estrutura do Código

- `gerar_senha()`: Função que gera uma senha aleatória com base na quantidade de caracteres selecionada.
- `copiar_senha()`: Função que copia a senha gerada para a área de transferência usando `pyperclip`.
- Interface construída com `customtkinter`, utilizando elementos como `CTkTabview`, `CTkLabel`, `CTkOptionMenu`, `CTkButton`, e `CTkTextbox` para uma aparência moderna.

## Requisitos

- Python 3.10 ou superior
- Pacotes:
  - `customtkinter`
  - `pyperclip`

## Contribuição

Fique à vontade para abrir issues ou enviar pull requests caso tenha ideias de melhorias ou novos recursos!

## Licença

Este projeto é licenciado sob a licença MIT - consulte o arquivo `LICENSE` para mais detalhes.
