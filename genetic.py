import random

def fitness(individ):
    i = 0
    for m in individ:
        if m == 0:
            i += 1
    return i

def selection(pop):
    chosen = []
    for i in range(len(pop)):
        aspirants = random.sample(pop, 3)
        macs = max(aspirants, key=fitness)
        chosen.append(macs[:])
    return chosen

def crossover(offspring):
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.7:
            child1[50:100], child2[50:100]=child2[50:100], child1[50:100]

def mutate(offspring):
    for mut in offspring:
        if random.random() < 0.3:
            for i in range(len(mut)):
                if random.random() < 0.05:
                    mut[i] = type(mut[i])(not mut[i])

def gen_individ():
    ind = []
    for s in range(100):
        ind.append(random.randint(0, 1))
    return ind

def gen_pop():
    pop = []
    for s in range(300):
        pop.append(gen_individ())
    return pop

gen = 0
popul = gen_pop()
print("Количество особей = %i "% len(popul))
fits = []
for k in popul:
    fits.append(fitness(k))
print("Лучшее качество особи = %i"% max(fits))
while(max(fits) < 100 and gen < 100):
    gen += 1
    offspring = []
    offspring = selection(popul)
    crossover(offspring)
    mutate(offspring)
    popul.clear()
    popul[:] = offspring
    fits.clear()
    for k in popul:
        fits.append(fitness(k))
print("Количество особей = %i "% len(popul))
print("Лучшее качество особи в конце = %i"% max(fits))
print("Поколение : %i"%gen)