from xpinyin import Pinyin
import unicodedata

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 4


unit2_1_3 = ('将来 保卫 禾苗 梦想 排队 蓝色 乘客 军队 观察 窗户 假装 放假 吸引 注意 掌声 金黄 远近 熟悉 关闭 丰富 泼水 清泉 '
          '懂得 好似 休闲 富有 召唤 呼唤 群众 北极 慌张 慌忙 拥挤 团结 结实 冰区 待遇 发觉 充数 齐全 排场 编号 演员 鼓励 '
          '继承 改成 温暖 映照 辽阔 摔倒 叔叔 帽子 报纸 盼望 迎接 借给 握手 命令 惊喜 学识 尽力 戏班 起航 奇怪 帘子 谈论 '
          '糟糕 另外')
unit4_1_3 = ('绿油油 乘风破浪 一本正经 引人注目 成群结队')

# unit_8_ = ('球场 拍球 羽毛 跳远 跳动 跳绳 黑板 板报 踢球 运动')

# unit_9_10_13 = ('汉字 汉语 甲鱼 甲虫 骨头 标志 标准 推行 推动 笑容 面容 容易 轻易 伯父 伯母 酒店 酒会 语气 话语 古代 代表 周边 '
#                 '周围 宋朝 互相 相同 相信 相反 称呼 名称 会议 议论 时刻 立刻 冲洗 冲茶 时装 化装 至今 至于 大哥 踩水 喊叫 呼喊 '
#                 '妹妹 兄妹 长短 粗壮 粗心 紧张 松紧')
# t_unit_9_13 = ('甲骨文 取长补短 粗枝大叶 安安')

word_2 = ('盛产 月份 秋季 暗红 吃够 制作 架子 成熟 好客 小镇 挺满 石桥 桥洞 摆满 拔出 油菜 露珠 丝绸 安静 欢闹 热情 安安 岸岸 按按 暗暗')
word_4 = ('葡萄沟 五光十色')

error_2_words = ('温暖 休闲 乘客 拥挤 发觉 鼓励 懂得 待遇 掌声 掌握 清泉 映照 摔倒 召唤 呼唤 惊慌 充数 起航 熟悉 盛产 制作 停止 '
                 '安安 岸岸 按按')
error_4_words = ('乘风破浪 掩耳盗铃 装腔作势 绿油油')


def split_twice(pinyin):
    for e in zip(*[iter(list(pinyin))] * 5):
        print('\t'.join(e))


def split_four(pinyin):
    for e in zip(*[iter(list(pinyin))] * 2):
        print('\t\t'.join(e))


def print_unicode(chars):
    for char in chars:
        unicodedata.name(char)
        print(char, hex(ord(char)))


if __name__ == '__main__':
    # print(len(error_2_words.split(' ')))
    p = Pinyin()
    out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in set(error_4_words.split(' '))]
    split_four(out)
    # split_twice(out)
    # print_unicode(['应', '担'])
