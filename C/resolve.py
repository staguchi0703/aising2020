def resolve():
    '''
    code here
    '''
    import math
    N = int(input())

    num_max = int(math.sqrt(N)) +1

    n_list = [[] for _ in range(N+1)]
    for i in range(1, num_max+1):
        for j in range(1, num_max+1):
            for k in range(1, num_max+1):
                if i**2+j**2+k**2+i*j+j*k+k*i <= N:
                    n_list[i**2+j**2+k**2+i*j+j*k+k*i] += [[i, j, k]]
    
    
    for i in range(1, N+1):
        temp = n_list[i]
        if temp:
            print(len(temp))
        else:
            print(0)


if __name__ == "__main__":
    resolve()
