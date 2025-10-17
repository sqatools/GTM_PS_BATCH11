import json
import os
import openpyxl
from datetime import datetime


class Utils:

    @staticmethod
    def read_json_file(file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data

    @staticmethod
    def read_excel_data(file_path, sheet_name):
        wb = openpyxl.load_workbook(file_path)
        sheet_name = wb[sheet_name]
        return sheet_name

    @staticmethod
    def get_unique_name():
        return datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

    @staticmethod
    def get_today_date():
        return datetime.now().strftime("%d_%m_%Y")

    def generate_screenshot_path(self):
        logs_path = os.path.join(os.getcwd(), "logs")
        today_date = self.get_today_date()
        today_folder_path = os.path.join(logs_path, today_date)
        images_path = os.path.join(today_folder_path, "images")
        if not os.path.exists(images_path):
            os.mkdir(images_path)

        image_file = f"{self.get_unique_name()}_element.png"
        image_file_path = os.path.join(images_path, image_file)
        return image_file_path


if __name__ == '__main__':
    print("__name__:", __name__)
    obj = Utils()
    data = obj.read_json_file("sample_json_data.json")
    print(data)
    print(data['browser'])

    excel_data = obj.read_excel_data("sample.xlsx", sheet_name="Sheet1")
    print(excel_data['A1'].value)
    print(excel_data['A2'].value)
