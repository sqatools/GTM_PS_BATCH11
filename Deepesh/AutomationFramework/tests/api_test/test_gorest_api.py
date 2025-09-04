import pytest
from ...api_objects.gorest.gorest_api_class import GorestAPI


class TestGorest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.goApi = GorestAPI()


    def test_get_all_entry_and_verify(self):
        res, st_code = self.goApi.get_all_object_details()
        assert st_code == 200