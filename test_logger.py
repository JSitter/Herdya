import pytest
import logger

def test_write_metadata():
    '''should create file with metadata'''
    file = open("./logs/logging", 'w')
    file.write("Hellow Worldz")
    file.close()

    file = open("./logs/logging", 'r')
    line_one = file.readline()
    file.close()
    assert line_one == "Hellow Worldz"
def test_log_interaction():
    pass