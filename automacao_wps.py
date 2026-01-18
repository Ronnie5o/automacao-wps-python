import pandas
import pyautogui
import time

# 1. Carregar os dados
tabela = pandas.read_csv("produtos.csv")
tabela = tabela.fillna("Vazio")
# Configuração de segurança: se o mouse for para o canto superior esquerdo, o código para.
pyautogui.FAILSAFE = True

# Configuração global de segurança: se o robô enlouquecer, jogue o mouse no canto superior esquerdo da tela
pyautogui.FAILSAFE = True

# 2. Abrir o WPS
pyautogui.press("win")
time.sleep(3)
pyautogui.write("wps", interval=0.2)
pyautogui.press("enter")

print("Esperando o WPS carregar...")
time.sleep(12) # Tempo para garantir que o programa e possíveis anúncios carreguem

# 3. NAVEGAÇÃO
# Clica no ícone Sheets (Verde) usando sua coordenada atualizada
pyautogui.click(x=30, y=518) 
time.sleep(4)

# Clica no '+' (Planilha em branco)
pyautogui.click(x=175, y=131) 
time.sleep(8) # Tempo maior para a planilha abrir totalmente

# --- GARANTIR O FOCO E A POSIÇÃO INICIAL ---
# Em vez de clicar e arriscar cair no meio da folha, usamos o teclado para ir ao topo
pyautogui.hotkey('ctrl', 'home') 
time.sleep(1)

print("Iniciando a digitação organizada por colunas...")

# 4. Loop de digitação
for linha in tabela.index:
    # Extração dos dados convertendo para texto (string)
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    
    # Digita o código e pula para a coluna B (Marca)
    pyautogui.write(codigo)
    pyautogui.press("tab") 
    
    # Digita a marca e pula para a coluna C (Preço)
    pyautogui.write(marca)
    pyautogui.press("tab") 

    
    # Digita o preço e pula para a linha de baixo, voltando para a coluna A
    pyautogui.write(preco)
    pyautogui.press("enter") 
    
    # Pausa de segurança a cada 5 linhas para você conferir o progresso
    if linha % 5 == 0 and linha > 0:
        print(f"Pausa de segurança na linha {linha}.")
        input("Confira se o WPS está preenchendo certo e aperte ENTER aqui para continuar...")