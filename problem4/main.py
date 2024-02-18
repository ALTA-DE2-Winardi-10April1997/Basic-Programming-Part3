def palindrome(input_string):
    clean_string = input_string.lower()
    if clean_string == clean_string[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False