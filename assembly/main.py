import json
from pathlib import Path
import sys

#Verification de l'usage du script
if len(sys.argv) != 2:
    sys.exit('Usage : main.py <code.yq>')

#Import du fichier json
opcodes_path = f"{Path(__file__).resolve().parent}\opcodes.json"

with open(opcodes_path, "r") as f:
    opcodes = json.load(f)

#Print de test A SUPPRIMER
print(opcodes)

#Verification que le fichier ne soit pas vide
with open(sys.argv[1], "r") as code:
    lines = code.readlines()
    if not lines: sys.exit('File is empty')

#Crée une liste avec seulement les instructions et leur valeur
clear_lines = []
for i in range(len(lines)):
    if lines[i].startswith('//') or lines[i] == '\n': continue
    end_line_pos = lines[i].find(';')
    clear_lines.append(lines[i][:end_line_pos])

#Print de test A SUPPRIMER
print(lines)
print(clear_lines)

#Transformation du code textuel en binaire
#Vérification que l'instruction donnée existe
def isOpcode(instruction):
    if instruction not in list(opcodes.keys()):
        return False
    else: return True

#Récupérer la valeur de l'opcode pour pouvoir l'inscrire dans le fichier hexa
def getBinOpcode(opcode_name):
    return f'0{opcodes[opcode_name]}'

#Print de test A SUPPRIMER
print(getBinOpcode('PUSH_CONST'))

#Récupérer la valeur associée à l'instruction (si nécessaire) en hexa
def getBinValue(line, opcode_name):
    if opcode_name in ["ADD", "SUB", "MUL", "DIV"]:
        return "00 00 00 00"
    line.strip()
    
#Transformation d'une valeur entière en hex (NE MARCHE PAS POUR LES MULTIPLES DE 16, A REGLER !!!!)
def intToBin(number):
    bin = []
    hex = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    remainder = 1
    while remainder > 0:
        remainder =  number % 16
        if remainder != 0: 
            bin.append(remainder)
        number = number // 16
    for i in range(len(bin)):
        if bin[i] >= 10: bin[i] = hex[bin[i]]
    bin.reverse()
    bin = ''.join([str(num) for num in bin])
    return bin

print(intToBin(2048))
print(intToBin(366))



#Boucle pour chaque ligne encoder l'instruction et la valeur associée 