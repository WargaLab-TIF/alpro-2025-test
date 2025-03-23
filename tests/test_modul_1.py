import sys
import os
import pytest

# Menambahkan path modul-1 ke sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../modul-1')))

from tugas_1 import hitung_luas_lingkaran

def test_hitung_luas_lingkaran():
    try:
        assert hitung_luas_lingkaran(7) == 153.93804002589985, "\n\n❌ Jawaban Salah: Luas lingkaran dengan jari-jari 7 seharusnya 153.93804002589985\n"
        assert hitung_luas_lingkaran(0) == 0.0, "\n\n❌ Jawaban Salah: Luas lingkaran dengan jari-jari 0 seharusnya 0.0\n"
        assert hitung_luas_lingkaran(1) == 3.141592653589793, "\n\n❌ Jawaban Salah: Luas lingkaran dengan jari-jari 1 seharusnya 3.141592653589793\n"
    except AssertionError as e:
        pytest.fail(str(e), pytrace=True)
