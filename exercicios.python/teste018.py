from math import radians,sin,cos,tan
an = float(input("Digite um ângulo:"))
seno = sin(radians(an))
print(f"O angulo de {an} tem o SENO  de {seno:.2f}")
cosseno = cos(radians(an))
print(f"O angulo de {an} tem o COSSENO  de {cosseno:.2f}")
tangente = tan(radians(an))
print(f"O angulo de {an} tem a TANGENTE de {tangente:.2f}")
