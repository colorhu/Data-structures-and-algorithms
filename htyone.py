class Stack:  # 栈
    def __init__(self):
        self.items = []

    def push(self, item):  # 入栈
        self.items.append(item)  # 将元素添加到列表末尾

    def pop(self):  # 弹出栈顶元素
        if not self.is_empty():  # 判断栈是否为空
            return self.items.pop()  # 弹出栈顶元素，列表方法pop()默认弹出列表末尾的元素
        else:
            raise ValueError("Stack is empty")

    def is_empty(self):  # 判断栈是否为空
        return len(self.items) == 0

    def peek(self):  # 返回栈顶元素
        if not self.is_empty():
            return self.items[-1]  # 返回列表最后一个元素，即栈顶元素
        else:
            raise ValueError("Stack is empty")


def is_operator(char):  # 判断是否为运算符
    return char in "+-*/"


def precedence(operator):  # 运算符优先级
    if operator in "+-":
        return 1
    if operator in "*/":
        return 2
    return 0


def is_numeric(char):  # 判断是否为数字
    return char.replace('.', '', 1).isnumeric()  # 这个代码段的目的是允许检测像 "3.14" 这样的浮点数字符串，将其转换为 "314"，然后检查它是否是一个数字。
    # .isnumeric() 方法只能用于检查整数
    # 不能直接检查浮点数。通过将小数点去除后，就可以检查剩余的字符串是否是整数。如果剩余的字符串是整数，.isnumeric() 返回 True，表示该字符是数字；如果不是整数，则返回 False。


def infix_to_postfix(expression):  # 中缀转后缀
    postfix = []  # 后缀表达式
    stack = Stack()  # 运算符栈
    i = 0
    while i < len(expression):  # 遍历表达式
        if is_numeric(expression[i]):
            start = i  # 数字的起始位置
            while i < len(expression) and (is_numeric(expression[i]) or expression[i] == '.'):  # 找到数字的结束位置
                i += 1
            postfix.append(expression[start:i])  # 数字直接添加到后缀表达式
            print("postfix:", postfix)
        elif expression[i] == '(':  # 左括号直接入栈
            stack.push(expression[i])  # 左括号入栈
            print("stack:", stack.items)
            i += 1
        elif expression[i] == ')':  # 右括号将栈中的运算符弹出，直到遇到左括号
            print("读取到右括号‘）’")
            while not stack.is_empty() and stack.peek() != '(':  # 遇到左括号停止,栈不为空
                postfix.append(stack.pop())  # 将运算符添加到后缀表达式,stack中弹出运算符
                print("stack:", stack.items)
                print("postfix:", postfix)
            stack.pop()  # 弹出左括号
            print("stack:", stack.items)
            i += 1  # 继续遍历
        elif is_operator(expression[i]):  # 运算符
            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(
                        expression[i])):  # 栈不为空，栈顶不是左括号，栈顶运算符优先级大于等于当前运算符，弹出栈顶运算符，添加到后缀表达式
                postfix.append(stack.pop())  # 将栈顶运算符弹出，添加到后缀表达式
                print("postfix:", postfix)
            stack.push(expression[i])  # 当前运算符入栈
            print("stack:", stack.items)
            i += 1
        else:  # 忽略空格
            i += 1
    while not stack.is_empty():  # 将栈中剩余的运算符弹出
        postfix.append(stack.pop())  # 添加到后缀表达式
        print("postfix:", postfix)
    return postfix  # 返回后缀表达式


def evaluate_postfix(expression):  # 求值后缀表达式
    stack = Stack()  # 操作数栈
    for char in expression:  # 遍历后缀表达式
        if is_numeric(char):  # 操作数入栈
            print(stack.items)
            stack.push(float(char))  # 将操作数转换为浮点数
        elif is_operator(char):
            operand2 = stack.pop()  # 弹出操作数
            operand1 = stack.pop()  # 弹出操作数
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            print(stack.items)
            stack.push(result)  # 将运算结果入栈
            print(stack.items)
    return stack.pop()  # 返回运算结果


def replace_parentheses(text):
    # 将中文括号替换为英文括号,很重要，找这个bug找了好久
    text = text.replace("（", "(").replace("）", ")")  # 将中文括号替换为英文括号
    return text


if __name__ == "__main__":
    file_name = "date.txt"

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            expression = file.read()
            expression = replace_parentheses(expression)  # 将中文括号替换为英文括号
            print(f"读取的中缀表达式: {expression}")

            postfix_expression = infix_to_postfix(expression)  # 中缀转后缀
            print(f"后缀表达式: {' '.join(postfix_expression)}")

            result = evaluate_postfix(postfix_expression)  # 求值后缀表达式
            print(f"求值结果: {result}")
    except FileNotFoundError:  # 文件未找到
        print(f"文件 '{file_name}' 未找到")
    except Exception as e:  # 其他错误
        print(f"发生错误: {e}")
#（7+15）*（23-28/4）#