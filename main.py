
import random
from Individual import Individual

VALUES = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600,
          38, 48, 78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22,
          42, 50, 323, 514, 87, 73, 78, 15, 26, 78, 210, 36, 85,
          189, 274, 43, 33, 10, 19, 389, 312]

WEIGHTS = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3,
           8, 15, 42, 42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4,
           18, 56, 7, 29, 93, 44, 3, 86, 66, 31, 65, 0, 79, 20,
           65, 52, 13]

CAPACITY = 850
POPULATION_SIZE = 200
G_LIMIT = 300

def main():
    items = list(zip(WEIGHTS, VALUES))
    population = [Individual(Individual.create_gnome(len(items)), items, CAPACITY)
                  for _ in range(POPULATION_SIZE)]
    best = None
    unchanged = 0

    for generation in range(1, G_LIMIT + 1):
        population.sort(key=lambda x: x.fitness, reverse=True)
        current = population[0]

        if best is None or current.fitness > best.fitness:
            best = current
            unchanged = 0
        else:
            unchanged += 1

        if generation == 1 or generation % 10 == 0:
            print(f'Generation: {generation}  Best fitness: {best.fitness}')

        if unchanged >= 60:
            print('Stopped because the best answer did not improve for 60 generations.')
            break

        new_generation = population[:int(0.10 * POPULATION_SIZE)]

        for _ in range(POPULATION_SIZE - len(new_generation)):
            parent1 = random.choice(population[:int(0.50 * POPULATION_SIZE)])
            parent2 = random.choice(population[:int(0.50 * POPULATION_SIZE)])
            new_generation.append(parent1.mate(parent2))

        population = new_generation

    selected = [i for i, gene in enumerate(best.chromosome) if gene == '1']
    total_weight = sum(WEIGHTS[i] for i in selected)
    total_value = sum(VALUES[i] for i in selected)

    print('\nSelected items (1-based):', [i + 1 for i in selected])
    print('Chromosome:', ''.join(best.chromosome))
    print('Total weight:', total_weight)
    print('Total value:', total_value)
    print('Capacity:', CAPACITY)

if __name__ == '__main__':
    main()
