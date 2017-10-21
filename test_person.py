import pytest
from person import Person
from virus import Virus

def test_did_survive_infection():
    avg = 0
    vir = Virus("cat", .5, 12)
    for i in range(10000):
        pat = Person("pat", False, vir)
        pat.did_survive_infection()
        if pat.is_alive:
            avg += 1
    assert avg > 4900 and avg < 5100

