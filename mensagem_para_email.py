import locale
import json
from datetime import datetime
import string
locale.setlocale(locale.LC_ALL,"")

def converter_para_brl(numero:float) -> str:
    brl = "R$" + locale.currency(numero,symbol=False, grouping=True)
    return brl

data = datetime(2022,12,28)
dados = dict(
    nome = "Arthur Henrique",
    valor= converter_para_brl(1_234_456),
    data = data.strftime("%d/%m/%Y"),
    empresa ="O. M.",
    telefone = "+55 (11)7890-5432",
    codigo_bancario = "110554556485-4556645526666-4452-52-0-54545"
)


texto = '''



Prezado(a) $nome,

informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso seja cancelado , entre em contato com a $empresa no telefone $telefone

Codigo bancario é $codigo_bancario




Atencioso,






${empresa}
Abraço
'''
template = string.Template(texto)

# print(json.dumps(dados, indent=2,ensure_ascii=False))

print(template.substitute(dados))
