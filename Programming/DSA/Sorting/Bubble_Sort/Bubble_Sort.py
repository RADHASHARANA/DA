from typing import List

def bubble_sort_ascending(array: List[int]):
     # Iterate from 0 to n-1
    for i in range(len(array)):
        #(Ai, Ai+1) compare Ai and Ai+1 from 0 to n-i-2 
        for j in range(0,len(array)-1-i):
            # compare Ai,Ai+1 and if not in correct position then swap
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def main():
    array = list(map(int, input('Enter the unsorted array: ').split( )))
    bubble_sort_ascending(array=array)
    print(array)

main()