# %%
#Task 9: Prime Number 
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True

# Example
print(is_prime(7))
print(is_prime(10))


# %%
#Task 10: Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Example
n = 1234
print(f"The sum of digits in (n) is {sum_of_digits(n)}")

# %%
#Task 11: LCM and GCD
import math 
def lcm_gcd(a,b):
    gcd = math.gcd(a,b)
    lcm = (a * b) // gcd
    return lcm, gcd

# Example
print(lcm_gcd(12, 18))
print(lcm_gcd(7, 5))


# %%
#Task 12: List Reversal
def reverse_list(lst):
    return lst[::-1]

# Example
print(reverse_list([1,2,3,4]))
print(reverse_list([7,8,9]))


# %%
#Task 13: Sort a List
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

# Example
print(bubble_sort([5, 3, 8, 1, 2]))


# %%
#Task 14: Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

#Example
print(remove_duplicates([1, 2, 2 , 3, 4, 4, 5]))

# %%
#Task 15: string Length
def string_length(s):
    count = 0 
    for _ in s:
        count +=1
    return count

# Example
print(string_length("HelloWorld"))
print(string_length("Python"))

# %%
#Task 16: Count Vowels and Consonants
def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v_count, c_count = 0, 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count +=1
            else:
                 c_count +=1

    return v_count, c_count

# Example
s = "hello world"
vowels, consonants = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")


# %%
import random

def generate_maze(size):
    maze = [[1 for _ in range(size)] for _ in range(size)]

    def carve_passages(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < size and 0 <= ny < size and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy][x + dx] = 0
                carve_passages(nx, ny)

    maze[1][1] = 0  # Start point
    carve_passages(1, 1)
    return maze

def print_maze(maze):
    for row in maze:
        print("".join("█" if cell == 1 else " " for cell in row))  # Walls as █, paths as space

def solve_maze(maze, start, end):
    stack = [start]
    visited = set()
    
    while stack:
        x, y = stack.pop()
        
        if (x, y) == end:
            return True
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze) and maze[ny][nx] == 0:
                stack.append((nx, ny))

    return False  # Only return False if no path is found

# Example
size = 11
maze = generate_maze(size)
print_maze(maze)
start, end = (1, 1), (size - 2, size - 2)
print(f"Solvable? {solve_maze(maze, start, end)}")


# %%



