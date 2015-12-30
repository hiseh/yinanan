from openpyxl import Workbook
from datetime import datetime
from unittest import TestCase
from app.kousuan import KouSuan

__author__ = 'hisehyin'
__datetime__ = '15/12/25 下午4:46'


class Excel:
    @staticmethod
    def grouped(iterable, n):
            return zip(*[iter(iterable)] * n)

    @staticmethod
    def output(file_path, questions):
        """
        输出成excel
        :param file_path:
        :param questions:
        :return:
        """
        wb = Workbook()
        ws = wb.create_sheet(title='questions')
        for i, e in enumerate(Excel.grouped(questions, 4)):
            for c, q in enumerate(e):
                ws['{column}{line}'.format(column=''.join(chr(65 + c)), line=i + 1)] = q

        return wb.save(filename=file_path)


class Test(TestCase):
    def setUp(self):
        self.start = datetime.now()

    def tearDown(self):
        print(datetime.now() - self.start)

    def test_excel_output(self):
        result = Excel.output('/Users/hisehyin/temp/an.xlsx', KouSuan.gen_add_sub_questions(1000, 20, 10, 0, True, False))
        print(result)
