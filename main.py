class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


def is_balanced(string):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"
    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return "Несбалансированно"

            last_open = stack.pop()

            if bracket_map[char] != last_open:
                return "Несбалансированно"

    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == '__main__':

    stack_test = Stack()
    print(f"Стек пуст? {stack_test.is_empty()}")
    stack_test.push(10)
    stack_test.push(20)
    stack_test.push(30)
    print(f"Стек: {stack_test}")
    print(f"Размер стека: {stack_test.size()}")
    print(f"Верхний элемент (peek): {stack_test.peek()}")
    print(f"Извлекаем верхний элемент (pop): {stack_test.pop()}")
    print(f"Стек после pop: {stack_test}")
    print(f"Размер стека после pop: {stack_test.size()}")
    print(f"Верхний элемент (peek): {stack_test.peek()}")
    print(f"Стек пуст? {stack_test.is_empty()}")

    try:
        while True:
            stack_test.pop()
    except IndexError as e:
        print(f"Попытка pop из пустого стека: {e}")

    balanced_sequences = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "()[]{}",
        ""
    ]

    unbalanced_sequences = [
        "}{",
        "{{[(])]}}",
        "[[{())}]",
        "([)]",
        "(()",
        "))",
        "{"
    ]

    for seq in balanced_sequences:
        result = is_balanced(seq)
        print(f"'{seq}' -> {result}")
        assert result == "Сбалансированно"

    for seq in unbalanced_sequences:
        result = is_balanced(seq)
        print(f"'{seq}' -> {result}")
        assert result == "Несбалансированно"

    print("Все тесты пройдены успешно!")
    if __name__ == '__main__':
        user_input = input("Введите строку со скобками для проверки: ")
        print(is_balanced(user_input))