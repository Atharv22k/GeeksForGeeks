class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        leaders = []
        
        # Start from the rightmost element
        max_from_right = arr[n - 1]
        leaders.append(max_from_right)
        
        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders.append(arr[i])
                max_from_right = arr[i]
        
        # Reverse the leaders list to maintain the original order
        leaders.reverse()
        
        return leaders


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends