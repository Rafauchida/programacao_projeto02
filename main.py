import random
from time import sleep
from database import database
import placar


def shuffle(slots = ["Apple", "Orange", "Banana"]): # randomize the results
    slot1 = random.choice(slots)
    slot2 = random.choice(slots)
    slot3 = random.choice(slots)
    res = [slot1, slot2, slot3]
    return res

def result(res):# print the results from the roll
    for c in res:
        print(f"|| {c} ||", end='')
    sleep(1)
    print()

def head(sample): #create the head to the text
    print(40*"-")
    print(sample)
    print(40*"-")

def results_verify(res = ["Apple", "Orange", "Banana"]):
    reward = 0
    for c in range(2):
        for a in res:
            if res[c] == a:
                reward += 1
    if reward == 2:
        reward = -3
    if reward == 3 or reward == 4:
        reward = 0
    if reward == 6:
        reward = 3
    return reward


placar.game()

head(f"Cada tentativa custa R${1:.2f}")
saldo = 0
nome = input("Digite o seu nome: ")
print(f"Saldo atual: {saldo}")
dinheiro = int(input("Quantos reais deseja colocar?\nSaldo: "))
saldo += dinheiro
while saldo >= 1:
    res = shuffle()
    combinacao = ' '.join(res)
    result(res)
    recompensa = results_verify(res)
    saldo += recompensa
    print(f"Você recebeu {recompensa} \n Saldo: {saldo}")
    play = input("Você quer continuar jogando?\n")
    while play.lower() not in ["sim", "s", "n", "nao"]:
        print("Por favor digite somente 'sim' ou 'nao'")
        play = input("Você quer continuar jogando?\n")
    if play.lower() in ["nao", "n"]:
        break
if saldo <= 0:
    print("Desculpe, sem dinheiro suficiente para jogar")

database.insert(nome, saldo)

head("Resultado final")
print(f"Saldo Final: {saldo}")

leaderboard = database.ranking()
xplacar.ranking(leaderboard[0][0], leaderboard[1][0], leaderboard[2][0])