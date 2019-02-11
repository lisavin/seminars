class Stack:
    def __init__(stack):
        stack = []

    def push(stack, data):
        stack.append(data)
        return "ok"

    def pop(stack):
        return stack.pop()

    def back(stack):
        return stack[len(stack)-1]

    def size(stack):
        return len(stack)

    def clear (stack):
        stack [:] = []
        return 'ok'

    def exit(stack):
        return "bye"

stack = Stack()
komanda = input()
while komanda != "exit":
    if komanda == 'push':
        elm = input()
        stack.push(stack.elm)