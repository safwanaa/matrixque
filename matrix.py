# first_multiple_input = input().rstrip().split()
# n = int(first_multiple_input[0])
# m = int(first_multiple_input[1])
# matrix = []
# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)



a = input().rstrip().split()


n = int((a[0]))
m = int((a[1]))


matrix = []
for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
result = ""


for j in range(m):
    
    alphanum= False
    for i in range(n):
       
        char=matrix [i][j]
        
        
        if char.isalnum():
            result += char
            alphanum = True
        elif char == ' ':
            
            if alphanum:
                result += ' '
                alphanum = False
        else:
            result += ' '

    result += ' '


print(result)

