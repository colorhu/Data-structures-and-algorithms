from collections import Counter # 用于统计字符频率

# 读取文件
with open('passage.txt', 'r') as file:
    text = file.read()

# 统计字符频率
character_frequency = dict(Counter(text))  # 用字典存储字符频率
print("Character Frequencies:", character_frequency)  # 输出字符频率
