# class LinearSearch(object):
#     def __init__(self):
#         self.data = []
#
#     def index(self, suggestions: Sequence[str]) -> None:
#         for i in suggestions:
#             self.data.append(i)
#
#     def search(self, pre: str) -> Generator[str, None, None]:
#         for i in self.data:
#             if i.startswith(pre):
#                 yield i

lst = []
num = int(input("Enter size of the list"))
for n in range(num):
    numbers = int(input("Enter any number: "))
    lst.append(numbers)

found = False

x = int(input("Enter a number to be searched: "))

for i in range(len(lst)):
    if x == lst[i]:
        found = True
        print("Element is found at %d" % i)
        break

if not found:
    print("Not found")
