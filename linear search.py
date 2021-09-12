
def reverse(li):
    l=len(li)
    for i in range(l):
        if i%2==0:
            li[i], li[i+1] = li[i+1], li[i]

li=[int(x) for x in input().split()]
print(li)
reverse(li)
print(li)