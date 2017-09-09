def brute_prime(seed):
    """
    brute_prime takes a non-negative interger seed, and returns the lowest
    prime number which is equal or greater than seed.
    """
    # test each integer seed, with integers test_number
    while seed:
        define_prime = True  # define_prime indicates if seed is a prime number
        for test_number in range(2, int(seed**0.5)+1):
            if seed % test_number == 0:
                define_prime = False
                break
        if define_prime:
            return seed
        seed += 1


def euclid_gcd(m, n):
    """
    euclid_gcd takes positive integers m and n
    and returns the greatest common divisor(gcd).
    """
    while n > 0:
        r = m % n
        m = n       # assign the value of n to m and the value of r to n.
        n = r
        if n == 0:
            return m


def txt2num(txt, k=3):
    """
    txt2num takes a string txt, and an integer k specifying the number
    of digits each character should tanslate to, defaulting to 3,
    and return an integer representation of order of txt
    """
    # concatenate '0' to the order of each letter
    order = ''
    for letter in txt:
        length_of_order = len(str(ord(letter)))
        order_of_letter = (k - length_of_order) * '0' + str(ord(letter))
        order += order_of_letter
    
    # eliminate '0' from front of the first letter
    if order[0] == '0':
        order = order[(k - length_of_order):]
    return int(order)


def num2txt(num, k=3):
    """
    num2txt takes a positive integers num,
    and an integer specifying the number of digit each character should
    translate to, k which is defaulting to 3,
    and returns txt, a string translated represents num.
    """
    txt = ''
    num = str(num)
    
    # translate each part of numbers into character and add to an empty string
    while num:
        # translate numbers at the back and move forward
        if len(num) > k:   # when there are more than one characters
            character = chr(int(num[-k:]))
            txt += character
            num = num[:-k]
        else:              # when there is only one character
            character = chr(int(num))
            txt += character
            break


from reference import brute_prime, euclid_gcd, extended_euclid
def rsa(min_p, min_q, min_e):
    """
    rsa takes three positive integers, min_p, min_q and min_e,
    and returns a 3-tuple contains three smallest prime numbers,
    public key d, private key e and modulus n respectively.
    """
    p = brute_prime(min_p)
    q = brute_prime(min_q)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = brute_prime(min_e)


from reference import txt2num
def rsa_encrypt(msg, e, n, k=3):
    """
    rsa_encrypt takes msg which is the message to be decrypted,
    e which is a positive integer representing the public key,
    n which is also a positive intger representing the modulus,
    k which is an optional positive integer that has default value of 3,
    and returns a positive integer of encrypted message using the formula.
    """
    m = txt2num(msg, k=k)
    c = m ** e % n
    return c
    
    # determine the value of e if gcd of e and phi is not one


from reference import num2txt
def rsa_decrypt(c, d, n, k=3):
    """
    rsa_decrypt takes c, a positive integer containing encrypted message,
    d which is a postive integer representing the private key,
    n which is a postive integer representing the modulus,
    k which is an optional positive integer that has default value of 3,
    and returns msg, a string containing decrypted version of message.
    """
    m = c ** d % n
    msg = num2txt(m, k=k)
    return msg
    while euclid_gcd(e, phi) != 1:
        min_e += 1
        e = brute_prime(min_e)
    d = extended_euclid(e, phi)
    return(d, e, n)
    return txt[::-1]
