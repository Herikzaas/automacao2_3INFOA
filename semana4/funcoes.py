def areaTR (base,altura):
    area = (base*altura)/2
    return area

def areaQD (lado) :
    area = lado*lado
    return area


print(f'A area do triangulo é {areaTR(2,10)}')

base = float(input('Digite a base :'))
altura = float(input('Digite a altura :'))

print(f'A area do triangulo é {areaTR(base,altura)}')