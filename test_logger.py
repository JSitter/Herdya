import pytest
from logger import Logger

# def test_write_metadata():
#     '''should create file with metadata'''
#     # file = open("./logs/logging", 'w')
#     # file.write("Hellow Worldz")
#     # file.close()
#     log = Logger("test.log")
#     log.write_metadata("100", ".5", "Ebola", ".5", ".5")

#     file = open("./logs/test.log", 'r')
#     line_one = file.readline()
#     file.close()
#     assert line_one == "100\t.5\tEbola\t.5\t.5\n"
    
# def test_log_interaction():
#     '''should add interaction to log'''
#     log = Logger("test.log")
#     log.log_interaction(get, "person2", "did infect", "person 2 vacc", "person2 sick")
#     file = open('./logs/test.log', 'r')

    #this needs to verify that log_interaction appends to end of file
    # first_line = file.readline()
    # first_line = file.readline()
    # file.close()
    # assert first_line == "person1\tperson2\tdid infect\tperson 2 vacc\tperson2 sick\n"

def test_log_infection_survival():
    ''' should log infection_survival '''
    log = Logger("test.log")
    log.log_infection_survival("person", True)
    file = open("./logs/test.log", "r")
    output = file.readline(2)
    file.close();
    print(output)

def test_log_time_step():
    '''should log time step'''
    log = Logger("test.log")
    log.log_time_step(1)
    file = open('./logs/test.log', 'r')
    
