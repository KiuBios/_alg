from datetime import datetime
power = [None]*10000
power[0] = 1
power[1] = 2


def power2n(n):
    if n < 0: raise
    if not power[n] is None: return power[n]
    power[n] = power2n(n-1)+power2n(n-1)
    return power[n]

n = 40
startTime = datetime.now()
print(f'power2n({n})={power2n(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'time:{seconds}')