
'''
Faça um programa em python que faça a divisão de 1 por um valor passado por uma
variável e realize o tratamento para as entradas abaixo:

entrada = 0
divisao = 1/entrada # vai dar error

#nesse caso tem que ser tratado o erro de divisão por zero, criar um tratamento de
exceção para esse tipo de erro e imprimir uma mensagem amigável com o tipo de
erro.

entrada = "teste"
divisao = 1/entrada # vai dar error

#nesse caso tem que ser tratado o erro de tipo, criar um tratamento # exceção para
esse tipo de erro e imprimir uma mensagem amigável com o tipo de erro.

E deixar o código para tratar erros genéricos diferentes dos mencionados acima.

Caso a entrada seja um valor que não provoque erro, imprimir o valor da divisão.

Por fim, independente de ter erro ou não imprimir ao final da execução do programa,
dentro da estrutura de tratamento de exceções uma mensagem informando seu nome
'''


entrada = input("Digite um valor: ")

try:
    entrada = float(entrada)
    divisao = 1 / entrada
    print("Resultado da divisão:", divisao)
except ZeroDivisionError:
    print("Erro: Divisão por zero é indefinida.")
except ValueError:
    print("Erro: Tipo de entrada inválido.")
except Exception as e:
    print("Ocorreu um erro genérico:", e)
else:
    print("Não houve erros.")
finally:
    print("Sara Freitas")