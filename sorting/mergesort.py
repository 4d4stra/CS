

def mergesort(arr):
    #defining base cases
    if len(arr)==1:
        return arr
    elif len(arr)==2:
        if arr[0]>arr[1]:
            arr[0],arr[1]=arr[1],arr[0]
        return arr
    else:#recursion,splitting arrays in half
        arr_i=mergesort(arr[:len(arr)/2])
        arr_k=mergesort(arr[len(arr)/2:])
        #combining sorted arrays
        counter_k=0
        counter=0
        for i in range(len(arr_i)):
            while counter_k<len(arr_k) and arr_k[counter_k]<arr_i[i]:
                arr[counter]=arr_k[counter_k]
                counter_k+=1
                counter+=1
            arr[counter]=arr_i[i]
            counter+=1
        while counter_k<len(arr_k):
            arr[counter]=arr_k[counter_k]
            counter+=1
            counter_k+=1
        return arr

print mergesort([10,1,12,3,17,2,16,0])
