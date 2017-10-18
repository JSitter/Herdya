import pytest
import logger

def test_write_metadata():
    '''should create file with metadata'''
    file = open("./logs/logging", 'w')
    file.write("Hellow Worldz")
    file.close()
def test_log_interaction():
    pass