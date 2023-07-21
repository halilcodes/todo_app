import time

# filenames = ['doc.txt', 'report.txt', 'presentation.txt']
#
# for file in filenames:
#     with open(file, "w") as f:
#         f.write("Hello")

# class Laptop:
#
#     def __init__(self, price):
#         self._price = price
#
#     def get_price(self):
#         return self._price
#
#     def set_price(self, value):
#         if not isinstance(value, (float, int)):
#             raise TypeError('The price attribute must be an int or float type.')
#
#
# laptop = Laptop(100)
#
# laptop.set_price("23")

print(time.localtime())
print(time.strftime("%d %b %Y %H:%M:%S"))