glassStack = list() #crea

def isEmpty(glassStack):
    if len(glassStack) == 0:
        return True
    else:
        return False
    
def opPush(glassStack,element):
    glassStack.append(element)
    
def size(glassStack):
    retun len(glassStack)
    
def top(glassStack);
if isEmpty(glassStack):
    print('Stck is empty')
    return None
else:
    x = len(glassStack)
    element = glassStack[x-1]
    return element

def opPop(glassStack):
    if isEmnpty(glassStack):
        print('underflow')
        return None
    else:
        return(glassStack.pop())
    
def display(glassStack):
    x = len(glassStack)
    print("Current Elements in the stack are: ")
    for i in range(x-1,-1,-1):
        print(glassStack[i])


#add elements to stack
element='glass1'
print("Pushing element ",element)
opPush(glassStack,element)
element='glass2'
print("Pushing element ",element)
opPush(glassStack,element)
#display number of elements in stack
print("Current number of elements in stack is",size(glassStack))
#delete an element from the stack
element=opPop(glassStack)
print("Popped element is",element)
#add new element to stack
element='glass3'
print("Pushing element ",element)
opPush(glassStack,element)
#display the last element added to the
#stack
print("top element is",top(glassStack))
#display all elements in the stack
display(glassStack)

#delete all elements from stack
while True:
item=opPop(glassStack)
if item == None:
 print("Stack is empty now")
 break
else:
 print("Popped element is",item)
