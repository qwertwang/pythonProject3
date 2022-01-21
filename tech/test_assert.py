import pytest

def test_1():
    assert 2+4 == 8

def test_2():
    print('测试2')

if __name__ == '__main__':
    pytest.main()