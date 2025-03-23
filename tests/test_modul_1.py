import pytest
from ../modul_1.tugas_1 import hitung_luas_lingkaran

def test_hitung_luas_lingkaran():
    assert hitung_luas_lingkaran(7) == 153.93804002589985
    assert hitung_luas_lingkaran(0) == 0.0
    assert hitung_luas_lingkaran(1) == 3.141592653589793
