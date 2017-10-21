import os
from simulation import Simulation

def test_simulation_instance():
    ''' test that simuation can be instantiated '''
    assert Simulation(1000, .2,"cat", .5, 1.2, 1)



def test_sim():
    os.system('python3 ./simulation.py 1000 .2 cat .5 1.2')


def test_sim_pop():
    sim = Simulation(10000, .2,"cat", .5, 1.2, 1)
    assert len(sim.population) == 10000