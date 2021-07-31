#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""Template for plot.

"""

__author__ = "Shadow Cheng"

import matplotlib.pyplot as plt
import random


def plot_xxx(data, x_label=None, config={}):
    # 加载一般配置
    title = config.get("title", "default title")
    color_map_name = config.get("color_map_name", "tab20")
    color_map = plt.get_cmap(color_map_name).colors

    
    # ====================================================
    # 绘图逻辑
    #=====================================================


    # 设置题目和图例
    plt.title(title)
    plt.legend()

    plt.show()


def main():
    # 配置绘图细节
    config = {
        "width": 0.8,
        "title": "Temp for stacked bar",
        "color_map_name": "tab20b",
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
    plot_xxx(data,series=series[:], x_label=x_label[:-3], config=config)


if (__name__ == "__main__"):
    main()
