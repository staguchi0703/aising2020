def resolve():
    '''
    code here
    '''
    N = int(input())
    As = [int(item) for item in input().split()]

    cnt = 0
    for i, item in enumerate(As):
        if (i+1) % 2 == 1 and item % 2 == 1: 
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
