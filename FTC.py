import re

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def __getitem__(self, i):
        return self.items[i]
    
    def __gettop__(self):
        if not self.is_empty():
            top = len(self.items)
            return self.items[top - 1]
        else:
            return None
    def __print__(self):
        print(self.items)



def checkPop(i, c, o):
    if i == c:
        if pilha.__gettop__() == o:
            pilha.pop()
            if aux.__gettop__() == dic[o]:
                aux.pop()



#main
pilha = Stack()
aux = Stack()
check = ''

dic = {'(': 0, '[': 1, '{': 2}
# lines = []
# while True:
#     line = input()
#     if line != 'END':
#         lines.append(line)
#     else:
#         lines.append('END')
#         break

entrada = '( { [ ] } )'
match = re.search(r'[^\(\)\[\]\{\} ]', entrada)
entrada = re.sub(r' +', '', entrada)
print(entrada)

pilha.push('$')
aux.push(3)
if match is None:
    if (len(entrada) != 0):
        for i in entrada:

            if i == '(' or i == '[' or i == '{':
                pilha.push(i)

                if aux.__gettop__() >= dic[i]:
                    aux.push(dic[i])
                else:
                    aux.push(-1)
                    

            checkPop(i, ')', '(')
            checkPop(i, ']', '[')
            checkPop(i, '}', '{')

else:
    print('character estranho')

    
pilha.pop()
aux.pop()

if pilha.is_empty() and aux.is_empty():
    print('casada e correta')

elif pilha.is_empty() and not aux.is_empty():
    print('casada e incorreta')

else:
    print('nao casada')

corrigido = entrada

match = re.findall(r'\(\[|\(\{|\[\{|\]\)|\}\)|\}\]', entrada)

for i in range(0, len(match)):
    print(match[i], match[i][::-1])
    a = re.escape(match[i])
    b = re.escape(match[i][::-1])

    corrigido = re.sub(a, b, corrigido)
    corrigido = re.sub(r'\\', '', corrigido)
    print(corrigido)