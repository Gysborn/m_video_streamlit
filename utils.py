import pandas
from openpyxl.workbook import Workbook


def converter(path):
    pandas.read_json(path, encoding='windows-1251').to_excel("output/output.xlsx")
