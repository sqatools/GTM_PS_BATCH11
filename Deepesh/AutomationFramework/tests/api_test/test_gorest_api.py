import pytest
from ...api_objects.gorest.gorest_api_class import GorestAPI


class TestGorest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.goApi = GorestAPI()

    def test_get_all_entry_and_verify(self):
        res, st_code = self.goApi.get_all_object_details()
        assert st_code == 200


    def test_create_user_and_Verify(self):
        res, st_code = self.goApi.create_new_entry()
        assert st_code == 201