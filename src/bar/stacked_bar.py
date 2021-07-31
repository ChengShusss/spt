#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
src: https://blog.csdn.net/m0_45209371/article/details/108241200

"""

import matplotlib.pyplot as plt
import random


def plot_stacked_bar(data, series=None, x_label=None, config={}):
    # 加载一般配置
    width = config.get("width", 0.8)
    title = config.get("title", "default title")
    color_map_name = config.get("color_map_name", "tab20")
    color_map = plt.get_cmap(color_map_name).colors
    grid = config.get("grid", False)
    legend = config.get("legend", False)

    # 如果没有指定series和x轴标签，则装入默认值
    if not series:
        series = data.keys()
    if not x_label:
        candidate = [data[k].keys() for k in series]
        x_label = list(max(candidate))

    # 防止颜色映射数量不足
    assert len(series) <= len(color_map), "Not enough color map for data"

    # 每次堆叠时的基准：pos
    pos = [0] * len(x_label)
    color_index = 0

    # 按照series逐行绘制
    for label in series:
        # 获取每行的值
        line = data[label]
        values = [line[x] for x in x_label]

        # 绘制一行
        plt.bar(x_label, values, width, bottom=pos,
                label=label, color=color_map[color_index])

        # 更新基准值
        pos = [pos[i] + values[i] for i in range(len(values))]
        color_index += 1

    # 设置题目和图例
    plt.title(title)
    if legend:
        plt.legend()
    plt.grid(grid)



def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for stacked bar",
        "color_map_name": "tab20b",
        "legend": True
    }

    # 生成假数据
    data = {}
    series_count = 5
    data_length = 10
    series = [f"series-{x}" for x in range(series_count)]
    x_label = [f"7-{x+1}" for x in range(data_length)]
    for item in series:
        temp = {}
        for label in x_label:
            temp[label] = random.randint(5, 20)

        data[item] = temp
    
    # 自定义数据，请取消注释下一行，参考data变量的数据结构
    # print(data)

    # 绘图
    plot_stacked_bar(data,series=series[:], x_label=x_label[:-3], config=config)
    
    plt.show()


if (__name__ == "__main__"):
    main()
