import GGanalysis.games.reverse_1999 as RV
from GGanalysis.gacha_plot import QuantileFunction, DrawDistribution
from GGanalysis import FiniteDist
import matplotlib.cm as cm
import numpy as np
import time

def RV_character(x):
    return '塑造'+str(x-1)
def RV_collection(x):
    return '集齐'+str(x)+'种'

# 重返未来1999 UP6星角色
RV_fig = QuantileFunction(
        RV.up_6star(6, multi_dist=True),
        title='重返未来1999 UP六星角色抽取概率',
        item_name='UP六星角色',
        text_head='采用官方公示模型\n获取1个UP六星角色最多140抽',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=750,
        mark_func=RV_character,
        line_colors=cm.YlOrBr(np.linspace(0.4, 0.9, 6+1)),  # cm.OrAKges(np.linspace(0.5, 0.9, 6+1)),
        y_base_gap=25,
        is_finite=None)
RV_fig.show_figure(dpi=300, savefig=True)

# 重返未来1999 UP5星角色
ans_list = [FiniteDist()]
for i in range(1, 7):
    ans_list.append(RV.specific_up_5star(i))
RV_fig = QuantileFunction(
        ans_list,
        title='重返未来1999 特定UP五星角色抽取概率',
        item_name='UP五星角色',
        text_head='采用官方公示模型',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=750,
        mark_func=RV_character,
        line_colors=cm.GnBu(np.linspace(0.4, 0.9, 6+1)),  # cm.OrAKges(np.linspace(0.5, 0.9, 6+1)),
        y_base_gap=25,
        is_finite=False)
RV_fig.show_figure(dpi=300, savefig=True)

# 重返未来1999 常驻集齐UP6星角色
ans_list = [FiniteDist()]
for i in range(1, 12):
    ans_list.append(RV.stander_charactor_collection(target_types=i))
RV_fig = QuantileFunction(
        ans_list,
        title='重返未来1999集齐常驻6星角色概率',
        item_name='常驻6星角色',
        text_head='采用官方公示模型',
        text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
        max_pull=3800,
        mark_func=RV_collection,
        line_colors=cm.PuRd(np.linspace(0.2, 0.9, 11+1)),
        y_base_gap=25,
        mark_offset=-0.4,
        y2x_base=3,
        mark_exp=False,
        is_finite=False)
RV_fig.show_figure(dpi=300, savefig=True)

# 重返未来1999 集齐两个UP五星角色
RV_fig = DrawDistribution(
    dist_data=RV.both_up_5star(),
    title='重返未来1999集齐两个UP五星角色',
    max_pull=300,
    text_head='采用官方公示模型',
    text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    description_pos=200,
    is_finite=False,
)
RV_fig.show_dist(dpi=300, savefig=True)

# 重返未来1999 获取六星角色
RV_fig = DrawDistribution(
    dist_data=RV.common_6star(1),
    title='重返未来1999获取六星角色',
    text_head='采用官方公示模型',
    text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    is_finite=True,
)
RV_fig.show_dist(dpi=300, savefig=True)

# 重返未来1999 常驻获取特定六星角色
RV_fig = DrawDistribution(
    dist_data=RV.specific_stander_6star(1),
    title='重返未来1999常驻获取特定六星角色',
    text_head='采用官方公示模型',
    text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    max_pull=2300,
    description_pos=1550,
    quantile_pos=[0.25, 0.5, 0.75, 0.9, 0.99],
    is_finite=False,
)
RV_fig.show_dist(dpi=300, savefig=True)

# 重返未来1999 获取UP六星角色
RV_fig = DrawDistribution(
    dist_data=RV.up_6star(1),
    title='重返未来1999获取UP六星角色',
    text_head='采用官方公示模型',
    text_tail='@一棵平衡树 '+time.strftime('%Y-%m-%d',time.localtime(time.time())),
    is_finite=True,
)
RV_fig.show_dist(dpi=300, savefig=True)