from pso import *
import csv

TEST_DIM = 30
NUM_ITER = 500

writer = csv.writer(open("tests.csv", mode="w"))

writer.writerow(["", "Test 1", "Test 2", "Test 3", "Test 4", "Random"])

for i in range(5):
    TEST_SEED = np.random.randint(1, 999999999, 1)
    res1 = Pso(
        w=0.729844,
        c1=1.496180,
        c2=1.496180,
        dim=TEST_DIM,
        swarm_size=30,
        seed=TEST_SEED,
        num_iterations=NUM_ITER
    ).determine_min()

    print("\n\n===========\n\nSolution: {}\n\n===========\n\n".format(res1))

    res2 = Pso(
        w=0.4,
        c1=1.2,
        c2=1.2,
        dim=TEST_DIM,
        swarm_size=30,
        seed=TEST_SEED,
        num_iterations=NUM_ITER
    ).determine_min()
    print("\n\n===========\nSolution: {} \n===========\n\n".format(res2))

    res3 = Pso(
        w=1.0,
        c1=2.0,
        c2=2.0,
        dim=TEST_DIM,
        swarm_size=30,
        seed=TEST_SEED,
        num_iterations=NUM_ITER
    ).determine_min()

    print("\n\n===========\nSolution: {} \n===========\n\n".format(res3))

    res4 = Pso(
        w=-1.0,
        c1=2.0,
        c2=2.0,
        dim=TEST_DIM,
        swarm_size=30,
        seed=TEST_SEED,
        num_iterations=NUM_ITER
    ).determine_min()

    print("\n\n===========\nSolution: {} \n===========\n\n".format(res4))

    random_best = float("inf")

    for _ in range(NUM_ITER):
        random_best = min(rast_func(np.random.uniform(-5.12, 5.12, TEST_DIM)),
                          random_best)

    writer.writerow([i, res1[0], res2[0], res3[0], res4[0], random_best])
