import pytest
import allure

@allure.feature("1111模块")
class Test_ad():
    @allure.title("parmetrize模块")
    @pytest.mark.parametrize("test_input,expect",
                             [
                                 ({"user": "test", "pws": "1233"}, {"code":0, "msg":""}),
                                 ("2+4", 6),
                                 ("6*9", 54),
                             ])
    def test_demo(test_input, expect):
        assert eval(test_input) == expect


    @allure.title("3+5")
    def test_1(self):
        a = "3+5"
        assert eval(a) == 8

    @allure.title("2+43")
    def test_2(self):
        a = "2+4"
        assert eval(a) == 6
    @allure.title("2+42")
    def test_4(self):
        a = "6*9"
        assert eval(a) == 54
    @allure.title("2+41")
    def test_41(self):
        a = "6*9"
        assert eval(a) == 54