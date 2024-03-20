#Pares e Ímpares
#Escreva uma função ordernar(lista) que recebe como parâmetro uma lista de inteiros não negativos. E ordene a lista de forma que os pares fiquem em ordem crescente e depois os ímpares em ordem decrescente. o PROGRAMA DEVE SER EM PYTHON

#Entrada:

#[
 # 4,
 # 32,
  #34,
  #543,
  #3456,
  #654,
  #567,
  #87,
  #6789,
  #98
#]
#Saida:

#[
  #4,
  #32,
  #34,
  #98,
  #654,
  #3456,
  #6789,
  #567,
  #543,
 #87
#]
#funcao
def ordenar(lista):
    pares = sorted([x for x in lista if x % 2 == 0]) #sorted ordena a lista, x para cada elemento da lista, se x for par
    impares = sorted([x for x in lista if x % 2 != 0], reverse=True)
    return pares + impares

#teste entrda
entrada = [4, 32, 34, 543, 3456, 654, 567, 87, 6789, 98]
saida = ordenar(entrada)
print(saida)