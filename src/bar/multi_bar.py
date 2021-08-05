#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
src: https://blog.csdn.net/qq_44864262/article/details/108098227

"""

__author__ = "Shadow Cheng"

import random
import numpy as np
import matplotlib.pyplot as plt



def plot_multi_bar(data, series=None, x_label=None, config={}):
    # 加载一般配置
    title = config.get("title", "default title")
    color_map_name = config.get("color_map_name", "tab20")
    color_map = plt.get_cmap(color_map_name).colors
    grid = config.get("grid", False)
    legend = config.get("legend", False)

    # ====================================================
    # 绘图逻辑
    # =====================================================
    if not series:
        series = data.keys()
    if not x_label:
        x_label = max([data[x].keys() for x in series])

    x = np.arange(len(x_label))
    total_width, n = 0.8, len(series)
    width = total_width / n
    x_base = x - (total_width - width) / 2
    
    for i in range(len(series)):
        values = data[series[i]].values()
        plt.bar(x_base + i * width, values, width=width, label=series[i])

    plt.xticks(x, x_label)

    # 设置题目和图例
    plt.title(title)
    if legend:
        plt.legend()
    plt.grid(grid)


def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for Plot",
        "color_map_name": "tab20b",
        'legend': True
    }

    # 生成假数据
    data = {}
    series_count = 3
    data_length = 5
    series = [f"series-{x}" for x in range(series_count)]
    x_label = [f"pos - {x:2d}" for x in range(data_length)]
    for item in series:
        temp = {}
        for label in x_label:
            temp[label] = random.randint(5, 20)

        data[item] = temp

    # 自定义数据，请取消注释下一行，参考data变量的数据结构
    print(data)

    # 绘图
    plot_multi_bar(data, series=series, x_label=x_label, config=config)
    plt.show()


if (__name__ == "__main__"):
    main()
