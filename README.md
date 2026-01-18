Descrição
Este projeto é uma automação desenvolvida em Python para transcrever dados de um arquivo CSV para o software de planilhas WPS Office. O robô navega pela interface, abre uma nova planilha e preenche 7 colunas de dados de forma organizada.

Desafios Superados
Posicionamento Preciso: Implementação do atalho Ctrl + Home para garantir que o robô sempre comece na célula A1, evitando erros de preenchimento em locais aleatórios.

Organização em Colunas: Uso estratégico de Tab e Enter para separar Código, Marca, Tipo, Categoria, Preço, Custo e Observações.

Tratamento de Dados: Utilização da biblioteca pandas com fillna("Vazio") para gerenciar células em branco e evitar interrupções no script.

Tecnologias
Python

PyAutoGUI (Automação de GUI)

Pandas (Manipulação de dados)

