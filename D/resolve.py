def resolve():
    '''
    code here
    '''
    N = int(input())
    X = [item for item in input()]

    cnt_1_x = X.count('1')

    def cal(i, X):
        cnt = 0
        if X[i] == '1':
            X[i] = '0'
            cnt_1 = cnt_1_x - 1
        else:
            X[i] = '1'
            cnt_1 = cnt_1_x + 1

        num = ''.join(X)
        num = int(num, 2)
        print(num, num % cnt_1)
        while num > 0:
            num %= cnt_1
            cnt_1 = bin(num)[2:].count('1')
            cnt += 1

        return cnt

    for i in range(N):
        print(cal(i, X))


if __name__ == "__main__":
    resolve()
