def prime_number(num):
    if num > 1 :
        for x in range(2,num):
            if num % x == 0:
                return "Not Prime"
        else:
            return "Prime"
    else:
        return "Not Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"