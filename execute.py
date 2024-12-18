import argparse
from papermill import execute_notebook
import random
import os

# pip install papermill
# COMANDO DE EXECUÇÃO PRO TERMINAL
# python execute.py  --criteria_path "df_delta50_comm.xlsx" --forindex_path "df_Delta50_comm.xlsx"  --criteria_sheet "delta_50"  --forindex_sheet "prices" --method "<"  --quantils 5 --dc_name "date"

parser = argparse.ArgumentParser(description='Executar o notebook com parâmetros')
parser.add_argument('--criteria_path', type=str, required=True, help='Caminho para o arquivo com dados de critério')
parser.add_argument('--forindex_path', type=str, required=True, help='Caminho para o arquivo com dados para cálculo do índice')
parser.add_argument('--criteria_sheet', type=str, required=True, help='Nome da planilha com dados de critério (se necessário)')
parser.add_argument('--forindex_sheet', type=str, required=True, help='Nome da planilha de dados para cálculo do índice (se necessário)')
parser.add_argument('--method', type=str, required=True, help='Comprar o que está acima e vender o que está abaixo (>) ou o contrário (<)')
parser.add_argument('--quantils', type=int, required=True, help='Número de quantis')
parser.add_argument('--dc_name', type=str, required=True, help='Nome da coluna que possui as datas')



args = parser.parse_args()

output_path = os.path.join('outputs', f'Execução {args.criteria_sheet}-{args.forindex_sheet}.ipynb')

execute_notebook(
    'IndexCreationByQuantils.ipynb',  
    output_path,  
    parameters=dict(
        criteria_path=args.criteria_path,
        forindex_path=args.forindex_path,
        criteria_sheet=args.criteria_sheet,
        forindex_sheet=args.forindex_sheet,
        method=args.method,
        quantils=args.quantils,
        dc_name = args.dc_name
    )
)

