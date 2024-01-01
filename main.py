# -*- coding: utf-8 -*-

from selenium import webdriver

from action import WebAction


def init():
    url = 'https://www.baidu.com'
    edge_driver = webdriver.Edge()
    edge_driver.get(url)
    # 关闭浏览器窗口
    return edge_driver


def load_script(script_path, brown_driver):
    action_ins = WebAction(brown_driver)
    with open(script_path, 'r', errors='ignore') as file:
        while True:
            # 逐行读取并打印内容
            web_script = file.readline()
            print(web_script.strip())  # 使用 strip() 方法去除行尾的换行符
            if '' == web_script:
                break
            action, xpath, value = parse_script(web_script)
            execute_script(action_ins, action, xpath, value)


def parse_script(web_script):
    # 提供的编码字符串
    # encoded_data = "点击按钮|submit_button|value"
    # 使用 | 进行分割
    split_data = web_script.split("|")
    # 分别取出变量
    action = split_data[0]
    xpath = split_data[1]
    value = split_data[2]
    # 打印结果
    print("行为:", action)
    print("网页元素:", xpath)
    print("值:", value)
    return action, xpath, value


def execute_script(action_ins, action_name, xpath_element, val):
    # 方法1: 使用getattr()函数
    if hasattr(action_ins, action_name):
        method = getattr(action_ins, action_name)
        method(xpath_element, val)
    else:
        print(f"Method '{action_name}' not found.")


if __name__ == '__main__':
    script_file = r'./test.txt'
    driver = None
    try:
        driver = init()
        load_script(script_file, driver)
    finally:
        if driver is not None:
            driver.close()
