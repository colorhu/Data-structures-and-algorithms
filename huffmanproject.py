from collections import Counter  # 用于统计字符频率

# 读取文件
with open('passage.txt', 'r', encoding='utf-8') as file:   # 读取文件，编码格式为utf-8
    text = file.read()

# 统计字符频率
character_frequency = dict(Counter(text))  # 用字典存储字符频率
print("Character Frequencies:", character_frequency)  # 输出字符频率


# class Node:
#     def __init__(self, value, freq):
#         self.value = value
#         self.freq = freq
#         self.left = None
#         self.right = None
#
#
# def huffman_tree(frequencies):
#     nodes = [Node(char, freq) for char, freq in frequencies.items()]
#
#     while len(nodes) > 1:
#         nodes = sorted(nodes, key=lambda x: x.freq)
#
#         left = nodes[0]
#         right = nodes[1]
#
#         new_node = Node(None, left.freq + right.freq)
#         new_node.left = left
#         new_node.right = right
#
#         nodes = nodes[2:]
#         nodes.append(new_node)
#
#     return nodes[0]
#
#
# # 构建哈夫曼树
# huffman = huffman_tree(character_frequency)
#
#
# def encode(root, current_code, encoded):
#     if root is not None:
#         if root.value is not None:
#             encoded[root.value] = current_code
#         encode(root.left, current_code + '0', encoded)
#         encode(root.right, current_code + '1', encoded)
#
#
# # 构建哈夫曼编码表
# huffman_codes = {}
# encode(huffman, '', huffman_codes)  # 用字典存储哈夫曼编码
#
# # 对文本进行编码
# encoded_text = ''.join([huffman_codes[char] for char in text])  # 将文本转为哈夫曼编码
#
# # 将编码后的文本转为字节，并写入文件
# padded_encoded_text = format(int(encoded_text, 2), '0' + str((len(encoded_text) + 7) // 8) + 'b')  # 将编码后的文本转为字节
#
# with open('compressed_file.bin', 'wb') as output_file:
#     output_file.write(
#         bytes(int(padded_encoded_text[i:i + 8], 2) for i in range(0, len(padded_encoded_text), 8)))  # 将字节写入文件
