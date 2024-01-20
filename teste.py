import os

conteudo = open('pi_digits.txt', 'w')
conteudo.write('teste')
conteudo.close()
conteudo = open('pi_digits.txt')


print(conteudo.readlines())
