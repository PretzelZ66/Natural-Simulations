import time
import random
print('Loading')


def pause(number):
    time.sleep(number)


def line(string):
    print(string)
    pause(1)

def Avr_Gen(The_list, gene_type):
    Gene_check = 0
    Average = 0
    if len(The_list) != 0:
        while len(The_list) != Gene_check:
            addition = The_list[Gene_check][gene_type]
            Average += addition
            Gene_check += 1
        Average = Average // len(The_list)
        return(Average)
    return(0)

M = 1
R = 2
T = 10
D = 3
A = 3
S = 27
B = 1
age = 0
fed = 0
fatigue = 0 
b_c = 0 #birth count
population = [[M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c], 
              [M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c],
              [M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c], [M, R, T, D, A, S, B, age, fed, fatigue, b_c],
              [M, R, T, D, A, S, B, age, fed, fatigue, b_c]]
offspring = []
breedable = []
average_genome = []

#facts
generation = 0
food = 0
temperature = 0
temp_rate = 0.1
temp_increase = 1
temp_state = True
temp_max = 5
deaths = 0
births = 0
mutation_rate = 1
fpg_cap = 10000
Avr_M = 0
Avr_R = 0
Avr_T = 0
Avr_D = 0
Avr_A = 0
Avr_S = 0
Avr_B = 0

pause(1)
line('Loaded')
print('')
line('~~CUSTOMISABLE SIMULATION PARAMETERS~~')
line('Would you like the genomes of the population to be displayed every 10 generations?')
user_response = input('YES/NO >>> ')
if user_response.lower() == 'yes':
    display_pop_genome = True
else:
    display_pop_genome = False
line('~~SIMULATION PARAMETERS HAVE BEEN SET~~')

