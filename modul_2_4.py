numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)) : # индес списка numbers
    if numbers [i] == 1: # если занчение =1, то его не рассматриваем
        i = i + 1
    else:
        is_prime = True
        for j in range (2, numbers [i] // 2 + 1): # делитель от 2 до значения числа / 2
            if numbers [i] % j == 0: # проверяем на простоту (остаток от деления =0)
                #brake - очень хотел, но команда в любом случае останавливает цикл сразу после j=2. Как сделать?
                is_prime = False
        if is_prime :
            primes.append(numbers [i])
        else:
            not_primes.append(numbers [i])
print('Primes:', primes)
print('Not primes:', not_primes)