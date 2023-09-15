from typing import List

def selectionSort(array: List[int]):
    #Iterate from 0 to n-2
    for i in range(len(array)-1):
        # Find minm element from i+1 to n-1 and replace it's actual position(ith)
        #minm = array[i]
        minm_index = i
        #find minm element
        for j in range(i+1,len(array)):
            if array[minm_index] < array[j]:
                #minm = array[j]
                minm_index = j
        array[i],array[minm_index] = array[minm_index],array[i] # swap the minimum element


def main():
    array = list(map(int, input('Enter the unsorted array: ').split( )))
    selectionSort(array=array)
    print(array)

main()