import pytest
from person import Person

def test_did_survive_infection():
    pat = Person("pat", False, {'mortality':.5})
    avg = 0.0
    for i in range(100):
        avg += pat.did_survive_infection()


    assert (avg / 100) >.4 and (avg/100 < .6)