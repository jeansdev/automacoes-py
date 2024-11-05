## CÓDIGO INICIAL
## import os
## from tkinter.filedialog import askdirectory

## caminho = askdirectory(title="Selecione uma pasta")

## lista_arquivos = os.listdir(caminho)

## locais = {
##    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
##   "videos": [".m4a", ".mp4"],
##    "planilhas": [".xlsx", ".csv"],
##    "docs": [".docx"],
##    "textos": [".txt"],
##    "pdfs": [".pdf"],
##    "rar-zip": [".rar", ".zip"],
##}

## for arquivo in lista_arquivos:
##    ## 01. Arquivo.pdf
##    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
##    for pasta in locais:
##        if extensao in locais[pasta]:
##            if not os.path.exists(f"{caminho}/{pasta}"):
##                os.mkdir(f"{caminho}/{pasta}")
##            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

## Código atual com a correção da possibilidade do arquivo já existir no destino
import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "videos": [".m4a", ".mp4"],
    "planilhas": [".xlsx", ".csv"],
    "docs": [".docx"],
    "textos": [".txt"],
    "pdfs": [".pdf"],
    "rar-zip": [".rar", ".zip"],
}

for arquivo in lista_arquivos:
     ## Exemplo: Se "arquivo" for "01. Arquivo.pdf", então "nome" será o caminho/nome sem a extensão e "extensao" será ".pdf"
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            ## Criar a pasta se ela não existir
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

            destino = f"{caminho}/{pasta}/{arquivo}"
            
            ## Verificar se o arquivo já existe no destino
            if not os.path.exists(destino):
                os.rename(f"{caminho}/{arquivo}", destino)
            else:
                print(f"O arquivo '{arquivo}' já existe em '{pasta}', ignorado.")
            break