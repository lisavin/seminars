
def push(self, data):
    self.mystack.append(data)
    return "ok"

def pop(self):
    return self.mystack.pop()

def back(self):
    return self.mystack[len(self.mystack)-1]

def size(self):
    return len(self.mystack)

    def clear (self):
        self.mystack [:] = []
        return 'ok'

    def exit(self):
        return "bye"

mysuperstack = Stack()
komanda = input()
while komanda != 'exit':
    if komanda == 'push':
        elm = input()
        print (mysuperstack.push(stack.elm))
        komanda = input()
    if komanda == 'pop':
        print(mysuperstack.pop)
        komanda = input()
    if komanda == 'back':
        print (mysuperstack.back())