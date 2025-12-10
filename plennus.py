import pandas as pd
import ezodf
import subprocess

data_inicio = input("Digite a data de início ex: 2023-12-16: ")
data_fim = input("Digite a data de fim ex: 2023-12-15: ")
author = input("Digite o nome do usuario git: ")
nm_completo = input("Digite seu nome completo: ")

caminho_arquivo_txt = 'texto.txt'

with open(caminho_arquivo_txt, 'w') as arquivo:
    pass

plennus_code = subprocess.run(f"bash plennus {data_inicio} {data_fim} {author}", shell=True, capture_output=True, text=True)
print("Buscando dados e adicionando no texto.txt:", plennus_code.stdout)

emojis = [":art:",
    ":zap:",
    ":fire:",
    ":bug:",
    ":ambulance:",
    ":sparkles:",
    ":pencil:",
    ":rocket:",
    ":lipstick:",
    ":tada:",
    ":white_check_mark:",
    ":lock:",
    ":bookmark:",
    ":construction:",
    ":arrow_up:",
    ":arrow_down:",
    ":pushpin:",
    ":construction_worker:",
    ":chart_with_upwards_trend:",
    ":recycle:",
    ":hammer:"]

meses = {"01":"JANEIRO",
    "02":"FEVEREIRO",
    "03":"MARÇO",
    "04":"ABRIL",
    "05":"MAIO",
    "06":"JUNHO",
    "07":"JULHO",
    "08":"AGOSTO",
    "09":"SETEMBRO",
    "10":"OUTUBRO",
    "11":"NOVEMBRO",
    "12":"DEZEMBRO",
}
segundas_partes = []

# Leitura do arquivo de texto
dados_txt = open(caminho_arquivo_txt, 'r').readlines()

# Função para realizar o split com base nos emojis
def split_string(string):
    for emoji in emojis:
        if emoji in string:
            return string.split(emoji, 1)[1].strip()
    return string

# Iterar sobre a lista de strings e armazenar as segundas partes
for texto_com_emoji in dados_txt:
    segunda_parte = split_string(texto_com_emoji)
    segundas_partes.append(segunda_parte)

dados_txt = segundas_partes

# Adiciona o arquivo ODS
caminho_arquivo_ods = "padrao.ods"
doc = ezodf.opendoc(caminho_arquivo_ods)

# Selecionar a primeira folha da planilha (índice 0)
planilha = doc.sheets[0]



# Preencher a coluna C da linha 12 a 25 com os valores da lista
linha_inicial = 11
linha_final = 24
coluna_c = 2  # Índice da coluna C (0-indexed)

for indice_linha, valor in enumerate(dados_txt):
    linha = linha_inicial + indice_linha
    if linha <= linha_final:
        planilha[linha, coluna_c].set_value(valor)

mes_txt_inicio = meses[data_inicio[5:7]]

mes_txt_fim = meses[data_fim[5:7]]

# Mudar a data interna da planilha
coluna_g = 6
posicao_linha = 8
planilha[posicao_linha, coluna_g].set_value(f'16/{data_inicio[5:7]}/{data_inicio[0:4]} a 15/{data_fim[5:7]}/{data_fim[0:4]}')

# Salvar as alterações
caminho_novo_arquivo_ods = f'16 {mes_txt_inicio} a 15 {mes_txt_fim} - {nm_completo}.ods'
doc.saveas(caminho_novo_arquivo_ods)

print(f'Planilha preenchida com sucesso em {caminho_novo_arquivo_ods}.')
