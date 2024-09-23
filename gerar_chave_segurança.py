# Importando uma biblioteca que ja vem instalada com Python
from secrets import token_hex

"""
Aqui vamos printar uma senha de 16bites (16 caracters) com um valor unico e suguraça alta para utilizar do nosso app"""
print(token_hex(16))

