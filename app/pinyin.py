from xpinyin import Pinyin
import unicodedata

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 4


# unit_1_2 = ('意思 意见 思考 思念 教室 教师 室内 室外 直尺 尺寸 道理 理想 理发 养病 养育 培养 良好 优良 字典 典礼 登山 登记 总是 '
#             '总结 总数 答题 回答 读书 朗读 造纸 造句 流血 心血 瓦片 砖瓦 热血 炎热 清凉 冰凉 学校 校园 拥抱 怀抱 抚摸 摸底 批评 '
#             '批发 评语 评论 责任 责备 责怪 水井 井口 第一 门第 停止 停车 痛苦 痛心 痛快 孩子 男孩 沉思 沉没 沉着')
# unit_1_2 = ('一声不吭 一言不发 一声不响 一丝不苟 登门求教 沉甸甸 走走停停')
# unit_3_4 = ('轻快 轻松 轻风 口哨 哨声 树梢 眉梢 树枝 枝头 交换 变换 支出 支持 除法 消除 害虫 伤害 晴天 湖水 湖面 安静 平静 宁静 '
#             '姑娘 新娘 朗读 晴朗 狠心 狠命 讨论 论文 创造 创伤 开创')
# unit_3_4 = ('悄悄话 静悄悄 晴空万里')
 #
twice_words = ('')
four_words = ('')


def split_twice(pinyin):
    for e in zip(*[iter(set(pinyin))] * 5):
        print('\t'.join(e))


def split_four(pinyin):
    for e in zip(*[iter(set(pinyin))] * 2):
        print('\t\t'.join(e))


def print_unicode(chars):
    for char in chars:
        unicodedata.name(char)
        print(char, hex(ord(char)))


if __name__ == '__main__':
    # print(len(twice_words.split(' ')))
    p = Pinyin()
    # out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in four_words.split(' ')]
    # split_four(out)
    out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in twice_words.split(' ')]
    split_twice(out)
    # print_unicode(['拥', ])
