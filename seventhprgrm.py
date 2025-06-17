# 1.Given a list colors=['red','green','blue']
colors=['red','green','blue']

#     a).Print the list
print(colors)
#     b).print the last elemnt
print(colors[-1])
#     c)print the second color
print(colors[1])

#     d)Add new color purple to the list
colors.append("purple")
print(colors)
#     e).update the color green into yellow color
colors[1]="yellow"
print(colors)
#     f).Reverse the list
print(colors[::-1])
#     g).length of the list
print(len(colors))
#
l=[34,67,12,90,23,78]
# # swap the 2nd element and last element
l[1],l[-1] = l[-1],l[1]
print(l)
# #
#
# 3.Given a list l=[[1,'Arun',23,'ekm'],[2,'Anu',24,'tvm'],[3,'Amal',25,'tcr']]
l1=[[1,'Arun',23,'ekm'],[2,'Anu',24,'tvm'],[3,'Amal',25,'tcr']]
s=l1[0][2]+l1[1][2]+l1[2][2]
avg =s/3
print(avg)
# print the average age of 3 students from given data.