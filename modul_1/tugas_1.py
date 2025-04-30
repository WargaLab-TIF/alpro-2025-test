import sys
import os
import pytest

# Menambahkan path modul-1 ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../modul-1')))

from tugas_1 import hitung_luas_lingkaran

def test_hitung_luas_lingkaran():
    assert hitung_luas_lingkaran(7) == 153.93804002589985
    assert hitung_luas_lingkaran(0) == 0.0
    assert hitung_luas_lingkaran(1) == 3.141592653589793
