print("\nCalcular Temperatura Fahrenheit para Celsius")


# Formula C = (F - 32) × 5/9 

Temperatura_F = float(input("\nInforme a Temperatura Fahrenheit: " ))

# SetVars 
Temperatura_C = (Temperatura_F - 32) * 5/9 
situacaoTemperatura = ""

if Temperatura_C >= 30:
    situacaoTemperatura = "Calor"
elif Temperatura_C >= 20:
    situacaoTemperatura = "Amena"
else:
    situacaoTemperatura = "Frio"

print(f"{Temperatura_F}°F, em Celsius é: {Temperatura_C:.2f}°C, a temperatura está {situacaoTemperatura}")
