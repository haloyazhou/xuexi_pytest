import pytest

'''
笛卡尔积
'''
@pytest.mark.parametrize("x", [0, -1, 2])
@pytest.mark.parametrize("y", [0, -2, 3])
def test_func(x, y):
    print("测试组合x->%s,y->%s"%(x, y))

    c = x+y
    expect = 100
    assert c < 10

def test_2():
    a = "2+4"
    assert eval(a) == 6