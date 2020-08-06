camp = ("Flamengo", "Santos", "Palmeiras", "Grêmio", "Athletico-PR",
        "São Paulo", "Internacional", "Corinthians", "Fortaleza", "Goiás",
        "Bahia", "Vasco", "Atletico-MG", "Fluminense", "Botafogo",
        "Ceará", "Cruzeiro", "CSA", "Chapecoense", "Avaí")







print("="*100)

print(f"Os 5 primeiros colocados são: {camp[0:5]} ")

print("="*100)

print(f"Os 4 ultimos colocados são: {camp[-4:]}")

print("="*100)

print(f" times em ordem alfabética: {sorted(camp)}")

print("="*100)

print(f"A chapecoense está na {camp.index('Chapecoense')+1}° posição")
