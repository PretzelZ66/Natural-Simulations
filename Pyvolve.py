#pyvolve 1.2.1.6
import time, random
print('LOADING')


def pause(number):
    """Pauses the program temporarily, for breaking up sections of text, or dramatic effect, etc"""
    time.sleep(number)


def line(string):
    """Displays a string, then pauses the program, so the user can read it"""
    print(string)
    pause(1)

def avr_gen(the_list, gene_type):
    """Obtains the average genome of the population"""
    gene_check = 0
    average = 0
    if len(the_list) != 0:
        while len(the_list) != gene_check:
            addition = the_list[gene_check][gene_type]
            average += addition
            gene_check += 1
        average = average // len(the_list)
        return(average)
    return(0)

m = 1
r = 2
t = 10
d = 3
a = 3
s = 27
b = 1
age = 0
fed = 0
fatigue = 0
b_c = 0 #birth count
contaminated = False
population = []
offspring = []
breedable = []
average_genome = []
pop_template = [m, r, t, d, a, s, b, age, fed, fatigue, b_c, contaminated]

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
event_clock2 = 0
event_clock3 = 0

avr_m = 0
avr_r = 0
avr_t = 0
avr_d = 0
avr_a = 0
avr_s = 0
avr_b = 0

class Cassowary:
    infected = 0
    food = 0
    kill_chance = 5
    mutaion_chance = 1
    infectiousness = 10
    metabolism = 3
met_clock = Cassowary.metabolism

pause(1)
line('LOADED')
print('')
line('~~CUSTOMISABLE SIMULATION PARAMETERS~~')

line('WHAT WOULD YOU LIKE TO CALL THE RESULTS FILE?')
while True:
    try:
        file_name = input('>>> ')
        file_name_raw = file_name + '_raw.txt'
        file_name += '.txt'
        with open(file_name, 'x') as file:
            file.close()
            
        with open(file_name_raw, 'x') as file:
            file.close()
        break
    except FileExistsError:
        print("File Taken. Try again")

line('''WHAT PRESET WOULD YOU LIKE TO USE? DEFAULT(0), NUCLEAR PLAYGROUND(1),
   THERMONUCLEAR PLAYGROUND(2), VIRUS PLAYGROUND(3), EVENT MAYHEM(4), CUSTOM(OTHER_NUM)''')
while True:
    try:
        preset_type = int(input('>>> '))
        break
    except ValueError:
        print("Invalid number. Try again")

if preset_type == 0:
    #default
    start_pop = 50
    event_chance_cap = 100
    mutation_rate = 1
    default_mutation_rate = 1
    mutation_severity = 1
    infect_counter = 1
    secrets = False
    
elif preset_type == 1:
    #nuclear playground
    start_pop = 50
    event_chance_cap = 69
    mutation_rate = 100
    default_mutation_rate = 100
    mutation_severity = 5
    infect_counter = 1
    secrets = False

elif preset_type == 2:
    #thermonuclear playground
    start_pop = 50
    event_chance_cap = 49
    mutation_rate = 500
    default_mutation_rate = 500
    mutation_severity = 25
    infect_counter = 0
    secrets = False

elif preset_type == 3:
    #RapiVirus
    start_pop = 50
    event_chance_cap = 100
    mutation_rate = 1
    default_mutation_rate = 1
    mutation_severity = 1
    infect_counter = 50
    secrets = False

    Cassowary.kill_chance = 50
    Cassowary.mutaion_chance = 10
    Cassowary.infectiousness = 100
    Cassowary.metabolism = 20
    Cassowary.food = 1000
    secrets = False

elif preset_type == 4:
    #event mayhem
    start_pop = 50
    event_chance_cap = 0
    mutation_rate = 1
    default_mutation_rate = 1
    mutation_severity = 1
    infect_counter = 50
    secrets = True
    
else:
    line('WHAT WOULD YOU LIKE THE STARTING POPULATION TO BE?')
    while True:
        try:
            start_pop = int(input('>>> '))
            if start_pop <= 1:
                start_pop = 2
            break
        except ValueError:
            print("Invalid number. Try again")    

    line('WOULD YOU LIKE A LOW (3), MEDIUM (2), or HIGH (1) EVENT CHANCE?')
    while True:
        try:
            event_chance = int(input('1/2/3 >>> '))
            if event_chance > 0 and event_chance <= 3:
                event_chance_cap = event_chance
            else:
                event_chance_cap = 2
            event_chance_cap = event_chance_cap * 50
            break
        except ValueError:
            print("Invalid number. Try again")  
    
    line('WHAT WOULD YOU LIKE THE DEFAULT RADIATION LEVEL TO BE?')
    while True:
        try:
            mutation_rate = int(input('>>> '))
            default_mutation_rate = mutation_rate
            break
        except ValueError:
            print("Invalid number. Try again")

    line('WHAT WOULD YOU LIKE THE MUTATION SEVERITY TO BE?')
    while True:
        try:
            mutation_severity = int(input('>>> '))
            break
        except ValueError:
            print("Invalid number. Try again")
    

    line('HOW MANY CREATURES SHOULD START OUT WITH THE VIRUS?')
    while True:
        try:
            infect_counter = int(input('>>> '))
            break
        except ValueError:
            print("Invalid number. Try again")
    
    secrets = False
    
pop_gen_check = 0
while pop_gen_check != start_pop:
    if infect_counter != Cassowary.infected:
        contaminated = True
        Cassowary.infected += 1
    else:
        contaminated = False
    
    pop_template = [m, r, t, d, a, s, b, age, fed, fatigue, b_c, contaminated]
    population.append(pop_template)
    pop_gen_check += 1

Cassowary.food += Cassowary.infected * 10

line('~~SIMULATION PARAMETERS HAVE BEEN SET~~')

