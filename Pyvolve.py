#Pyvolve 1.2.0
import time, random
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
contaminated = False
population = []
offspring = []
breedable = []
average_genome = []
pop_template = [M, R, T, D, A, S, B, age, fed, fatigue, b_c, contaminated]

#facts
generation = 0
deaths = 0
births = 0
food = 0
fpg_cap = 10000
breedable_count = 0

temperature = 0
temp_rate = 0.1
temp_increase = 1
temp_state = True
temp_max = 5

events =  0
event_clock1 = 0

Avr_M = 0
Avr_R = 0
Avr_T = 0
Avr_D = 0
Avr_A = 0
Avr_S = 0
Avr_B = 0

class Virus:
    infected = 0
    food = 0
    kill_chance = 5
    mutaion_chance = 1
    infectiousness = 5
    metabolism = 3

pause(1)
line('Loaded')
print('')
line('~~CUSTOMISABLE SIMULATION PARAMETERS~~')

line('What would you like to call the results file?')
file_name = input('>>> ')
file_name_raw = file_name + '_raw.txt'
file_name += '.txt'
with open(file_name, 'x') as file:
    file.close()
    
with open(file_name_raw, 'x') as file:
    file.close()

line('What preset would you like to use? Default(0), Nuclear Playground(1), Thermonuclear Playground(2), Custom(OTHER)')
preset_type = int(input('>>> '))

if preset_type == 0:
    #Default
    start_pop = 50
    event_chance_cap = 100
    mutation_rate = 1
    default_mutation_rate = mutation_rate
    mutation_severity = 1
    infect_counter = 1
    
elif preset_type == 1:
    #Nuclear_playground
    start_pop = 50
    event_chance_cap = 69
    mutation_rate = 100
    default_mutation_rate = 100
    mutation_severity = 5
    infect_counter = 1

elif preset_type == 2:
    #Thermonuclear_playground
    start_pop = 50
    event_chance_cap = 49
    mutation_rate = 500
    default_mutation_rate = 500
    mutation_severity = 25
    infect_counter = 0
    
else:
    line('What would you like the starting population to be?')
    start_pop = int(input('>>> '))
    if start_pop <= 1:
        start_pop = 2

    line('Would you like a Low (3), Medium (2), or High (1) event chance?')
    event_chance = int(input('1/2/3 >>> '))
    if event_chance > 0 and event_chance <= 3:
        event_chance_cap = event_chance
    else:
        event_chance_cap = 2
    event_chance_cap = event_chance_cap * 50
    
    line('What would you like the default radiation level to be?')
    mutation_rate = int(input('>>> '))
    default_mutation_rate = mutation_rate

    line('What would you like the mutation severity to be?')
    mutation_severity = int(input('>>> '))

    line('How many creatures would you like to start out with the virus?')
    infect_counter = int(input('>>> '))

pop_gen_check = 0
while pop_gen_check != start_pop:
    if infect_counter != Virus.infected:
        contaminated = True
        Virus.infected += 1
    else:
        contaminated = False
    
    pop_template = [M, R, T, D, A, S, B, age, fed, fatigue, b_c, contaminated]
    population.append(pop_template)
    pop_gen_check += 1

line('~~SIMULATION PARAMETERS HAVE BEEN SET~~')

