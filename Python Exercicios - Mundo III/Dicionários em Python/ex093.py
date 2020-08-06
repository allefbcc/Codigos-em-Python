jogador = dict()
partidas = list()


jogador["Nome"] = str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
print()


for c in range(0, tot):
    partidas.append(int(input(f"Quantos gols na {c+1}° partida? ")))


jogador["Gols"] = partidas[:]
jogador["Total"] = sum(partidas)

print("="*30)
print(jogador)
print("="*30)

for k, v in jogador.items():
    print(f"O campo {k} tem o valor: {v}")

print("="*30)

print(f"O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas.")

for i, v in enumerate (jogador["Gols"]):
    print(f"    => Na {i+1}° partida, fez {v} Gols.")

print(f"{jogador['Nome']} fez um total de {jogador['Total']} Gols")
