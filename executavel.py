from pathlib import Path

from PyPDF2 import PdfFileMerger,PdfFileReader
import os

caminho = str(os.path.dirname(os.path.realpath(__file__))) # Define o caminho que se encontra o executavel

listaPDFs = os.listdir(caminho + '/pdfs') # Cria a lista em ordem alfabética crescente dos pdfs
listaPdfsCombinados = os.listdir(caminho + '/Output')

merger = PdfFileMerger()

if ['Combinado.pdf'] == listaPdfsCombinados:
    os.remove(caminho + '/Output/Combinados.pdf')

for file in listaPDFs:
    merger.append(PdfFileReader(caminho + '/pdfs/' + file))

merger.write(caminho + '/Output/Combinados.pdf')
