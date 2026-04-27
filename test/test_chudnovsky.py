import pytest
from mpmath import mp

from ..chudnovsky import _mpf_fixed_length, chudnovsky

def test__mpf_fixed_length():
    mp.dps = 4*2
    assert _mpf_fixed_length(mp.mpf("3.140"), 4) == mp.mpf("3.14")
    mp.dps = 5*2
    assert _mpf_fixed_length(mp.mpf("3.1400"), 5) == mp.mpf("3.140")

    mp.dps = 10*2
    assert _mpf_fixed_length(mp.mpf("3.141592653"), 8) == mp.mpf("3.14159265")
    mp.dps = 25*2
    assert _mpf_fixed_length(mp.mpf("3.141592653589793238462643"), 23) == mp.mpf("3.14159265358979323846264")


def test_chudnovsky_invalid_input():
    with pytest.raises(ValueError, match="Error: <n> must be integer and greater than 0"):
        chudnovsky(0)

    with pytest.raises(ValueError, match="Error: <n> must be integer and greater than 0"):
        chudnovsky(-1)

def test_chudnovsky_known_values():
    assert chudnovsky(10) == mp.mpf("3.1415926535")
    assert chudnovsky(23) == mp.mpf("3.14159265358979323846264")

def test_chudnovsky_length():
    assert len(str(chudnovsky(10))) == 10+2 # + point and newline
    assert len(str(chudnovsky(10))) == 10+2 # + point and newline
