#Importar bibliotecas necessárias
import random

'''
Regras do sistema de sorteio do Genshin Impact:
1 - Dentro de 10 sorteios, é garantido que o jogador receberá um item de 4 ou 5 estrelas;
2 - Dentro de 90 sorteios, é garantido que o jogador receberá um item 5 estrelas;
3 - Se o último item 4 estrelas sorteado não for do banner, o próximo 4 estrelas será do banner;
4 - Se o último item 5 estrelas sorteado não for do banner, o próximo 5 estrelas será do banner;
'''

#Função para sortear um item 4 estrelas - retorna o índice do item sorteado:
def summon4Star(featured4Star):
    if featured4Star == True:
        return random.randint(0,2) #Sortear um indice que representa um número limitado, nesse caso, os limitados vão de 0 a 3
    else:
        result = random.uniform(0.0, 1.0) #Sorteia um 4 estrelas qualquer levando em consideração o peso de raridade
        if result <= 0.50000:
            return random.randint(0,2) #Retorna um 4 estrelas do banner
        else:
            return random.randint(3,43) #Retorna um 4 estrelas que não é do banner

#Função para sortear um item 5 estrelas - retorna o índice do item sorteado:
def summon5Star(featured5Star):
    if featured5Star == True:
        return 0 #Retorna o índice do personagem limitado
    else:
        result = random.uniform(0.0, 1.0) #Sorteia um 5 estrelas qualquer levando em consideração o peso de raridade
        if result <= 0.50000:
            return 0 #Sorteou o personagem do banner
        else:
            return random.randint(1,6) #Retorna um personagem 5 estrelas que não é do banner

#Função para mostrar o resultado no terminal:
def print_result(midCont, maxCont, item, featured4Star, featured5Star):
    print(f'[4: {midCont:2}-{str(featured4Star):5} || 5: {maxCont:2}-{str(featured5Star):5}] Ganhou {item}')

#Definição da função que mostrará o item obtido e retornará o status do jogador em relação ao gacha:
def summon (items, featured4Star, featured5Star, maxCont, midCont):
    #Incrementar contadores:
    maxCont += 1
    midCont += 1

    #Direcionar sorteador de acordo com as contagens
    if midCont == 10 and maxCont < 90: #Item deve ser pelo menos 4 restrelas
        tier_result = random.uniform(0.0, 1.0)
        if tier_result <= (5.1/5.8): #Apenas normalizando as porcentagens
            summon_result = summon4Star(featured4Star)
            print_result(midCont, maxCont, items[1][summon_result], featured4Star, featured5Star)
            midCont = 0
            if summon_result < 4:
                featured4Star = False
            else:
                featured4Star = True
        else:
            summon_result = summon5Star(featured5Star)
            print_result(midCont, maxCont, items[2][summon_result], featured4Star, featured5Star)
            midCont = 0
            maxCont = 0
            if summon_result == 0:
                featured5Star = False
            else:
                featured5Star = True
    elif maxCont == 90: #Item deve ser um 5 estrelas
        summon_result = summon5Star(featured5Star)
        print_result(midCont, maxCont, items[2][summon_result], featured4Star, featured5Star)
        midCont = 0
        maxCont = 0
        if summon_result == 0:
            featured5Star = False
        else:
            featured5Star = True
    else:
        #Pode ser um item qualquer
        tier_result = random.uniform(0.0, 1.0)
        if tier_result <= 0.94300: #Sortear um item 3 estrelas
            summon_result = random.randint(0,12) #Um item 3 estrelas qualquer
            print_result(midCont, maxCont, items[0][summon_result], featured4Star, featured5Star)
        elif tier_result <= 0.99400:#Sortear um item 4 estrelas
            summon_result = summon4Star(featured4Star)
            print_result(midCont, maxCont, items[1][summon_result], featured4Star, featured5Star)
            midCont = 0
            if summon_result < 4:
                featured4Star = False
            else:
                featured4Star = True
        else: #Sortear um item 5 estrelas
            summon_result = summon5Star(featured5Star)
            print_result(midCont, maxCont, items[2][summon_result], featured4Star, featured5Star)
            midCont = 0
            maxCont = 0
            if summon_result == 0:
                featured5Star = False
            else:
                featured5Star = True
    
    return [midCont, maxCont, featured4Star, featured5Star] #retorna o estado do jogador após o sorteio
