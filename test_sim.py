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

def test_sim_continuation():
    sim = Simulation(1, .2, "cat", .5, .5)
    sim.population = [getUnVacPerson(1)]
    assert sim._simulation_should_continue()
    sim.population = [getVacPerson(1)]
    assert not sim._simulation_should_continue()
    sim.population = [getDeadPerson(1)]
    assert not sim._simulation_should_continue()

def test_sim():
    sim = Simulation(10000, .2, "cat", .5, .5)
    sim.run()
    
def getUnVacPerson(name):
    from person import Person
    return Person(name, False)

def getVacPerson(name):
    from person import Person
    return Person(name, True)

def getDeadPerson(name):
    from person import Person
    from virus import Virus
    patient = Person(name, False, Virus("cat", 1, 1))
    patient.did_survive_infection()
    return patient
