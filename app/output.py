import sys

from datetime import datetime
from unittest import TestCase
from kousuan import KouSuan

__author__ = 'hisehyin'
__datetime__ = '15/12/25 下午4:46'


class Table:
    @staticmethod
    def kousuan():
        questions = KouSuan.gen_kousuan_questions(110, 100)
        for e in zip(*[iter(set(questions))] * 5):
            print('\t'.join(e))

    @staticmethod
    def shushi():
        questions = KouSuan.gen_add_sub_questions(total=24, max_=1000, add_carry=True, sub_carry=True)
        for e in zip(*[iter(set(questions))] * 4):
            print('\t'.join(e))

if __name__ == '__main__':
    args = sys.argv[1:]
    if '-kousuan' in args:
        Table.kousuan()
    elif '-shushi' in args:
        Table.shushi()


class Test(TestCase):
    def setUp(self):
        self.start = datetime.now()

    def tearDown(self):
        print(datetime.now() - self.start)

    def test_table_kousuan(self):
        Table.kousuan()

    def test_shushi(self):
        Table.shushi()
