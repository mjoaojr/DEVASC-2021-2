from loadcsv import load_csv
import pytest
from loadcsv import load_csv

def test_file_exist ():
    with pytest.raises (FileNotFoundError):
        alunos = load_csv ("eca.csv")

def test_empty_file ():
    alunos = load_csv ("testes/teste1.csv")
    assert len(alunos) == 0

def test_load_file ():
    alunos = load_csv ("testes/teste2.csv")
    assert alunos[0]['Nome'] == "João"
    assert alunos[0]['Av1'] == 8.0
    assert alunos[0]['Av2'] == 7.0