while True:
    pause(1)
    random.shuffle(population)

    #Random Events
    event_check = random.randint(0, 150)
    if event_check == 0:
        print('LOW LEVEL RADIATION HAZARD')
        mutation_rate = random.randint(2, 4)
        event_clock1 = random.randint(1, 10)
    
    #Temperature Change
    if temp_state == True:
        temperature += temp_rate
    elif temp_state == False:
        temperature -= temp_rate

    if temperature >= temp_max or temperature <= 0-temp_max:
        if temp_state == True:
            temperature = temp_max
            temp_state = False
        else:
            temperature = 0-temp_max
            temp_state = True
        temp_max += random.randint(1, 2)
        temp_increase += 1
        temp_rate = 0.1 * temp_increase
        
    #Temperature Deaths
    temp_check = 0
    for i in range(len(population)):
        if population[temp_check][2] < temperature or 0-population[temp_check][2] > temperature:
            del population[temp_check]
            deaths += 1
            temp_check -= 1
        temp_check += 1
    
    #food changing
    food += random.randint(5000, fpg_cap)
    foodupdown = random.randint(-1, 1)
    if foodupdown == -1:
        fpg_cap -= 1000
        if fpg_cap < 5000:
            fpg_cap = 5000
    elif foodupdown == 1:
        fpg_cap += 1000
    
    #Fatigue down
    fatigue_check = 0
    for x in range(len(population)):
        if population[fatigue_check][9] > 0:
            population[fatigue_check][9] -= 1
        fatigue_check += 1
    
    #feeding
    food_check = 0
    for x in range(len(population)):
        if population[food_check][8] == 0 and food > 0:
            food -= 1
            population[food_check][8] = population[food_check][0]
        food_check += 1
    
    #Starvation check
    starve_check = 0
    for x in range(len(population)):
        if population[starve_check][8] == 0:
            del population[starve_check]
            starve_check -= 1
            deaths += 1
        starve_check += 1
    
    #Deaths
    death_check = 0
    while len(population) != death_check:
        death_number = random.randint(1, 100)
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
            death_check -= 1
            deaths += 1
        elif death_number <= population[death_check][3]:
            del population[death_check]
            deaths += 1
            death_check -= 1
        death_check += 1

    #Get averages
    Avr_M = Avr_Gen(population, 0)
    Avr_R = Avr_Gen(population, 1)
    Avr_T = Avr_Gen(population, 2)
    Avr_D = Avr_Gen(population, 3)
    Avr_A = Avr_Gen(population, 4)
    Avr_S = Avr_Gen(population, 5)
    Avr_B = Avr_Gen(population, 6)

    average_genome = [Avr_M, Avr_R, Avr_T, Avr_D, Avr_A, Avr_S, Avr_B]
    
    #Generation of offspring
    Completed = 0
    Past_completed = 0
    breedable1 = []
    breedable2 = []
    
    done_percentage = len(population)
    p_1 = 0
    p_2 = 0
    p_3 = 0
    
    while len(population) != Completed:
        breedable1 = []
        breedable2 = []
        while breedable1 == []:
            if Completed >= len(population):
                break
            if population[Completed][7] >= population[Completed][6] and population[Completed][9] == 0:
                breedable1 = population[Completed]
                Past_completed = Completed
            Completed += 1
        
        if Completed >= (done_percentage * 0.25) and p_3 == 0:
            print("   25%")
            p_3 = 1
        elif Completed >= (done_percentage * 0.50) and p_2 == 0:
            print("   50%")
            p_2 = 1
        elif Completed >= (done_percentage * 0.75) and p_1 == 0:
            print("   75%")
            p_1 = 1
        if Completed >= len(population):
                break
        
        while breedable2 == []:
            if Completed >= len(population):
                break
            if population[Completed][7] >= population[Completed][6] and population[Completed][9] == 0:
                breedable2 = population[Completed]
                break
            Completed += 1
        
        if Completed >= (done_percentage * 0.25) and p_3 == 0:
            print("   25%")
            p_3 = 1
        elif Completed >= (done_percentage * 0.50) and p_2 == 0:
            print("   50%")
            p_2 = 1
        elif Completed >= (done_percentage * 0.75) and p_1 == 0:
            print("   75%")
            p_1 = 1
        if Completed >= len(population):
            break
        
        if breedable2[1] > breedable1[1]:
            litter_cap = random.randint(breedable1[1], breedable2[1])
        elif breedable1[1] > breedable2[1]:
            litter_cap = random.randint(breedable2[1], breedable1[1])
        elif breedable1[1] == breedable2[1]:
            litter_cap = random.randint(breedable1[1], breedable2[1]+1)
        litter = 0
        
        while litter != litter_cap:
            baby = []
            for i in range(7):
                baby_inherit = random.randint(0, 1)
                if baby_inherit == 0:
                    baby.append(breedable1[i])
                else:
                    baby.append(breedable2[i])
            
            mutationyesno = random.randint(1, 1000)
            if mutationyesno <= baby[5]*mutation_rate:
                stat = random.randint(0, 6)
                change = random.randint(0,1)
                if change == 0:
                    baby[stat] += 1
                elif change == 1:
                    baby[stat] -= 1
                
                if baby[4] == 0:
                    baby[4] = 1
                if baby[6] == -1:
                    baby[6] = 0
            baby.append(age)
            baby.append(fed)
            baby.append(fatigue)
            baby.append(b_c)
            
            infant_death_yesno = random.randint(1, 100)
            if infant_death_yesno > baby[3]:
                offspring.append(baby)
            else:
                deaths += 1
            baby = []
            litter += 1
            births += 1
        F_Added = random.randint(1, 2)
        population[Completed][9] = (F_Added + population[Completed][10])
        population[Past_completed][9] = (F_Added + population[Past_completed][10])
        population[Completed][10] += 1
        population[Past_completed][10] += 1
        
        Completed += 1
        
    #aging of population
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] += 1
        age_check += 1
    
    #Hunger check
    hungry_check = 0
    for x in range(len(population)):
        population[hungry_check][8] -= 1
        hungry_check += 1
    
    #Offspring added to population
    population.extend(offspring)

    #Dead creatures converted to food.
    for x in range(deaths):
        bonus_food = random.randint(0, 19)
        if bonus_food == 0:
            food += 1
    
    #Resets
    offspring = []
    breedable = []
    generation += 1
    
    #Event clocks
    if event_clock1 > 0:
        event_clock1 -= 1
    if event_clock1 == 0:
        mutation_rate = 1
    
    #Facts
    print('')
    print(f'Generation: {generation}')
    print(f"Population: {len(population)}")
    print(f"Deaths: {deaths}")
    print(f"Births: {births}")
    if len(population) != 0:
        print(f"Net Growth: {(births - deaths)/len(population)}%")
    else:
        print("Net Growth: -100%")
    print(f'Food: {food}')
    print(f'Temperature: {temperature}')
    print(f'Average Genome: {average_genome}')
    print('---------------------------------------------')
    if display_pop_genome == True:
        if generation %10 == 0:
            line(population)
    births = 0
    deaths = 0
    if len(population) == 0:
        print("EVERY THING DIED")
        time.sleep(20)
        break
