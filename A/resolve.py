def resolve():
    '''
    code here
    '''
    L, R, d = [int(item) for item in input().split()]

    cnt = 0
    for i in range(L, R+1):
        if i % d == 0:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    resolve()
