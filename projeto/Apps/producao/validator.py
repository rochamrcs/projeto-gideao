from django.core.exceptions import ValidationError
import re

def validar_ordem(value):

    lista = []

    for n in str(value):
        lista.append(n)

    if not isinstance(value, int):
        raise ValueError('Entrada inválida, apenas números inteiros')
    
    if len(lista) != 8:
        raise ValidationError(f'O número {value} tem que ter 8 caracteres numericos.')

def valida_lote(value):

    lista = []

    for n in value:
        lista.append(n)

    valida_estado = ''.join(lista[0:2])
    valida_sequencia = ''.join(lista[6:9]) 
    valida_tipo = ''.join(lista[9])

    if not re.match(r'[rR][jJ]', valida_estado):
        raise ValidationError(f'{valida_estado} está invalído, porfavor verifique!')
    
    if not valida_sequencia.isdigit():
        raise ValidationError(f'{valida_sequencia} está invalído, porfavor verifique!')
    
    if not re.match(r'[eE]', valida_tipo):
        raise ValidationError(f'{valida_tipo} está invalído, porfavor verifique!')
    
    if len(lista) != 10:
        raise ValidationError(f'O lote {value} tem que ter 10 caracteres.')

def valida_volume(value):

    resultado = len(str(value))

    if resultado != 6:
        raise ValidationError(f'Volume inválido.')