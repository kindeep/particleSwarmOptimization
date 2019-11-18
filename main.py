from pso import *
TEST_SEED = np.random.randint(1, 999999999, 1)
res1 = Pso(
    w=float(input("Enter inertia component: ")),
    c1=float(input("Enter c1: ")),
    c2=float(input("Enter c2: ")),
    dim=int(input("Enter num of dimensions: ")),
    swarm_size=int(input("Enter swarm size: ")),
    seed=int(input("Enter random number seed: ")),
    num_iterations=int(input("Enter number of iterations: "))
).determine_min()

print("\n===========\nSolution: {}\n===========\n".format(res1))
