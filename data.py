a = 10
print("Before:", id(a))
a = a + 5
print("After:", id(a))

s = "hello"
print("\nBefore:", id(s))
s = s + " world"
print("After:", id(s))

lst = [1, 2, 3]
print("\nBefore:", id(lst))
lst.append(4)
print("After:", id(lst))

t = (1, 2, 3)
print("\nBefore:", id(t))
t = t + (4,)
print("After:", id(t))

d = {"a": 1}
print("\nBefore:", id(d))
d["b"] = 2
print("After:", id(d))
