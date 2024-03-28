if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
# Generate all possible coordinates using list comprehension
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# Filter out coordinates where the sum is not equal to n
filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

print(filtered_coordinates)