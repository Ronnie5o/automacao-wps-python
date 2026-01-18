import pandas
import pyautogui
import time

# 1. Carregar os dados
tabela = pandas.read_csv("produtos.csv")
tabela = tabela.fillna("Vazio") # Garante que células vazias não quebrem o código

# Configuração de segurança: se precisar parar, jogue o mouse no canto superior esquerdo da tela
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.3 # Pequeno intervalo entre comandos para estabilidade

# 2. Abrir o WPS
pyautogui.press("win")
time.sleep(2)
pyautogui.write("wps", interval=0.1)
pyautogui.press("enter")

print("Esperando o WPS carregar...")
time.sleep(10) 

# 3. NAVEGAÇÃO
# Clica no ícone Sheets (Verde)
pyautogui.click(x=30, y=518) 
time.sleep(3)

# Clica no '+' (Planilha em branco)
pyautogui.click(x=175, y=131) 
time.sleep(5) 

# RESET DE POSIÇÃO: Garante o início na célula A1
pyautogui.hotkey('ctrl', 'home') 
time.sleep(1)

print("Iniciando transcrissão completa... Mãos ao alto!")

# 4. Loop de digitação SEM PAUSAS
for linha in tabela.index:
    # Extrair todas as colunas do CSV
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])
    
    # Sequência de digitação (Tab para colunas, Enter para nova linha)
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    pyautogui.write(categoria)
    pyautogui.press("tab")
    
    pyautogui.write(preco)
    pyautogui.press("tab")
    
    pyautogui.write(custo)
    pyautogui.press("tab")
    
    pyautogui.write(obs)
    
    pyautogui.press("enter") 
    
    # Apenas um aviso no terminal para você ver que ele está vivo
    if linha % 10 == 0:
        print(f"Linha {linha} processada...")

print("Tarefa concluída com sucesso!")