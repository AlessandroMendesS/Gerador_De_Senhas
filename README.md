Gerador de Senhas
Este projeto é uma aplicação GUI (Interface Gráfica de Usuário) que gera senhas seguras e permite copiá-las para a área de transferência. Ele foi desenvolvido utilizando a biblioteca customtkinter para a interface, secrets para a geração de senhas seguras e pyperclip para copiar as senhas.

![image](https://github.com/user-attachments/assets/8481f0fb-8aea-4e17-888a-0b5052ed10a2)


Funcionalidades
Geração de senhas aleatórias com letras, números e símbolos.
Seleção da quantidade de caracteres da senha.
Exibição da senha gerada em uma caixa de texto.
Função para copiar a senha gerada para a área de transferência com apenas um clique.
Tecnologias Utilizadas
Python 3.10+
customtkinter: Para criar uma interface gráfica moderna e customizável.
secrets: Para gerar senhas seguras, com forte nível de aleatoriedade.
string: Para fornecer os conjuntos de caracteres utilizados na geração da senha.
pyperclip: Para copiar a senha diretamente para a área de transferência.
Instalação
Clone este repositório em seu ambiente local:
bash
Copiar código
git clone https://github.com/seu-usuario/gerador-de-senhas.git
Instale as dependências necessárias. Execute o comando abaixo para instalar o pyperclip e customtkinter:
bash
Copiar código
pip install customtkinter pyperclip
Execute o arquivo Python:
bash
Copiar código
python gerador_de_senhas.py
Como Usar
Ao iniciar a aplicação, você verá uma interface com um menu para selecionar a quantidade de caracteres da senha.
Escolha a quantidade de caracteres desejada (de 1 a 25).
Clique no botão "Gerar senha" para gerar uma senha aleatória.
A senha gerada aparecerá em uma caixa de texto abaixo.
Para copiar a senha gerada para a área de transferência, clique no botão "Copiar".
Exemplo de Interface
A interface consiste em uma aba de geração de senhas com uma opção para definir o número de caracteres, um botão para gerar a senha e outro para copiá-la.

Estrutura do Código
gerar_senha(): Função que gera uma senha aleatória com base na quantidade de caracteres selecionada.
copiar_senha(): Função que copia a senha gerada para a área de transferência usando pyperclip.
Interface construída com customtkinter, utilizando elementos como CTkTabview, CTkLabel, CTkOptionMenu, CTkButton, e CTkTextbox para uma aparência moderna.
Requisitos
Python 3.10 ou superior
Pacotes:
customtkinter
pyperclip
Contribuição
Fique à vontade para abrir issues ou enviar pull requests caso tenha ideias de melhorias ou novos recursos!

Licença
Este projeto é licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.
