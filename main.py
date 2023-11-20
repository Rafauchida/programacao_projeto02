from random import randint
from database import database

def sequencia(streak = 0):
	if streak < 3:
		return False
	if streak >= 3:
		return True
	
def par_verification(player = 2):
	if player % 2 == 0:
		return True
	else:
		return False

pontos = 0
streak = 0
player_name = input("Digite o seu nome: ")

while True:
	computer = randint(1, 5)
	bonus = sequencia(streak)
	player = int(input("Digite um número entre 1-5: "))
	while player not in [0, 1, 2, 3, 4, 5]:
		player = int(input("Favor digitar um número entre 1-5: "))
	if player == 0:
		break
	elif player == computer:
		if bonus:
			pontos += (streak * pontos)
			bonus = streak * pontos
		else:
			pontos += 1
			bonus = 1
		streak += 1
		print(f"Você ganhou {bonus} pontos! O número era {computer} e você escolheu {player}")
		print(f"streak: {streak}")
		print(f"pontos: {pontos}")
	else:
		streak = 0
		print(f"Você errou! O número escolhido era {computer} e você digitou {player}")
		print(f"streak: {streak}")
		print(f"pontos: {pontos}")

	if par_verification(player):
		print(f"O seu número é par")
	else:
		print(f"O seu número não é par")

database.insert(player_name, pontos)
data = database.get_balance()

for c in range(len(data)):
	print(f"{c+1}° lugar: {data[c][0]}")
	print(f"pontos: {data[c][1]}")
	if(c == 2):
		break