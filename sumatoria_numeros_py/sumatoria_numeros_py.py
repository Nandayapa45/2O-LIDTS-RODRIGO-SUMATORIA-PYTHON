
NUM=8
nums= [0]*NUM
total= 0
for i in range (NUM):
        nums[i] =int(input("Por favor, instroduzca el numero: "))
        total+= nums[i]
        print("El total de numero es: ", total)