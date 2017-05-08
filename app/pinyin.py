from xpinyin import Pinyin
import unicodedata

__author__ = 'hiseh'
__datetime__ = 2017 / 3 / 4


# unit_1_7 = ('意思 意见 思考 思念 教室 教师 室内 室外 直尺 尺寸 道理 理想 理发 养病 养育 培养 良好 优良 字典 典礼 登山 登记 总是 '
#             '总结 总数 答题 回答 读书 朗读 造纸 造句 流血 心血 瓦片 砖瓦 热血 炎热 清凉 冰凉 学校 校园 拥抱 怀抱 抚摸 摸底 批评 '
#             '批发 评语 评论 责任 责备 责怪 水井 井口 第一 门第 停止 停车 痛苦 痛心 痛快 孩子 男孩 沉思 沉没 沉着 轻快 轻松 轻风 '
#             '口哨 哨声 树梢 眉梢 树枝 枝头 交换 变换 支出 支持 除法 消除 害虫 伤害 晴天 湖水 湖面 安静 平静 宁静 姑娘 新娘 朗读 '
#             '晴朗 狠心 狠命 讨论 论文 创造 创伤 开创 照旧 照常 感冒 冒烟 开始 始终 吸引 呼吸 身旁 旁边 处所 所以 总之 之前 欢喜 '
#             '喜爱 响亮 明亮 闪亮 感动 感受 感谢 答谢 使用 使劲 使者 一颗 保护 保持 夹层 夹杂 方便 轻便 表现 表示 味道 香味 美味 '
#             '山羊 羊肉 吃惊 拐弯 拐角 弯曲 弯路 垂挂 垂直 低垂 吃亏 理亏 花狗 狗肉 星期 期待 学期 刚才 刚好 漂亮 漂流 漂白 约定 '
#             '节约 汽车 汽油 等待 等候 车票 门票 失信 丢失 失约 任务 灰色 灰兔 早晨 清晨 做操 早操 机遇 相遇 失误 误会 咱们 顺路 '
#             '顺利 顺心 帝国 帝王 朝阳 朝气 岸边 海岸 啼哭 啼叫 小舟 轻舟 南方 南瓜 应该 虽然 关系 系列 担心 分担 对错 错字 越过 '
#             '越冬 依靠 靠近 初中 初步 跑步 船员 船只 比较 计较 内外 内心 科学 科目 部队 部分 最后 最近 通知 通过 沙石 沙包 沙发 '
#             '风景 景色 爬山 爬行 古诗 诗歌')
# unit_1_7 = ('一声不吭 一言不发 一声不响 一丝不苟 登门求教 沉甸甸 走走停停 悄悄话 静悄悄 晴空万里 惊天动地 惊弓之鸟 目瞪口呆 '
#             '不期而遇 诗情画意 ')

# unit_8_ = ('球场 拍球 羽毛 跳远 跳动 跳绳 黑板 板报 踢球 运动')

unit_9_10_13 = ('汉字 汉语 甲鱼 甲虫 骨头 标志 标准 推行 推动 笑容 面容 容易 轻易 伯父 伯母 酒店 酒会 语气 话语 古代 代表 周边 '
                '周围 宋朝 互相 相同 相信 相反 称呼 名称 会议 议论 时刻 立刻 冲洗 冲茶 时装 化装 至今 至于 大哥 踩水 喊叫 呼喊 '
                '妹妹 兄妹 长短 粗壮 粗心 紧张 松紧')
t_unit_9_13 = ('甲骨文 取长补短 粗枝大叶 安安')


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
    # print(len(unit_9_10_13.split(' ')))
    p = Pinyin()
    out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in t_unit_9_13.split(' ')]
    split_four(out)
    # out = [p.get_pinyin(w, ' ', show_tone_marks=True) for w in unit_9_10_13.split(' ')]
    # split_twice(out)
    # print_unicode(['应', '担'])