while True:
    deaths = 0
    pause(1)
    random.shuffle(population)
    
    #food changing
    print('    Changing Food')
    food += random.randint(5000, fpg_cap)
    foodupdown = random.randint(-1, 1)
    if foodupdown == -1:
        fpg_cap -= 1000
        if fpg_cap < 5000:
            fpg_cap = 5000
    elif foodupdown == 1:
        fpg_cap += 1000

    #Breedable assignment
    print('    Sorting Breedables from Unbreedables')
    breedable_check = 0
    for i in range(len(population)):
        if len(population[breedable_check]) == 13:
            del population[breedable_check][12]
        
        if population[breedable_check][6] <= population[breedable_check][7] and population[breedable_check][9] == 0:
            breedable = True
            population[breedable_check].append(breedable)
            breedable_count += 1
        else:
            breedable = False
            population[breedable_check].append(breedable)
        breedable_check += 1
    
    #Event clocks
    print('    Event Clocks')
    if event_clock1 > 0:
        event_clock1 -= 1
        if event_clock1 == 0:
            mutation_rate = default_mutation_rate
    if event_clock2 > 0:
        event_clock2 -= 1
        print("AFTERSHOCK")
        death_check = 0
        while len(population) != death_check:
            death_number = random.randint(1, 400)
            if death_number == 13:
                if population[death_check][12] == True and breedable_count > 2:
                    del population[death_check]
                    death_check -= 1
                    deaths += 1
                    breedable_count -= 1
            death_check += 1
        
    #Random Events
    print('    Random event check')
    event_done = ''
    event_check = random.randint(0, event_chance_cap)
    if event_check == 0:
        event = random.randint(events, 7)
        if event == 0:
            event_done = 'ENVIRONMENT STABILITY LOWERED'
            event_chance_cap -= 1
            if event_chance_cap > 0:
                event_chance_cap -= random.randint(1, 5)
            if event_chance_cap < 0:
                events = 1
                
        elif event == 1:
            event_done = 'LOW LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(2, 4)
            event_clock1 += random.randint(1, 10)
        elif event == 2:
            event_done = 'MEDIUM LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(4, 6)
            event_clock1 += random.randint(5, 15)
        elif event == 3:
            event_done = 'HIGH LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(6, 8)
            event_clock1 += random.randint(10, 20)
        elif event == 4:
            event_done = 'VOLCANIC ERRUPTION'
            temp_max += random.randint(3, 5)
            temperature -= random.randint(1, 3)
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 250)
                if death_number == 13:
                    if population[death_check][12] == True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
        elif event == 5:
            event_done = 'FAMINE'
            food -= random.randint(3000, 9000)
            if food <= 0:
                food = 0
            if foodupdown == -1:
                fpg_cap -= 1000
                if fpg_cap < 5000:
                    fpg_cap = 5000
        elif event == 6:
            event_done = 'PLAGUE'
            Plague_check = 0
            while len(population) != Plague_check:
                death_number = random.randint(0, 100)
                if death_number == 0:
                    population[Plague_check][11] = True
                    Plague_check += 1
        elif event == 7:
            event_done = 'EARTHQUAKE'
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 300)
                if death_number == 13:
                    if population[death_check][12] == True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
            event_clock2 += random.randint(1, 3)
        print(event_done)
        
    #Temperature Change
    print('    Temperature Change')
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
    print('    Temperature Deaths')
    temp_check = 0
    for i in range(len(population)):
        if population[temp_check][2] < temperature or 0-population[temp_check][2] > temperature:
            del population[temp_check]
            deaths += 1
            temp_check -= 1
        temp_check += 1
    
    #Fatigue down
    print('    Fatigue Down')
    fatigue_check = 0
    for x in range(len(population)):
        if population[fatigue_check][9] > 0:
            population[fatigue_check][9] -= 1
        fatigue_check += 1
    
    #feeding
    print('    Feeding')
    food_check = 0
    for x in range(len(population)):
        if population[food_check][8] == 0 and food > 0:
            food -= 1
            population[food_check][8] = population[food_check][0]
        food_check += 1
    
    #Starvation check
    print('    Starvation Check')
    starve_check = 0
    for x in range(len(population)):
        if population[starve_check][8] == 0:
            del population[starve_check]
            starve_check -= 1
            deaths += 1
        starve_check += 1
    
    #Virus Deaths
    print('    Virus Killing')
    Virus_check = 0
    for x in range(len(population)):
        Virus_chance = random.randint(1, 100)
        if Virus_chance <= Virus.kill_chance:
            del population[Virus_check]
            Virus_check -= 1
            deaths += 1
            Virus.food += random.randint(1, 3)
        Virus_check += 1
    
    #Deaths
    print('    Deaths')
    death_check = 0
    while len(population) != death_check:
        death_number = random.randint(1, 100)
        if population[death_check][7] == population[death_check][4]:
            del population[death_check]
            death_check -= 1
        elif death_number <= population[death_check][3]:
            del population[death_check]
            deaths += 1
            death_check -= 1
        death_check += 1
    
    #Generation of offspring
    print('    Generation of offspring')
    births = 0
    Completed = 0
    Past_completed = 0
    breedable1 = []
    breedable2 = []
    
    
    while len(population) != Completed:
        breedable1 = []
        breedable2 = []
        while breedable1 == []:
            if Completed >= len(population):
                break
            if population[Completed][12] == True:
                breedable1 = population[Completed]
                Past_completed = Completed
            Completed += 1
        if Completed >= len(population):
                break
        
        while breedable2 == []:
            if Completed >= len(population):
                break
            if  population[Completed][12] == True:
                breedable2 = population[Completed]
                break
            Completed += 1
            
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
                    baby[stat] += random.randint(1, mutation_severity)
                elif change == 1:
                    baby[stat] -= random.randint(1, mutation_severity)
                
                if baby[1] <= 0:
                    baby[1] = 1
                if baby[4] <= 0:
                    baby[4] = 1
                if baby[6] <= -1:
                    baby[6] = 0
            baby.append(age)
            baby.append(fed)
            baby.append(fatigue)
            baby.append(b_c)
            
            if breedable1[11] == True or breedable2[11] == True:
                willinfect = random.randint(0, 99)
                if willinfect <= Virus.infectiousness:
                    contaminated = True
            else:
                contaminated = False
            baby.append(contaminated)
            
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
    print('    Aging of population')
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] += 1
        age_check += 1
    
    #Hunger check
    print('    Hunger check')
    hungry_check = 0
    for x in range(len(population)):
        population[hungry_check][8] -= 1
        hungry_check += 1
    
    #Offspring added to population
    print('    Offspring added to population')
    population.extend(offspring)
    
    #Virus Mutation
    print('    Mutating virus')
    if Virus.mutaion_chance >= random.randint(1, 100):
        Virus_Decider = random.randint(1, 4)
        change = random.randint(1, 2)
        if change == 2:
            change = -1
        
        if Virus_Decider == 1:
            Virus.kill_chance += change
        elif Virus_Decider == 2:
            Virus.mutaion_chance += change
        elif Virus_Decider == 3:
            Virus.infectiousness +=  change
        elif Virus_Decider == 4:
            Virus.metabolism += change
        
    #Get averages
    print('    Getting average genes')
    Avr_M = Avr_Gen(population, 0)
    Avr_R = Avr_Gen(population, 1)
    Avr_T = Avr_Gen(population, 2)
    Avr_D = Avr_Gen(population, 3)
    Avr_A = Avr_Gen(population, 4)
    Avr_S = Avr_Gen(population, 5)
    Avr_B = Avr_Gen(population, 6)

    average_genome = [Avr_M, Avr_R, Avr_T, Avr_D, Avr_A, Avr_S, Avr_B]

    Virus_genome = [Virus.kill_chance, Virus.mutaion_chance, Virus.infectiousness, Virus.metabolism]

    #Dead creatures converted to food.
    print('    Dead creatures converted to food')
    for x in range(deaths):
        if random.randint(1, 20) == 1:
            food += 1

    #Virus feeding/deaths
            
    #Virus Curing
    print('    Curing virus')
    for i in range(len(population)):
        if population[i][11] == True:
            if random.randint(1, 100) == 1:
                population[i][11] = False
    
    #Virus Check
    print('    Checking for virus')
    Virus.infected = 0
    for i in range(len(population)):
        if population[i][11] == True:
            Virus.infected += 1
    
    #Resets
    print('    Resets')
    offspring = []
    generation += 1
    breedable_count = 0
    
    #Facts
    print('---------------------------------------------')
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
    print(f'Virus infected: {Virus.infected}')
    print(f'Average Genome: {average_genome}')
    print(f'Virus Genome: {Virus_genome}')
    print('---------------------------------------------')
    
    with open(file_name, 'a') as output:
        output.write(f'Generation: {generation}\n')
        output.write(f'Population: {len(population)}\n')
        output.write(f"Deaths: {deaths}\n")
        output.write(f'Births: {births}\n')
        if len(population) != 0:
            output.write(f'Net Growth: {(births - deaths)/len(population)}%\n')
        else:
            output.write("Net Growth: -100%\n")
        output.write(f'Food: {food}\n')
        output.write(f'Temperature: {temperature}\n')
        output.write(f'Infected: {Virus.infected}\n')
        output.write(f'Average Genome: {average_genome}\n')
        output.write(f'Virus Genome: {Virus_genome}\n')
        if event_done != "":
            output.write(f'Event: {event_done}\n')
        output.write('---------------------------------------------\n')
        if len(population) == 0:
            output.write("EVERY THING DIED\n")
        output.close()
    
    with open(file_name_raw, 'a') as output:
        output.write(f'{generation}\n')
        output.write(f'{len(population)}\n')
        output.write(f"{deaths}\n")
        output.write(f'{births}\n')
        if len(population) != 0:
            output.write(f'{(births - deaths)/len(population)}%\n')
        else:
            output.write("-100%\n")
        output.write(f'{food}\n')
        output.write(f'{temperature}\n')
        output.write(f'{Virus.infected}\n')
        output.write(f'{average_genome[0]}\n')
        output.write(f'{average_genome[1]}\n')
        output.write(f'{average_genome[2]}\n')
        output.write(f'{average_genome[3]}\n')
        output.write(f'{average_genome[4]}\n')
        output.write(f'{average_genome[5]}\n')
        output.write(f'{average_genome[6]}\n')
        output.close()
    
    if len(population) == 0:
        print("EVERY THING DIED")
        break
