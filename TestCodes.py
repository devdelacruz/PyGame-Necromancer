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

# from csv import DictReader
# # open file in read mode
#
# list = []
#
# with open('gamelogs.csv', 'r') as read_obj:
#     # pass the file object to DictReader() to get the DictReader object
#     csv_dict_reader = DictReader(read_obj)
#     # iterate over each line as a ordered dictionary
#     for row in csv_dict_reader:
#         # row variable is a dictionary that represents a row in csv
#         print(row)

# import csv

# my_dict = {"Name":[],"Points":[],"Levels Cleared":[]};

# thisdict = {
#   "Name": "1",
#   "Points": "1",
# }
# thisdict.update({"color": "red"})

# Bubble Sort
import csv

List = []

with open("gamelogs.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for lines in csv_reader:
            x = lines['Name']
            y = lines['Points']
            List.append(y + '        ' + x)

# print("=======================")
# print(List)

for i in range(0, len(List) - 1):
    for j in range(len(List) - 1):
        if (List[j] > List[j + 1]):
            List[j], List[j + 1] = List[j + 1], List[j]

# print("=======================")
List.reverse()
# print(List)
#
# print("=======================")


for y in range(5):
    print(List[y])