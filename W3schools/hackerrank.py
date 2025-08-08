#def is_leap(year):
#    leap = False
#    
#    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#        leap = True
#        
#    return leap
#year = int(input("Enter year: "))
#print(is_leap(year))

#if __name__ == '__main__':
#    n = int(input())
#for i in range(n-1, -1, -1):
#    print(n - i, end = " ")
    
#def print_full_name(first, last):
#    print("Hello", first, last + "! You just delved into python")
#
#if __name__ == '__main__':
#    first_name = input()
#    last_name = input()
#    print_full_name(first_name, last_name)

#if __name__ == '__main__':
#    x = int(input())
#    y = int(input())
#    z = int(input())
#    n = int(input())
#
#g = [x, y, z]
#new_g = [[i, j, k] for i in range(0, x+1, 1) for j in range(0, y+1, 1) for k in range(0, z+1, 1) if (i + j + k) != n]
#print(new_g, end="")

#if __name__ == '__main__':
#    n = int(input())
#    arr = map(int, input().split())
#arr = list(arr)
#rem = max(arr)
#while rem in arr:
#    arr.remove(rem)
#print(max(arr))

#if __name__ == '__main__':
#    for _ in range(int(input())):
#        record = []
#        name = input()
#        score = float(input())
#        record.append([name, score])


#Bài Find the percentage
#if __name__ == '__main__':
#    n = int(input())
#    student_marks = {}
#    for _ in range(n):
#        name, *line = input().split()
#        scores = list(map(float, line))
#        student_marks[name] = scores
#    query_name = input()
#scores = student_marks[query_name]
#if query_name in student_marks:
#    ava = (sum(scores))/(len(scores))
#    print(f'{ava:.2f}')


#Bài Basic Data Types
#if __name__ == '__main__':
#    N = int(input())
#    list = []
#    for i in range(N):
#        user_input = input().split()
#        
#        if user_input[0] == "insert":
#            list.insert(int(user_input[1]), int(user_input[2]))
#        elif user_input[0] == "print":
#            print(list)
#        elif user_input[0] == "remove":
#            list.remove(int(user_input[1]))
#        elif user_input[0] == "append":
#            list.append(int(user_input[1]))
#        elif user_input[0] == "sort":
#            list.sort()
#        elif user_input[0] == "pop":
#            list.pop()
#        elif user_input[0] == "reverse":
#            list.reverse()


#Bài Find a string
#def count_substring(string, sub_string):
#    count = 0
#    for i in range(0, len(string)):
#        if string[i:i+len(sub_string)] == sub_string:
#            count += 1
#    return count
#
#if __name__ == '__main__':
#    string = input().strip()
#    sub_string = input().strip()
#    
#    count = count_substring(string, sub_string)
#    print(count)

#if __name__ == "__main__":
#    n = int(input())
#    int_list = map(int, input().split())
#    tuple_list = tuple(int_list)
#    print(hash(tuple_list))


# String Validators
#if __name__ == '__main__':
#    s = input()
#l_s = list(s)
#check = []
## Alnum
#for c in l_s:
#    if c.isalnum():
#        check.append("True")
#    else:
#        check.append("False")
#if "True" in check:
#    print("True")
#    check.clear()
#else:
#    print("False")
#    check.clear()
## Alpha
#for c in l_s:
#    if c.isalpha():
#        check.append("True")
#    else:
#        check.append("False")
#if "True" in check:
#    print("True")
#    check.clear()
#else:
#    print("False")
#    check.clear()
## Digit
#for c in l_s:
#    if c.isdigit():
#        check.append("True")
#    else:
#        check.append("False")
#if "True" in check:
#    print("True")
#    check.clear()
#else:
#    print("False")
#    check.clear()
## Lowercase
#for c in l_s:
#    if c.islower():
#        check.append("True")
#    else:
#        check.append("False")
#if "True" in check:
#    print("True")
#    check.clear()
#else:
#    print("False")
#    check.clear()
## UpperCase  
#for c in l_s:
#    if c.isupper():
#        check.append("True")
#    else:
#        check.append("False")
#if "True" in check:
#    print("True")
#    check.clear()
#else:
#    print("False")
#    check.clear()  
#    
## cách đúng 
#if __name__ == '__main__':
#    s = input()
#
#    print(any(c.isalnum() for c in s))
#    print(any(c.isalpha() for c in s))
#    print(any(c.isdigit() for c in s))
#    print(any(c.islower() for c in s))
#    print(any(c.isupper() for c in s))

# Text Wrap
#import textwrap
#
#def wrap(string, max_width):
#    result = textwrap.fill(string, max_width)
#    return result
#
#if __name__ == '__main__':
#    string, max_width = input(), int(input())
#    result = wrap(string, max_width)
#    print(result)

#arr = map(int, input().split())
#l_arr = list(arr)
#N = l_arr[0]
#M = l_arr[1]
#thickness = int((N-1)/2)
#
## Top
#for i in range(thickness):
#    print((str(".|"+("..|"*i)*2+".")).center(M, "-"))
#
## Middle
#print("WELCOME".center(M, "-"))
#
## Bottom
#for i in range(thickness-1, -1, -1):
#    print(str(".|"+("..|"*i)*2+".").center(M, "-"))

# Another way
#h, w = map(int, input().split())
#for i in range(1,h,2):
#    print((".|."*i).center(w,"-"))
#print("WELCOME".center(w,"-"))
#for i in range(h-2,0,-2):
#    print((".|."*i).center(w,"-"))

#def print_formatted(number):
#    for i in range(1, number+1, 1):
#        width = len(bin(number)[2:])
#        print(str(i).rjust(width), (oct(i)[2:]).rjust(width), (hex(i))[2:].upper().rjust(width), (bin(i))[2:].rjust(width))
#
#if __name__ == '__main__':
#    n = int(input())
#    print_formatted(n)

#def print_rangoli(size):
#    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#    width = (4*size)-3
#    if size == 1:
#        width_a = 1
#    else:
#        width_a = 3
#    for i in range(1, size):
#        print(("-".join(alphabet[size-1 : size-i : -1] ) +"-"+ "-".join(alphabet[size-i])+"-"+"-".join(alphabet[size-i+1 : size])).center(width, "-"))
#    # Middle
#    print(("-".join(alphabet[n-1:0:-1]) + "-".join(alphabet[0]).center(width_a, "-") + "-".join(alphabet[1:n:1])).center(width, "-"))
#    for i in range(size-1, 0, -1):
#        print(("-".join(alphabet[size-1 : size-i : -1] ) +"-"+ "-".join(alphabet[size-i])+"-"+"-".join(alphabet[size-i+1 : size])).center(width, "-"))
#    
#if __name__ == '__main__':
#    n = int(input())
#    print_rangoli(n)

#def print_rangoli(size):
#    alphabet = [chr(i) for i in range(97, 123)]
#    alphabet = alphabet[:size]
#    indices = list(range(size))
#    indices = indices[::-1] + indices[:-1]
#    for i in indices:
#        start_index = i + 1
#        original = alphabet[-start_index:]
#        reverse = original[::-1]
#        row = reverse + original[1:]
#        row = "-".join(row)
#        width = size * 4 - 3
#        row = row.center(width, "-")
#        print(row)
#if __name__ == '__main__':
#    n = int(input())
#    print_rangoli(n)
