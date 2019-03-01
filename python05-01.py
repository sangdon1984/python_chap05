class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

# print(type(a))
a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)
print(a.sum())
b = FourCal()
b.setdata(5, 6)
print(a.first)
print(a.second)
print(a.sum())