'''
Dictionary -> {key: value}
dict()
mutable
iterable
values can be accessed using the keys

keys can only be the immutable datatypes
'''

stu = {
    "fname": "John",
    "lname" : "Doe",
    "course" : "Python",
    "age" : "23"
}

another_dict = dict(country="US", **stu)
#print(another_dict)

#print(stu)
#print(type(stu))

#print(stu["age"])
#print(stu)
stu["age"] = 25
stu["country"] = "IND"
#print(stu)

#print(stu.keys())
#print(stu.values())
#print(stu.items())

#for k,v in stu.items():
     #print(f"key is : {k} and value is : {v}")

#print(stu.get("age"))
#print(stu.get("ages","age is not present"))

#print(stu)
#print(stu.pop("age"))
#print(stu.popitem())

d = {"fname" : "Jane"}

stu.update(d)

stu.setdefault("age")
#print(stu)


# count frequency of each character in given word
w = "Hello how"

frq = {}

for i in w:
    if frq.get(i) == None:
        frq[i] = 1
    else:
        frq[i] = frq[i] + 1

#print(frq)

for i in w:
    if frq.get(i.lower()) == None:
        frq[i.lower()] = 1
    else:
        frq[i.lower()] = frq[i.lower()] + 1

#print(frq)

for i in w:
    if frq.get(i.upper()) == None:
        frq[i.upper()] = 1
    else:
        frq[i.upper()] = frq[i.upper()] + 1
#print(frq)

# TODO: WAP to count the frequency of words

w = "Hello world for Programming Environmnet Hello dear Software Environmnet"

w1 = w.split(" ")
frq = {}

for i in w1:
    if frq.get(i) == None:
        frq[i] = 1
    else:
        frq[i] = frq[i] + 1

#print(frq)

for i in w1:
    if frq.get(i.lower()) == None:
        frq[i.lower()] = 1
    else:
        frq[i.lower()] = frq[i.lower()] + 1

#print(frq)

for i in w1:
    if frq.get(i.upper()) == None:
        frq[i.upper()] = 1
    else:
        frq[i.upper()] = frq[i.upper()] + 1

#print(frq)