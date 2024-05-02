# Function to find the maximum sum of an alternating subsequence
def max_alternating_subsequence_sum(nums):
    stack = []
    flag = 1  # Flag to indicate the sign of the first element
    total_sum = 0

    # Iterate through the sequence
    for k in nums:
        if not stack:  # Check if the stack is empty
            stack.append(k)
            if k < 0:
                flag = 0
        else:
            if flag == 0:
                if k < 0 and k > stack[-1]:  # If negative and greater than top element of stack
                    stack.pop()
                    stack.append(k)
                if k > 0:
                    stack.append(k)
                    flag = 1
            else:
                if k > 0 and k > stack[-1]:  # If positive and greater than top element of stack
                    stack.pop()
                    stack.append(k)
                if k < 0:
                    stack.append(k)
                    flag = 0

    # Sum up the elements in the stack
    total_sum = sum(stack)
    return total_sum

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the length of the sequence and the sequence of numbers
    n = int(input())
    nums = list(map(int, input().split()))

    # Calculate and print the maximum sum of the alternating subsequence
    print(max_alternating_subsequence_sum(nums))
