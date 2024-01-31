def isPrime(N):
    if N < 2:
        return False
        
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
            
    return True

def find_primes(N, primes):
    count = 0
    temp = 0
    start = 0
    end = 0

    while start < len(primes) and end <= len(primes):
        if temp < N:
            if end < len(primes):
                temp += primes[end]
                end += 1
            else:
                break
        elif temp > N:
            temp -= primes[start]
            start += 1
        else:
            count += 1
            temp -= primes[start]
            start += 1

    return count
    
def answer(N):
    primes = []
    for num in range(2, N + 1):
        if isPrime(num):
            primes.append(num)
            
    return find_primes(N, primes)


N = int(input())
res = answer(N)
print(res)
