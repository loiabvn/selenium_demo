# Selenium + python Unitest (pytest)
# Execute command: pytest demo/demo_4_3.py --html=report.html -s
import pytest
from demo.BaseClass import BaseClass


class TestClass(BaseClass):
    @classmethod
    def setup_class(cls):
        print("\n===== BEGIN =====")
        print("Setup class: {} execution".format(cls.__name__))

    @classmethod
    def teardown_class(cls):
        print("\nTeardown class: {} execution".format(cls.__name__))
        print("===== END =====")

    def setup_method(self, method):
        print("\n\tsetup method: {}".format(method.__name__))

    def teardown_method(self, method):
        print("\tteardown method: {}".format(method.__name__))

    @pytest.fixture()
    def data_ok(self):
        print('\tsetup data_ok')
        data = ['username_correct', 'password_correct']
        yield data
        print('\tteardown data_ok')

    @pytest.fixture()
    def data_fail(self):
        print('\tsetup data_fail')
        data = ['username_incorrect', 'password_incorrect']
        yield data
        print('\tteardown data_fail')

    def test_tc1(self, data_ok):
        print('\ttc_content_1', data_ok)
        logger = self.getLogger()
        logger.info(data_ok)
        assert True

    def test_tc2(self, data_fail):
        print('\ttc_content_2', data_fail)
        logger = self.getLogger()
        logger.info(data_fail)
        assert True

    def test_tc3(self, data_fail):
        print('\ttc_content_3', data_fail)
        logger = self.getLogger()
        logger.info(data_fail)
        assert 'Hi' == 'Hello', "Test failed because strings do not match"
