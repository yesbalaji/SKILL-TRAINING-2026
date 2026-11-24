n=[10,20,30,40]
t=50
low=0
high=len(n)-1
while low<=high:
    mid=(low+high)//2
    if(n[mid]==t):
        print("Found at index",mid)
        break
    elif n[mid]<t:
        low=mid+1
    else:
        high=mid-1
else:
    print("Element not found")
                