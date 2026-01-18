import pandas

# Passo 1: Carregar a tabela
tabela = pandas.read_csv("produtos.csv")
# --- PASSO DE TRATAMENTO (Limpeza) ---

# 1. Ver se tem valores vazios (NaN) e decidir o que fazer.
# Vamos usar o .fillna() para preencher espaços vazios.
# Exemplo: Se não tiver observação, escreve "Nenhuma".
tabela = tabela.fillna("Vazio")

# 2. Se houver linhas totalmente vazias, podemos excluí-las:
tabela = tabela.dropna(how="all", axis=0) 

print("\n--- Tabela Tratada e Limpa! ---")
print(tabela.head())

# Passo 2: Mostrar a tabela inteira no terminal
print("--- TABELA COMPLETA ---")
print(tabela)

# Passo 3: Aprender a pegar um dado específico
# Vamos ver apenas o código do produto da primeira linha (linha 0)
primeiro_codigo = tabela.loc[0, "codigo"]

print(f"\nO código do primeiro produto é: {primeiro_codigo}")
# Vamos ver qual é a MARCA do produto na linha 1
segunda_marca = tabela.loc[1, "marca"]
print(f"A marca do segundo produto é: {segunda_marca}")
# O 'for' percorre cada índice da sua tabela (de 0 até 292)
for linha in tabela.index:
    # Pegamos o código e a marca de cada linha
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    
    # Vamos apenas imprimir no terminal para ver acontecer
    print(f"Lendo linha {linha}: Produto {codigo} da marca {marca}")





# --- NOVA PARTE: CÁLCULO DE LUCRO ---
print("\n" + "="*30) 
print("CÁLCULO DE LUCRO POR PRODUTO")
print("="*30 + "\n")

for linha in tabela.index:
    # 1. Primeiro coletamos os dados da tabela
    codigo = tabela.loc[linha, "codigo"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    
    # 2. AGORA fazemos a conta (essencial vir antes do print)
    lucro = preco - custo 
    
    # 3. Agora os prints podem usar a variável 'lucro'
    dados_completos = tabela.iloc[linha] 
    
    print("-" * 30)
    print(f"RESUMO: {codigo} | Lucro: R${lucro:.2f}")
    print("DADOS COMPLETOS DESTA LINHA:")
    print(dados_completos)
    print("-" * 30)
    
    print(f"Produto: {codigo} | Preço: {preco} | Custo: {custo} | Lucro: R${lucro:.2f}")
    # Acrescentando esse novo print
    print(f"Produto: {codigo} | Preço: {preco} | Custo: {custo} | Lucro: R${lucro:.2f}")
    # --- PASSO: EXCLUSÃO DE COLUNAS DESNECESSÁRIAS ---

# O comando .drop exclui colunas. 
# axis=1 significa que estamos excluindo uma COLUNA (vertical)
# columns=["nome_da_coluna"] é onde você coloca o que quer tirar

#tabela = tabela.drop(columns=["obs"], axis=1) 
#print("\n--- Coluna 'obs' removida com sucesso! ---")
#print(tabela.head()) # Veja que a coluna sumiu do print

# --- NOVA PARTE: FILTRANDO DADOS ---
print("\n" + "="*30)
print("APENAS PRODUTOS DA MOTOROLA")
print("="*30)

# Criamos uma nova tabela (dataframe) apenas com a marca desejada
tabela_motorola = tabela.loc[tabela["marca"] == "Motorola"]

print(tabela_motorola)
print(f"\nQuantidade de produtos encontrados: {len(tabela_motorola)}")
# --- NOVA PARTE: VALOR TOTAL DO ESTOQUE MOTOROLA ---

# Somamos a coluna de preço unitário apenas da tabela filtrada
faturamento_potencial = tabela_motorola["preco_unitario"].sum()

print(f"\nSe vendermos todos os itens da Motorola, o faturamento será de: R${faturamento_potencial:.2f}")
# --- PASSO FINAL: SALVAR O RELATÓRIO ---

# O comando .to_csv cria um arquivo novo
# index=False serve para não salvar aquela coluna de números (0, 1, 2...) no arquivo
tabela_motorola.to_csv("relatorio_motorola.csv", index=False)

print("\n" + "!"*30)
print("ARQUIVO 'relatorio_motorola.csv' GERADO COM SUCESSO!")
print("Verifique a sua pasta no VS Code!")
print("!"*30)
