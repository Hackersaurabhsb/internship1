mylist = [3, 2, 1, 7,4,5]


def partition(mylist, first, last):
    pivot = mylist[first]
    i = first+1
    j = last
    while i < j:
        while i <= j and mylist[i] <= pivot:
            i = i+1
        while j >= i and pivot <= mylist[j]:
            j = j-1
        if i < j:
            temp = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = temp
        temp = mylist[first]
        mylist[first] = mylist[j]
        mylist[j] = temp
    return j


def mainfunc(mylist, first, last):
    if first < last:
        pos = partition(mylist, first, last)
        mainfunc(mylist, first, pos-1)
        mainfunc(mylist, pos+1, last)


def quicksort(mylist):
    print("List before sorting is :")
    print(mylist)
    n = len(mylist)
    print("List after sorting is : ")
    mainfunc(mylist, 0, n-1)


quicksort(mylist)
print(mylist)
