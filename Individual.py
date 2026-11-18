
import random

class Individual:
    def __init__(self, chromosome, items, capacity):
        self.chromosome = chromosome
        self.items = items
        self.capacity = capacity
        self.fitness = self.cal_fitness()

    @staticmethod
    def create_gnome(size):
        return [random.choice('01') for _ in range(size)]

    def cal_fitness(self):
        weight = 0
        value = 0

        for gene, (item_weight, item_value) in zip(self.chromosome, self.items):
            if gene == '1':
                weight += item_weight
                value += item_value

        if weight > self.capacity:
            return -1

        return value

    def mate(self, parent2):
        child = []

        for gene1, gene2 in zip(self.chromosome, parent2.chromosome):
            chance = random.random()

            if chance < 0.45:
                child.append(gene1)
            elif chance < 0.90:
                child.append(gene2)
            else:
                child.append(random.choice('01'))

        return Individual(child, self.items, self.capacity)
