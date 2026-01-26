import sys
print("initial sys.path")
for p in sys.path:
    print(p)
sys.path.append("C: \ Users\ADMIN\PycharmProjects\PythonProject\my_project")
print("sys.path")
for p in sys.path:
    print(p)

print("\nAfter adding a new path: ")
for p in sys.path:
    print(p)

import hello_Anna
hello_Anna.say_hi()

