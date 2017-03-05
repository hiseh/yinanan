import xpinyin

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 4


twice_words = ('意思 意见 思考 思念 教室 教师 室内 室外 直尺 尺寸 道理 理想 理发 养病 养育 培养 良好 优良 字典 典礼 登山 登记 总是 '
               '总结 总数 答题 回答 读书 朗读 造纸 造句 流血 心血 瓦片 砖瓦 热血 炎热 清凉 冰凉 学校 校园 拥抱 怀抱 抚摸 摸底 批评 '
               '批发 评语 评论 责任 责备 责怪 水井 井口 第一 门第 停止 停车 痛苦 痛心 痛快 孩子 男孩 沉思 沉没 沉着')
four_words = ('一声不响 一言不发 一声不吭 一丝不苟 登门求教 沉甸甸 走走停停')


def split_twice(pinyin):
    for e in zip(*[iter(set(pinyin))] * 5):
        print('\t'.join(e))


def split_four(pinyin):
    for e in zip(*[iter(set(pinyin))] * 2):
        print('\t\t'.join(e))


if __name__ == '__main__':
    p = xpinyin.Pinyin()
    out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in four_words.split(' ')]
    split_four(out)
