import pytest


@pytest.fixture(scope="class", autouse=True)
def setup_class(request):

    print("Setting up class")
    data = {"key": "value"}


    request.cls.data = data

    yield

    print("Tearing down class")




@pytest.mark.usefixtures("setup_class")
class TestExample:

    def test_case_1(self):
        assert self.data["key"] == "value"
        print("firts method")

    def test_case_2(self):
        assert isinstance(self.data, dict)
        print("second classs")
