"""Exercício Python #004 - Dissecando uma Variável"""

resposta_usuario = input('Digite algo: ')
print(f'''o tipo primitivo desse valor é {type(resposta_usuario)} 
Só tem espaços? {resposta_usuario.isspace()}
É um número? {resposta_usuario.isnumeric()}
É alfabético? {resposta_usuario.isalpha()}
É alfanúmerico? {resposta_usuario.isalnum()}
Está em maiúsculas? {resposta_usuario.isupper()}
Está em minúsculas? {resposta_usuario.islower()}
Está capitalizada?? {resposta_usuario.istitle()}''') 
