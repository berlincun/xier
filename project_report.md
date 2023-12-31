# 《Python程序设计基础》程序设计作品说明书

题目： 项目1： 外星人入侵游戏👽

学院： 21计科

姓名： 莫杭程

学号： B20210302224

指导教师： 周景

起止日期：2023.11.10-2023.12.10

## 摘要

本实验基于教材内容，实现了一个外星人入侵游戏。通过Python编程，成功创建了游戏窗口，并添加了飞船图像，使玩家可以驾驶飞船并射击子弹。同时，创建了一群外星人，它们可以移动并被射杀，游戏在玩家射杀所有外星人。此外，添加了Play按钮、提高等级和计分功能，增加了游戏的趣味性和挑战性。最终，实现了部分练习的功能，如将飞船放在屏幕左侧进行射击、在游戏背景中绘制星星以及将最高分保存到文件中。

关键词：
外星人入侵游戏、飞船、外星人、计分、等级提升。

## 第1章 需求分析

1.游戏窗口：需要创建一个可视化的游戏窗口，用于展示游戏画面和交互界面。

2.飞船图像：需要添加飞船的图像，并实现飞船的移动和射击功能。

3.外星人群：需要创建一群外星人，并实现它们在屏幕上的移动和被射杀的功能。

4.游戏结束条件：需要设定游戏结束的条件，如玩家射杀所有外星人。

5.Play按钮：需要添加一个Play按钮，用于开始游戏或重新开始游戏。

6.等级和计分：需要实现游戏的等级提升和计分功能，增加游戏的挑战性和趣味性。

7.练习功能：需要实现教材中的部分练习功能，如将飞船放在屏幕左侧进行射击、在游戏背景中绘制星星以及将最高分保存到文件中。

## 第2章 分析与设计

### 系统架构
1.游戏窗口和图形界面：负责创建游戏窗口，加载并显示飞船、外星人和子弹等图像。

2.游戏逻辑和控制：包括处理飞船和外星人的移动、射击行为，定义游戏规则和结束条件，以及处理计分和等级提升等游戏逻辑。

3.用户交互和输入控制：负责响应用户的输入操作，如键盘控制飞船移动和射击，处理鼠标点击事件等。
### 系统流程
1.游戏初始化：加载游戏所需的资源，包括图像等，初始化游戏窗口和各种游戏对象。

2.游戏进行：不断循环检测用户输入、更新游戏对象的状态、处理碰撞检测、计算得分等，实现游戏的持续进行。

3.游戏结束：当满足游戏结束条件时，展示游戏结束画面，保存最高分等。
### 系统模块
1.游戏初始化模块：负责加载游戏资源，初始化游戏窗口和各种游戏对象。
2。游戏逻辑控制模块：包括处理游戏对象的移动、射击行为，定义游戏规则和结束条件，处理计分和等级提升等游戏逻辑。
3.用户交互模块：处理用户输入，如键盘操作、鼠标点击等。
4.显示模块：负责游戏画面的显示，包括飞船、外星人、子弹的生成，以及游戏得分、等级等信息的展示。
5.星星模块：每次循环中，生成一个随机位置的星星，并将其坐标存储在stars列表中。然后，遍历stars列表，将所有的星星绘制到游戏界面上。

### 关键实现
1.加载游戏窗口和图形资源。
2.实现飞船和外星人的移动、射击逻辑。
3.响应用户输入，控制飞船的移动和射击。
4.实现计分和等级提升功能。
5.处理游戏的启动、进行和结束流程，包括最高分的保存和展示

## 第3章 软件测试

### 单元测试用例

| \#  | 测试目标 | 输入 | 预期结果 | 测试结果 |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |    键盘控制飞船移动       | 右键      |  飞船向上移动                |       飞船向上移动            |
| 2   |    键盘控制子弹射出       |  按住空格     |     飞船连续射出子弹             |           飞船连续射出子弹        |
| 3   |       得分模块    |    空格   |          子弹击中外星人获得十分        |            子弹击中外星人获得十分       |
| 4   |       play again按钮   |   点击play again按钮    |           重新开始游戏        |          重新开始游戏         |                 |

## 结论

本项目成功实现了外星人入侵游戏的基本功能，包括创建游戏窗口、添加飞船图像、驾驶飞船、飞船射击子弹、创建一群外星人、外星人移动和射杀、结束游戏、添加Play按钮、提高等级、计分功能等。同时，也实现了教材中部分练习的功能，如将飞船放在屏幕左侧进行射击、在游戏背景中随机位置绘制星星、将游戏中得到的最高分保存到文件中。

然而，项目仍有改进的空间。例如，可以增加更多的游戏元素和关卡设计，提升游戏的趣味性和挑战性；优化游戏界面和用户交互设计，改进游戏的可玩性和用户体验；加入音效和背景音乐，提升游戏的沉浸感。另外，还可以考虑增加外星人的等级与不同的血量。

总的来说，该项目初步实现了外星人入侵游戏的基本功能，但仍有许多方面可以进一步改进和完善，以提升游戏的整体品质和吸引力。

## 参考文献
[1]Eric Matthes.Python Crash Course: A Hands-On, Project-Based Introduction to Programming,2015

[2]Al Sweigart,Invent Your Own Computer Games with Python,2010

[3]Real Python,How to Build a 2D Game in Python,2022

[4]刘班.基于Pygame快速开发游戏软件[J].数字技术与应用,2013,31(8):130-130

[5]陆嘉诚,王楚虹,师文庆,黄江.基于Python的飞机大战游戏开发[J].机电工程技术,2020,49(3):75-77
