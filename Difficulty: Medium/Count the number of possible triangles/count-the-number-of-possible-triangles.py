#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        # Sort the array
        arr.sort()
        n = len(arr)
        count = 0
        
        # Iterate for every possible largest side
        for k in range(2, n):
            i, j = 0, k - 1
            while i < j:
                # Check the triangle condition
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)  # All pairs (i, j), (i+1, j), ..., (j-1, j) are valid
                    j -= 1
                else:
                    i += 1
        
        return count    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends