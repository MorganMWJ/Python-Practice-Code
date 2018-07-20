from string import ascii_uppercase
import random
#Genetic Algorithm

def setup(numberInPopulation, wordToFind):
    pop = []
    for i in range(numberInPopulation):
        pop.append(''.join(random.choice(ascii_uppercase+' ') for n in range(len(wordToFind))))
    return [(p,0) for p in pop]

def calcFitness(element, wordToFind):
    lettersInCorrectPosition = 0
    for i in range(len(wordToFind)):
        if element[i]==wordToFind[i]:
            lettersInCorrectPosition += 1
    return (lettersInCorrectPosition/float(len(wordToFind)))**4
    #power of 2 or 4 because exponential fitness function reduced run time
    #makes those with only one character better have a much higher fitness

#roulette wheel selection, return only the chromosones
def getParentRWS(population):
    #sum the fitnesses
    S = sum([p[1] for p in population])
    #get random number between 0 and sum
    r = random.uniform(0.0,S)
    #start from th etop of the population, keep adding fitnesses to the partial sum until P>S
    P = 0
    for e in population:
        P += e[1]
        #individual/element for which P exceeds S is chosen
        if P>r:
            return e[0]

#accept-reject, return only the chromosones
def getParentAR(population):
    while(True):
        #pick random individual
        individual = random.choice(population)
        #accept if random value is less than individuals fitness
        if random.uniform(0.0,1.0) <= individual[1]:
            return individual[0]

def crossover(parent1, parent2):
    #take 1st half of genes from 1st parent & 2nd half from 2nd parent
    return parent1[:(len(parent1)//2)] + parent2[(len(parent2)//2):]

def mutation(element, mutationRate):
    #chance to mutate each of the chromosones
    for i in range(len(element)):
        if random.randint(1,100)/float(100) <= mutationRate:
            element = element[:i] + random.choice(ascii_uppercase+' ') + element[i+1:]
    return element
    
    
def testPrint(population, generation):
    currentBest = ("",0)
    sumFitness = 0.0
    for p in population:
        print(p[0] + ' => ' + str(p[1]))
        sumFitness += p[1]
        if p[1] > currentBest[1]:
            currentBest = (p[0],p[1])
    print("\tBest of generation " + str(generation) + ":\n\t" + currentBest[0] + ' => ' + str(currentBest[1]))
    averageFitness = (sumFitness/len(population))*100
    print("\tAverage Fitness: %.2f%%" % averageFitness)
    return currentBest

WORD_TO_FIND = input("Enter the string to evelove[ascii_uppercase & whitespace ONLY]:\n")
POPULATION_SIZE = int(input("Enter the population size[integer]:\n"))
MUTATION_RATE = float(input("Enter the mutation rate[decimal between 0-1]:\n"))

population = setup(POPULATION_SIZE, WORD_TO_FIND)
generation = 1

found = False
while(found==False):
    #calculate fitness
    population = [(p[0],calcFitness(p[0],WORD_TO_FIND)) for p in population]
    bestOfGeneration = testPrint(population,generation)

    if bestOfGeneration[1] == 1:
        input("\tSolution Found, Enter to End...")
        found = True
    else:
        newPopluation = []
        for i in range(POPULATION_SIZE//2):
            #pick two parent randomly (higher chance if higer level of fitness)
            p1 = getParentAR(population)
            p2 = getParentAR(population)
            #crossover
            newElement = crossover(p1,p2)
            #mutation
            newElement = mutation(newElement,MUTATION_RATE)
            #add to new population
            newPopluation.append((newElement,0))
        population = newPopluation
        generation += 1
