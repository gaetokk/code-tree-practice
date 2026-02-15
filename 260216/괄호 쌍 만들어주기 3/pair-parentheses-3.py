A = input()

# Please write your code here.
answer = 0

for i in range(len(A)):
    if A[i] == "(":
        for n in range(i+1, len(A)):
            if A[n] == ")":
                answer += 1


print(answer)