print('---------------------------------------------')

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

    #breedable assignment
    print('    Sorting Breedables From Unbreedables')
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
    
    #event clocks
    print('    Event Clocks')
    if event_clock1 > 0:
        event_clock1 -= 1
        if event_clock1 == 0:
            mutation_rate = default_mutation_rate
    if event_clock2 > 0:
        event_clock2 -= 1 
        temperature -= random.randint(1, 3) * temp_rate
    if event_clock3 > 0:
        event_clock3 -= 1
        print("Aftershock")
        death_check = 0
        while len(population) != death_check:
            death_number = random.randint(1, 400)
            if death_number == 13:
                if population[death_check][12] is True and breedable_count > 2:
                    del population[death_check]
                    death_check -= 1
                    deaths += 1
                    breedable_count -= 1
            death_check += 1
        
    #random events
    print('    Random Event Check')
    event_done = ''
    event_check = random.randint(0, event_chance_cap)
    if event_check == 0:
        event = random.randint(events, 7)
        if event == 0:
            event_done = 'ENVIRONMENTAL STABILITY LOWERED'
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
            event_done = 'MEDIUM LEVEL ADIATION HAZARD'
            mutation_rate += random.randint(4, 6)
            event_clock1 += random.randint(5, 15)
            
        elif event == 3:
            event_done = 'HIGH LEVEL RADIATION HAZARD'
            mutation_rate += random.randint(6, 8)
            event_clock1 += random.randint(10, 20)
            
        elif event == 4:
            event_done = 'VOLCANIC ERRUPTION'
            temp_max += random.randint(3, 5)
            temperature += random.randint(1, 3) * temp_rate
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 250)
                if death_number == 13:
                    if population[death_check][12] is True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
            event_clock2 += random.randint(2, 4)
                
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
		    if secrets == True:
				easter_egg = random.randint(0, 100)
			    if easter_egg = 19:
				    event_done = 'NEW CORONAVIRUS STRAIN'
			    else:
				    event_done = 'PLAGUE'
			else:
				event_done = 'PLAGUE'
				plague_check = 0
            while len(population) != plague_check:
                death_number = random.randint(0, 100)
                if death_number == 0:
                    population[plague_check][11] = True
                    plague_check += 1
                    
        elif event == 7:
            event_done = 'EARTHQUAKE'
            death_check = 0
            while len(population) != death_check:
                death_number = random.randint(1, 300)
                if death_number == 13:
                    if population[death_check][12] is True and breedable_count > 2:
                        del population[death_check]
                        death_check -= 1
                        deaths += 1
                        breedable_count -= 1
                death_check += 1
            event_clock3 += random.randint(1, 3)

            
        if secrets is True:
            event = random.randint(1, 1000000000000000000000000000000000) #1/1 Decillion
            if event == 679711511511111997114121:
                event_done = 'CASSOWARY RAID'
                death_check = 0
                while len(population) != death_check:
                    death_number = random.randint(1, 10)
                    if death_number == 6:
                        del population[death_check]
                        death_check -=1
                        deaths += 1
                    death_check += 1
        print(event_done)
        
    #temperature change
    print('    Temperature Change')
    
    temp_rate = 0.1 * temp_increase
    temp_boost = (random.randint(-5, 5) * 0.1)
    temp_rate += temp_boost
    naturilisation = random.randint(0, 50)

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
            temp_max += (random.randint(5, 20) * 0.1)
            temp_increase += 1
    
    #temperature deaths
    print('    Temperature Deaths')
    temp_check = 0
    for i in range(len(population)):
        if population[temp_check][2] < temperature or 0-population[temp_check][2] > temperature:
            del population[temp_check]
            deaths += 1
            temp_check -= 1
        temp_check += 1
    
    #fatigue down
    print('    Fatigue Counter Decrease')
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
    
    #starvation check
    print('    Starvation Check')
    starve_check = 0
    for x in range(len(population)):
        if population[starve_check][8] == 0:
            del population[starve_check]
            starve_check -= 1
            deaths += 1
        starve_check += 1
    
    #virus deaths
    print('    Virus Killing')
    Cassowary_check = 0
    for x in range(len(population)):
        Cassowary_chance = random.randint(1, 100)
        if Cassowary_chance <= Cassowary.kill_chance:
            del population[Cassowary_check]
            Cassowary_check -= 1
            deaths += 1
            Cassowary.food += random.randint(1, 3)
        Cassowary_check += 1
    
    #deaths
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
    
    #generation of offspring
    print('    Breeding Creatures')
    births = 0
    completed = 0
    past_completed = 0
    breedable1 = []
    breedable2 = []
    
    
    while len(population) != completed:
        breedable1 = []
        breedable2 = []
        while breedable1 == []:
            if completed >= len(population):
                break
            if population[completed][12] is True:
                breedable1 = population[completed]
                past_completed = completed
            completed += 1
        if completed >= len(population):
                break
        
        while breedable2 == []:
            if completed >= len(population):
                break
            if  population[completed][12] is True:
                breedable2 = population[completed]
                break
            completed += 1
            
        if completed >= len(population):
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
            
            if breedable1[11] is True or breedable2[11] is True:
                willinfect = random.randint(1, 100)
                if willinfect >= Cassowary.infectiousness:
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
        f_added = random.randint(1, 2)
        population[completed][9] = (f_added + population[completed][10])
        population[past_completed][9] = (f_added + population[past_completed][10])
        population[completed][10] += 1
        population[past_completed][10] += 1
        
        completed += 1
        
    #aging of population
    print('    Aging Of Population')
    age_check = 0
    while len(population) != age_check:
        population[age_check][7] += 1
        age_check += 1
    
    #hunger check
    print('    Hunger Check')
    hungry_check = 0
    for x in range(len(population)):
        population[hungry_check][8] -= 1
        hungry_check += 1
    
    #offspring added to population
    print('    Merging Offspring With Population')
    population.extend(offspring)
    
    #virus mutation
    print('    Virus Mutation')
    if Cassowary.mutaion_chance >= random.randint(1, 100):
        Cassowary_decider = random.randint(1, 4)
        change = random.randint(1, 2)
        if change == 2:
            change = -1
        
        if Cassowary_decider == 1:
            Cassowary.kill_chance += change
        elif Cassowary_decider == 2:
            Cassowary.mutaion_chance += change
        elif Cassowary_decider == 3:
            Cassowary.infectiousness +=  change
        elif Cassowary_decider == 4:
            Cassowary.metabolism += change
        
    #Obtain Average Genome
    print('    Obtaining Average Genome')
    avr_m = avr_gen(population, 0)
    avr_r = avr_gen(population, 1)
    avr_t = avr_gen(population, 2)
    avr_d = avr_gen(population, 3)
    avr_a = avr_gen(population, 4)
    avr_s = avr_gen(population, 5)
    avr_b = avr_gen(population, 6)

    average_genome = [avr_m, avr_r, avr_t, avr_d, avr_a, avr_s, avr_b]

    Cassowary_genome = [Cassowary.kill_chance, Cassowary.mutaion_chance, Cassowary.infectiousness, Cassowary.metabolism]

    #dead creatures converted to food.
    print('    Converting Corpses To Food')
    for x in range(deaths):
        if random.randint(1, 20) == 1:
            food += 1
            
    #virus curing
    print('    Handing Out Vaccines')
    for i in range(len(population)):
        if population[i][11] is True:
            if random.randint(1, 100) == 1:
                population[i][11] = False

    #virus feeding/deaths
    print('    Virus Feeding and Starving')
    if met_clock == 0:
        for i in range(len(population)):
            if population[i][11] is True:
                if Cassowary.food >= 1:
                    Cassowary.food -= 1
            elif Cassowary.food == 0:
                population[i][11] = False
        met_clock = Cassowary.metabolism
    else:
        met_clock -= 1
    
    #virus check
    print('    Diagnosing Coronavirus')
    Cassowary.infected = 0
    for i in range(len(population)):
        if population[i][11] is True:
            Cassowary.infected += 1
    
    #technical resets
    print('    Technical Resets')
    offspring = []
    generation += 1
    breedable_count = 0
    
    #facts
    print('---------------------------------------------')
    print(f'Generation: {generation}')
    print(f"Population: {len(population)}")
    print(f"Deaths: {deaths}")
    print(f"Births: {births}")
    if len(population) != 0:
        print(f"Net growth: {(births - deaths)/len(population)}%")
    else:
        print("Net growth: -100%")
    print(f'Food: {food}')
    print(f'Temperature: {temperature}')
    print(f'Virus Infected: {Cassowary.infected}')
    print(f'Average Genome: {average_genome}')
    print(f'Virus Genome: {Cassowary_genome}')
    print('---------------------------------------------')
    
    with open(file_name, 'a') as output:
        output.write(f'Generation: {generation}\n')
        output.write(f'Population: {len(population)}\n')
        output.write(f"Deaths: {deaths}\n")
        output.write(f'Births: {births}\n')
        if len(population) != 0:
            output.write(f'Net growth: {(births - deaths)/len(population)}%\n')
        else:
            output.write("Net growth: -100%\n")
        output.write(f'Food: {food}\n')
        output.write(f'Temperature: {temperature}\n')
        output.write(f'Infected: {Cassowary.infected}\n')
        output.write(f'Average Genome: {average_genome}\n')
        output.write(f'Virus Genome: {Cassowary_genome}\n')
        if event_done != "":
            output.write(f'Event: {event_done}\n')
        output.write('---------------------------------------------\n')
        if len(population) == 0:
            output.write("Every Thing Died\n")
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
        output.write(f'{Cassowary.infected}\n')
        output.write(f'{average_genome[0]}\n')
        output.write(f'{average_genome[1]}\n')
        output.write(f'{average_genome[2]}\n')
        output.write(f'{average_genome[3]}\n')
        output.write(f'{average_genome[4]}\n')
        output.write(f'{average_genome[5]}\n')
        output.write(f'{average_genome[6]}\n')
        output.close()
    
    if len(population) == 0:
        print("EVERYTHING DIED")
        break
