import random
#pick out the ith smallest index value from an unsorted array
def ith_order_stat(arr,i):
    #base cases
    if len(arr)==1:
        return arr
    else:
        #preprocessing, selecting random pivot; fixes
        pivot_ind=random.randint(0,len(arr)-1)
        pivot=arr[pivot_ind]
        arr[0],arr[pivot_ind]=arr[pivot_ind],arr[0]
        #partition; using first element as partition
        sep=0
        while sep<len(arr) and arr[sep]<=pivot:
            sep+=1
        for ii in range((sep+1),len(arr)):
            if arr[ii]<=pivot:
                arr[sep],arr[ii]=arr[ii],arr[sep]
                sep+=1
        #recurse
        if sep-1==i:#our pivot is the element! Weeeeee!
            return arr[0]
        elif sep>i:
            arr_new=ith_order_stat(arr[:sep],i)
        else:
            i-=sep
            arr_new=ith_order_stat(arr[sep:],i)
        return arr_new
