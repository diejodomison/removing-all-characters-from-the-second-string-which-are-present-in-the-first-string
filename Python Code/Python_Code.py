k=input()
l=input()
m=""
for i in l:
    if i in k:
        continue
    else:
        m+=i
print(m)