print(dir(dict))
d1 = {1: "sai",
      2: "teja",
      3: "surya",
      4: "teja"}
for item in d1.items():
    print(item)

print(d1.keys())
print(d1.values())
print(d1.items())
d2 = d1.copy()
print(d2)
d1.clear()
print(d1)
print(d2.pop(1))
print(d2)
d1 = d2.copy()
print(d1)
d1[10] = "Saiteja"
print(d1)
newdict ={}
print(newdict.fromkeys("2345", ("sai", "teka")))
d1.update()
set = {1,2,23,4,54,5,56,223}
set.discard()