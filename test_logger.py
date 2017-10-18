import pytest
from logger import Logger

def test_write_metadata():
    '''should create file with metadata'''
    # file = open("./logs/logging", 'w')
    # file.write("Hellow Worldz")
    # file.close()
    log = Logger("test.log")
    log.write_metadata("100", ".5", "Ebola", ".5", ".5")

    file = open("./logs/test.log", 'r')
    line_one = file.readline()
    file.close()
    assert line_one == "100\t.5\tEbola\t.5\t.5"
    
def test_log_interaction():
    pass