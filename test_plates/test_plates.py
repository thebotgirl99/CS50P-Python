from plates import is_valid

def main():
    test_len()
    test_ftwo()
    test_num()
    test_exp()

def test_len():
    assert is_valid("AARV22") == True
    assert is_valid("OUTATIME") == False

def test_ftwo():
    assert is_valid("cs50") == True
    assert is_valid("CS05") == False
    assert is_valid("O") == False
    assert is_valid("A453") == False
    assert is_valid("34AD") == False

def test_num():
    assert is_valid("AA34") == True
    assert is_valid("CS50P") == False
    assert is_valid("5as5as0as5s") == False
    assert is_valid("1505005545") == False

def test_exp():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3,14") == False

if __name__ == "__main__":
    main()