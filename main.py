import modules.classBanner as cBanner
import modules.classPlayer as cPlayer

    
#Programa principal - teste de gacha:

#Instanciar jogador:
player = cPlayer.Player('player')

#Instanciar banner:
banner = cBanner.charBanner()
banner.loadBanner()

print('-------------------------------')
print('Genshin Impact Gacha Simulator!')
print('-------------------------------\n')
times = int(input('Digite o número de sorteios: '))

player.loadState() #Carregar estado no arquivo do jogador
player.playerSummon(times, banner.items) #Realizar 180 sorteios:
player.saveState() #Salvar estado final no arquivo