times = ("Flamengo", "Cruzeiro", "Palmeiras", "Bahia", "Mirassol", "Bragantino",
          "Botafogo", "Sao Paulo", "Fluminense", "Atletico Mineiro", "Ceara", 
          "Corinthians","Internacional", "Gremio", "Santos","Vitoria", "Vasco da Gama",
            "Fortaleza", "Juventude", "Sport")
print("CAMPEONATO BRASILEIRAO DE FUTEBOL".center(60,"="))
print(f"Os 5 primeiros colocados sao {times[:5]}")
print("-=" *30)
print(f"Os ultimos 4 colocados sao {times[-4:]}")
print("-=" *30)
print(f"Os times em ordem alfabetica sao {sorted(times)}")
print("-=" *30)
print(f"O Sao paulo esta na {times.index('Sao Paulo') +1} posicao")