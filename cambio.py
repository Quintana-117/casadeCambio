pesos = int(input("¿Cuántos pesos te sobraron, carnal?:    "))
soles = int(input("Quantos reais sobraram pra você, mano?: "))
reales = int(input("¿Cuántos soles te sobraron, causa?:    "))

peso = 0.051 # 1 peso mexicano = 0.051 USD  
sol = 0.27 # 1 sol = 0.27 USD
real = 0.20 # 1 real = 0.20 USD

total = pesos * peso + soles * sol + reales * real

print(total)
