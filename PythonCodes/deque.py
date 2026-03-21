from collections import deque

dq = deque([10, 20, 30])

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable)
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  

print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)