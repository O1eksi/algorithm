

def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    else:
        gen_bin(M-1, prefix+"0")
        gen_bin(M-1, prefix+"1")

def generate_namber(N:int, M:int, prefix=None):
    """
        Generates all numbers(with leading non-significant zeros) in the N-ary number system (N<=10) of length M
    :param N: Number <=10
    :param M: length
    :param prefix:
    :return:
    """
    if M == 0:
        print(prefix)
        return
    prefix = prefix or []
    for digit in range(N):
        prefix.append(digit)
        generate_namber(N, M-1, prefix)
        prefix.pop()

# generate_namber(10, 3)

gen_bin(3)