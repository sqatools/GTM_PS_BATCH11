import json
import openpyxl


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


if __name__ == '__main__':
    print("__name__:", __name__)
    obj = Utils()
    data = obj.read_json_file("sample_json_data.json")
    print(data)
    print(data['browser'])

    excel_data = obj.read_excel_data("sample.xlsx", sheet_name="Sheet1")
    print(excel_data['A1'].value)
    print(excel_data['A2'].value)
