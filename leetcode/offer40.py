from typing import List
class Solution:
    def getLeastNumbers(self,arr:List[int],k:'int')-> List[int]:
        def quick_sort(arr,l,r):
            if l>=r: return
            i,j =l,r
            while i<j:
                while i<j and arr[j] >= arr[l]: j-=1
                while i<j and arr[i] <= arr[l]: i+=1
            arr[l],arr[i] =arr[j],arr[i]

            quick_sort(arr,l,i-1)
            quick_sort(arr,i+1,r)

        quick_sort(arr,0,len(arr)-1)
        return arr[:k]