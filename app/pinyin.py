from xpinyin import Pinyin

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 4


twice_words = ('轻快 轻松 轻风 口哨 哨声 树梢 眉梢 树枝 枝头 交换 变换 支出 支持 '
               '除法 消除 害虫 伤害 晴天 湖水 湖面 安静 平静 宁静 '
               '姑娘 新娘 朗读 晴朗 狠心 狠命 讨论 论文 创造 创伤 开创')
four_words = ('悄悄话 静悄悄 晴空万里 尹悦涵')


def split_twice(pinyin):
    for e in zip(*[iter(set(pinyin))] * 5):
        print('\t'.join(e))


def split_four(pinyin):
    for e in zip(*[iter(set(pinyin))] * 2):
        print('\t\t'.join(e))


if __name__ == '__main__':
    p = Pinyin()
    out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in four_words.split(' ')]
    split_four(out)
    # out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in twice_words.split(' ')]
    # split_twice(out)
