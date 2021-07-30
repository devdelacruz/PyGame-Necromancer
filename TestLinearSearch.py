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

# lst = []
# num = int(input("Enter size of the list"))
# for n in range(num):
#     numbers = int(input("Enter any number: "))
#     lst.append(numbers)
#
# found = False
#
# x = int(input("Enter a number to be searched: "))
#
# for i in range(len(lst)):
#     if x == lst[i]:
#         found = True
#         print("Element is found at %d" % i)
#         break
#
# if not found:
#     print("Not found")


# import threading


# def runthreads():
#     th1 = threading.Thread(target=count1)
#     th1.start()
#     th1 = threading.Thread(target=count2)
#     th1.start()
#
#
# def count1():
#     print("Start of Count1")
#     for i in range(100000000):
#         print(i)
#     print("End")
#
#
# def count2():
#     print("Start of Count2")
#     for i in range(100000000):
#         print(i)
#     print("End")

#
# if __name__ == "__main__":
#     runthreads()

for i in range(10000000000):
    print(i)
