# bibliotecas = pacotes de códigos
# pip install pyautogui

import pyautogui
import time
import pandas

# Este comando lê o arquivo e guarda tudo na variável 'tabela'
tabela = pandas.read_csv("produtos.csv")

# Vamos apenas ver se ele leu corretamente antes de continuar
print(tabela)

#pyautogui.click -> clica
#pyautogui.write -> escreve um texto
#pyautogui.press -> aperta uma tecla

#pyautogui.hotkey -> aperta um atalho (hotkey)
pyautogui.PAUSE = 0.1
link = "https://www.youtube.com/watch?v=x9us47urjcQ"
# Passo a Passo do seu programa
# Passo 1: Entrar no sistema da empresa
# abriria o navegador
# Passo 1: Abrir o Chrome direto no site
pyautogui.hotkey("win", "r") # Abre o menu Executar
time.sleep(3)

# Digita o comando para abrir o Chrome já no link desejado
# Note que usamos 'chrome' seguido do link
pyautogui.write(f"chrome {link}") 
pyautogui.press("enter")

# # ESPERE o site carregar completamente
# time.sleep(5)
# #MOLO001 Marca Exemplo   Tipo Exemplo    
# # Passo 2: Clicar no primeiro campo (Código do Produto)
# # Agora você precisa do ponto (x, y) do primeiro campo da tabela
# # pyautogui.click(x=600, y=360)
# pyautogui.write(link)
# pyautogui.press("enter")
# # 1. Espera o site carregar completamente
# time.sleep(5)

# # 2. Clica no campo "Código do Produto" usando o ponto que encontraste
# pyautogui.click(x=518, y=284)

# # 3. Preenche o primeiro campo e pula para os próximos com TAB
# pyautogui.write("MOLO001") # Código
# pyautogui.press("tab")

# pyautogui.write("Marca Exemplo") # Marca
# pyautogui.press("tab")

# pyautogui.write("Tipo Exemplo") # Tipo
# pyautogui.press("tab")

# # Continua assim para os outros campos...






