from datetime import datetime
from random import randint
from unittest import TestCase

__author__ = 'hisehyin'
__datetime__ = '15/12/25 上午10:50'


class KouSuan:
    @staticmethod
    def gen_add_sub_questions(total, upper_limit, three_element_percent=0, add_carry=False, sub_carry=False):
        """
        生成加减计算题
        :param total: 题目总数
        :param upper_limit: 运算上限,例如20以内加减法
        :param three_element_percent: 三位运算比重
        :param add_carry: 是否允许进位加
        :param sub_carry: 是否允许借位减
        :return: generator
        """
        element_limit = 3 if three_element_percent > 0 else 2
        questions = 0
        while questions < total:
            elements = [randint(0, upper_limit) for i in range(element_limit)]
            question = ''
            for i, e in enumerate(elements):
                option = ' + ' if randint(0, 1) == 1 else ' - '
                question += str(e)
                if i < len(elements) - 1:
                    question += option
                    if ('-' in option) and (e % 10 < elements[i + 1] % 10):
                        break
                else:
                    if 0 <= eval(question) <= 20:
                        yield question + ' = '
                        questions += 1


class Test(TestCase):
    def setUp(self):
        self.start = datetime.now()
        self.total = 100
        self.limit = 20

    def tearDown(self):
        print(datetime.now() - self.start)

    def test_simple_question(self):
        result = KouSuan.gen_add_sub_questions(self.total, self.limit, 0, True, False)
        for i, e in enumerate(result):
            print(e)

        # self.assertEqual(i, self.total - 1)
