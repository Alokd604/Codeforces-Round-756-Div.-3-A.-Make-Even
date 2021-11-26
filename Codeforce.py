test_case=int(input())
while(test_case):
    n = input()
    num = int(n)
    # print(num2)
    # print(num2/2)
    even_digit=0
    for i in range(0, len(n)):
        num2 = int(n[i])
        # print(num2)
        if (num2 % 2 == 0):
            even_digit=1
            break
    num2 = int(n[0])
    if (num % 2 == 0):
        print(0)
    elif (num == 1 or num == 3 or num == 5 or num == 7 or num == 9):
        print(-1)
    elif (num2%2==0):
        print(1)
    elif even_digit==1:
        print(2)
    else:
        print(-1)
    test_case=test_case-1





