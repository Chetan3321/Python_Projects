# Stack implementation using a list
stack = []

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushing elements:", stack)

# Pop an element (removes the last item)
popped_item = stack.pop()
print("Popped Item:", popped_item)
print("Stack after popping an element:", stack)

# Peek at the top of the stack
top_item = stack[-1]
print("Top Item:", top_item)

# Check if the stack is empty
if not stack:
    print("The stack is empty")
else:
    print("The stack is not empty")
