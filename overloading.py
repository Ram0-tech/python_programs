# x,y=10,20
# print(x+y)

class A:
    def __init__(self,n):
        self.n=n
    # def _add_(self, other):
    #     return self.n+other.n
    # def _sub_(self, other):
    #     return self.n - other.n
    # def _eq_(self, other):
    #     return self.n==other.n
    def _str_(self):
        return str(self.n)
x=A(10)
y=A(20)
# print(x+y)
# print(x-y)
# print(x==y)
print(x)


# class A:
#     def __init__(self,n):
#         self.n=n
#     def _add_(self, other):
#         return self.n+other.n
#
# x=A("Hello ")
# y=A("python")
# print(x+y)