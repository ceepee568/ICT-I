name=input("Enter your name: ")
for i in name:
    print(i)
li=["Python Programming","Python Fundamentals","Python Interview Questions"]
for x in li:
    print(x)
print()

lenli=len(li)
for x in range(lenli):
    print(li[x])
print()

my_tuple=tuple(li)
for x in (my_tuple):
    print(x)
print()

my_set=set(li)
for x in (my_set):
    print(x)
print()

tup=("John Smith", "Jane Doe","Alice Johnson")
for x in tup:
    print(x)

set1={10,30,20}
for x in set1:
    print(x)

BookDetails=dict({"Python Programming":"John Smith","Python Fundamentals": "Alice Johnson","Python Interview Questions":"Jane Doe"})
for keys in BookDetails:
    print(keys,BookDetails[keys])
