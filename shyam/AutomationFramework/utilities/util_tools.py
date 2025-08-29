import  openpyxl

class Utils:
    @staticmethod
    def read_excel_file(file_path,sheet_name):
        wb =openpyxl.load_workbook(file_path)
        sheet=wb[sheet_name]
        return sheet


if __name__=="__main__":
    obj=Utils()
    excel_data=obj.read_excel_file("hrm.xlsx","Sheet1")
