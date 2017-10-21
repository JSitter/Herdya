import pytest
from person import Person
from virus import Virus

def test_did_survive_infection():
    num = 0
    vir = Virus("cat", .5, 12)
    for i in range(10000):
        pat = Person("pat", False, vir)
        pat.did_survive_infection()
        if pat.is_alive:
            num += 1
    assert num > 4900 and num < 5100

