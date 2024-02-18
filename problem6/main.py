def prime_number(num):
    if num > 1:
        for x in range(2,num):
            if num % x == 0:
                return False
        else:
            return True
    else:
        return False

def full_prima(N):
    # your code here
    str_num = str(N)
    if '-' in str_num:
        return False
    for digit in str_num:
        if not prime_number(int(digit)):
            return False
    else:
        return True


if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True