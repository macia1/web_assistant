import pandas as pd


def excel_reader(path):
    result = []
    df = pd.read_excel(path)
    # 打印读取的数据
    print(df)
    # 使用 iterrows() 遍历 DataFrame
    for index, row in df.iterrows():
        print(f"Index: {index}, 书名: {row['书名']}")
        result.append(row)
    print(result)
    print(result[0]['书名'])
    return result


def txt_reader(path):
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if '' != line:
                line_list = line.split("|")
                line_result = {}
                index = 1
                for word in line_list:
                    line_result[index] = word
                    index = index + 1
                result.append(line_result)
    return result


if __name__ == '__main__':
    prompt = excel_reader('ChatGPT Prompt.xlsx')
    print(prompt)
    reader = txt_reader("test.txt")
    print(reader)
