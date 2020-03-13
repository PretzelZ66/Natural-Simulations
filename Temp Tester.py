import random

generation = 1

temperature = 0
temp_rate = 0.1
temp_increase = 1
temp_state = True
temp_max = 5

print('WHAT WOULD YOU LIKE TO CALL THE RESULTS FILE?')
file_name = input('>>> ')
file_name_raw = file_name + '_raw.txt'

with open(file_name_raw, 'x') as file:
    file.close()

while True:
    #temperature change
    print('    Temperature Change')
    
    temp_rate = 0.1 * temp_increase
    temp_boost = (random.randint((0-(temp_max//2)), (temp_max // 2)) * 0.1)
    temp_rate += temp_boost
    naturilisation = random.randint(0, 100)

        #Temp Change
    if temp_state == True:
        if naturilisation == 0:
            temperature -= temp_rate
            print("na")
        else:
            temperature += temp_rate
    elif temp_state == False:
        if naturilisation == 0:
            temperature += temp_rate
            print("na")
        else:
            temperature -= temp_rate
    
        #Temp Max Change
    if temperature >= temp_max:
        if temp_state == True:
            temp_state = False
            temperature = temp_max
            temp_max += (random.randint(5, 20) * 0.1)
            temp_increase += 1
    elif temperature <= (0 - temp_max):
        if temp_state == False:
            temp_state = True
            temperature = (0 - temp_max)
            temp_max += (random.randint(5, 20))
            temp_increase += 1

    generation += 1

    print(f"Generation: {generation}")
    print(f'Temperature: {temperature}')
    print('---------------------------------------------')
    
    with open(file_name_raw, 'a') as output:
        output.write(f'{generation}\n')
        output.write(f'0\n')
        output.write(f"0\n")
        output.write(f'0\n')
        output.write("0%\n")
        output.write(f'0\n')
        output.write(f'{temperature}\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.write(f'0\n')
        output.close()
