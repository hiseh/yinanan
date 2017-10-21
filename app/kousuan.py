import re
from datetime import datetime
from random import randint
from unittest import TestCase
from enum import IntEnum

__author__ = 'hisehyin'
__datetime__ = '15/12/25 上午10:50'


OPTION_SIGN = {0: '+', 1: '-', 2: '*', 3: '/'}

OPTION_PRINT = {'+': ' + ', '-': ' - ', '*': ' × ', '/': ' ÷ '}


class KouSuan:
    @staticmethod
    def gen_kousuan_questions(total, max_):
        """
        口算题，加减乘除
        :param total: 
        :param min_0: 
        :return: 
        """
        questions = 0
        regex = re.compile(r'\D')
        while questions < total:
            option = OPTION_SIGN[randint(0, 3)]
            if option == '*':
                question = '{num1}{option}{num2}'.format(num1=randint(0, 9),
                                                         option=option,
                                                         num2=randint(0, 9))
            elif option == '/':
                question = '{num1}{option}{num2}'.format(num1=randint(0, max_),
                                                         option=option,
                                                         num2=randint(1, 9))
            else:
                question = '{num1}{option}{num2}'.format(num1=randint(0, max_),
                                                         option=option,
                                                         num2=randint(0, max_))
            result = eval(question)
            if 0 <= result < max_ + 15:
                if option == '/' and not 1 < result < 10:
                    continue
                elif option == '*' and result < 10:
                    continue

                questions += 1
                option_print = OPTION_PRINT[str(option)]
                question = regex.sub(option_print, question)
                yield question + ' ='

    @staticmethod
    def gen_multiplication_division(total, max_arg1, max_arg2, min_=1, min_arg1=1, min_arg2=1):
        """
        生成乘除法计算题
        :param total: 题目总数
        :param max_arg1: 第一位最大运算数
        :param max_arg2: 第2位最大运算数
        :param min_arg1: 第一位最小运算数
        :param min_arg2: 第2位最小运算数
        :param min_: 结果下限
        """
        questions = 0
        regex = re.compile(r'\D')
        while questions < total:
            option = OPTION_SIGN[randint(2, 3)]
            if randint(1, 100) & 1 == 0:
                question = '{num1}{option}{num2}'.format(num1=randint(min_arg1, max_arg1),
                                                         option='*',
                                                         num2=randint(min_arg2, max_arg2))
            else:
                question = '{num1}{option}{num2}'.format(num1=randint(min_arg1, max_arg1),
                                                         option='/',
                                                         num2=randint(min_arg2, max_arg2))

            result = eval(question)
            if min_ <= result:
                questions += 1
                option_print = OPTION_PRINT[str(option)]
                question = regex.sub(option_print, question)
                yield question + ' ='

    @staticmethod
    def gen_add_sub_questions(total, max_, min_=0, three_element_percent=0, add_carry=False, sub_carry=False):
        """
        生成加减计算题
        :param total: 题目总数
        :param max_: 运算上限,例如20以内加减法
        :param min_: 运算下限
        :param three_element_percent: 三位运算比重
        :param add_carry: 是否允许进位加
        :param sub_carry: 是否允许借位减
        :return: generator
        """
        element_limit = 3 if three_element_percent > 0 else 2
        questions = 0
        while questions < total:
            elements = [randint(0, max_) for _ in range(element_limit)]
            question = ''
            for i, e in enumerate(elements):
                option = ' + ' if randint(0, 1) == 1 else ' - '
                question += str(e)
                if i < len(elements) - 1:
                    question += option
                    if (not sub_carry) and ('-' in option) and (e % 10 < elements[i + 1] % 10):
                        break
                    if (not add_carry) and ('+' in option) and (e % 10 + elements[i + 1] % 10 >= 10):
                        break
                else:
                    if 0 <= eval(question) <= max_:
                        if ('+' in question) and eval(question) < min_:
                            continue
                        yield question + ' = '
                        questions += 1

    @staticmethod
    def gen_3_questions(total, max_1, max_2):
        """
        乘除法计算题
        :param total:
        :param max_1:
        :param max_2:
        :return:
        """
        questions = 0
        pass


class Test(TestCase):
    def setUp(self):
        self.start = datetime.now()
        self.total = 100
        self.max = 100

    def tearDown(self):
        print(datetime.now() - self.start)

    # def test_simple_question(self):
    #     result = KouSuan.gen_add_sub_questions(self.total, 1000, 10, 0, True, True)
    #     for i, e in enumerate(result):
    #         print(e)

    # def test_kousuan(self):
    #     result = KouSuan.gen_kousuan_questions(20, 100)
    #     for i, e in enumerate(result):
    #         print(i, e)
    
    def test_gen_multiplication_division(self):
        result = KouSuan.gen_multiplication_division(total=200, max_arg1=99, max_arg2=10, min_arg1=20,  min_arg2=3, min_=10)
        for e in zip(*[result] * 5):
            print('\t'.join(e))
