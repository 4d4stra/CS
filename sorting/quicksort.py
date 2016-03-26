import random
def quicksort(arr):
    #base cases
    if len(arr)==1:
        return arr
    else:
        #preprocessing, selecting random pivot; fixes
        pivot_ind=random.randint(0,len(arr)-1)
        pivot=arr[pivot_ind]
        #partition; using first element as partition
        sep=0
        while sep<len(arr) and arr[sep]<pivot:
            sep+=1
        for i in range((sep+1),len(arr)):
            if arr[i]<=pivot:
                arr[sep],arr[i]=arr[i],arr[sep]
                sep+=1
        #recurse
        if sep!=0:
            arr[:sep]=quicksort(arr[:sep])
        if sep!=len(arr):
            arr[sep:]=quicksort(arr[sep:])
        return arr

print quicksort([10,1,12,3,4,17,2,16,0])
