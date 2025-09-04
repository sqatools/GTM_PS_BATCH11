from ...base.api_base import APIBase
from .gorest_api_data import *

class GorestAPI(APIBase):
    def __init__(self):
        super().__init__()


    def get_all_object_details(self):
        all_details_api = f"{api_path}/users"
        res_data, res_code = self.get_method(url=all_details_api, header=headers)
        return res_data, res_code



