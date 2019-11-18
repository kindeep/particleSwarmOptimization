import numpy as np
import math

LOWER_BOUND = -5.12
UPPER_BOUND = 5.12


def check_vector_bound(x):
    for i in x:
        if i >= UPPER_BOUND or i <= LOWER_BOUND:
            return False
    return True


def rast_func(x):
    return 10 * len(x) + np.sum((x ** 2 - np.array([math.cos(2 * math.pi * xi) * 10 for xi in x])))


class Particle:
    def __init__(self, position, velocity, best, best_x):
        self.position = position
        self.velocity = velocity
        self.best = best
        self.best_x = best_x

    def __str__(self):
        return "Position: {0}, Velocity: {1}, Best: {2} at {3}".format(
            self.position, self.velocity, self.best, self.best_x)


class Pso:

    def __init__(self, w, c1, c2, dim, swarm_size, seed, num_iterations, debug_info=False):
        self.dim = dim
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.rng = np.random.default_rng(seed)
        self.neighbourhood_best = float("inf")
        self.neighbourhood_best_x = np.zeros(dim)
        self.swarm_size = swarm_size
        self.swarm = []
        self.num_iterations = num_iterations
        self.debug_info = debug_info

    def fitness(self, x):
        return rast_func(x)

    def update_neighbourhood_best(self):
        for particle in self.swarm:
            if particle.best < self.neighbourhood_best and check_vector_bound(particle.best_x):
                self.neighbourhood_best = particle.best
                self.neighbourhood_best_x = np.copy(particle.best_x)

    def initial_particle(self):
        pos = self.rng.uniform(LOWER_BOUND, UPPER_BOUND, self.dim)
        return Particle(position=pos, velocity=np.zeros(self.dim), best=self.fitness(pos), best_x=pos)

    def update_velocity(self, p: Particle):
        r1 = self.rng.uniform(0, 1, self.dim)
        r2 = self.rng.uniform(0, 1, self.dim)
        p.velocity = self.w * p.velocity + \
            self.c1 * r1 * (p.best_x - p.position) + \
            self.c2 * r2 * (self.neighbourhood_best_x - p.position)

    def determine_min(self):
        # Initialize particles randomoly
        for i in range(self.swarm_size):
            self.swarm.append(self.initial_particle())

        self.update_neighbourhood_best()

        self.print_positions()
        self.print_velocities()

        for iteration in range(self.num_iterations):
            for particle in self.swarm:
                # evaluate fitness
                curr_fitness = self.fitness(particle.position)
                # update personal best
                if curr_fitness < particle.best and check_vector_bound(particle.position):
                    particle.best = curr_fitness
                    particle.best_x = np.copy(particle.position)

            self.update_neighbourhood_best()
            # update velocity and position for swarm
            for p in self.swarm:
                self.update_velocity(p)
                p.position = p.position + p.velocity
            print("Iteration: {0} n..d_best: {1}".format(
                iteration, self.neighbourhood_best))
            self.print_positions()
            self.print_velocities()
        return self.neighbourhood_best, self.neighbourhood_best_x
        pass

    # Just prinitng methods
    def print_swarm(self):
        if self.debug_info:
            for p in self.swarm:
                print(p, end=" ; ")
            print()

    def print_positions(self):
        if self.debug_info:
            print("Positions: ", end="")
            for pr in self.swarm:
                print(pr.position, end=",")
            print()

    def print_velocities(self):
        if self.debug_info:
            print("Velocities: ", end="")
            for pr in self.swarm:
                print(pr.velocity, end=",")
            print()
