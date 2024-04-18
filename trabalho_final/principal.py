from glicemia import Glicemia
from statistics import mode, median, mean

nome_arquivo = "glicose_data_suja.csv"

lista_glicemias = []

#ler arquivo

with open(nome_arquivo, "r", encoding='utf8') as leitor:
    for linha in leitor:
        valor_corrigido = linha.replace(",",";")
        vetor_linha = valor_corrigido.split(";")

        glicemia = Glicemia(vetor_linha[0], vetor_linha[1], vetor_linha[3], vetor_linha[4],
                       vetor_linha[5], vetor_linha[6], vetor_linha[7])
        lista_glicemias.append(glicemia)

for item in lista_glicemias:
   print(item)

#valores em listas separadas

valores_glicemia = []
valores_kcal = []
valores_carb = []

for glicemia in lista_glicemias:
    valores_glicemia.append(glicemia.valor_glicemia)
    valores_kcal.append(glicemia.kcal)
    valores_carb.append(glicemia.carb)

#media, mediana e moda

def calcular_media(lista):
    for item in lista:
        media = mean(lista)
    return media

def calcular_mediana(lista):
    for item in lista:
        mediana = median(lista)
    return mediana

def calcular_moda(lista):
    for item in lista:
        moda = mode(lista)
    return moda

##

media_glicemia = calcular_media(valores_glicemia)
media_kcal = calcular_media(valores_kcal)
media_carb = calcular_media(valores_carb)

print("Valor da média de glicemia:", media_glicemia, "mg/dL")
print("Valor da média de kcal:", media_kcal, "kcal")
print("Valor da média de carboidratos:", media_carb, "g")

mediana_glicemia = calcular_mediana(valores_glicemia)
mediana_kcal = calcular_mediana(valores_kcal)
mediana_carb = calcular_mediana(valores_carb)

print("Mediana dos valores de glicemia:", mediana_glicemia,"mg/dL")
print("Mediana dos valores de calorias:", mediana_kcal,"kcal")
print("Mediana dos valores de carboidratos:", mediana_carb,"g")

moda_glicemia = calcular_moda(valores_glicemia)
moda_kcal = calcular_moda(valores_kcal)
moda_carb = calcular_moda(valores_carb)

print("Moda dos valores de glicemia:", moda_glicemia)
print("Moda dos valores de calorias:", moda_kcal)
print("Moda dos valores de carboidratos:", moda_carb)