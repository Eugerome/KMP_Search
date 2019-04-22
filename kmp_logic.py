import random

letters = ["A", "B", "C", "D"]

# generates string for testing
def generate_string(len_str):
    pattern = "".join([random.choice(letters) for i in range(len_str)])
    return pattern

# returns list of indexes 
def KMP_search(text, pattern):
    len_txt = len(text)
    len_ptrn = len(pattern)
    # start indexes, i for pattern, j for text
    i = j = 0
    # list of indexes when the patterns start
    patterns_found = []
    # 
    lps = compute_prefix(pattern, len_ptrn)

    while i < len_txt:
        if pattern[j] == text[i]:
            j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == len_ptrn:
            patterns_found.append(i-j)
            j = lps[j - 1]         
    return patterns_found

# creates list for longest prefix 
def compute_prefix(pattern, len_ptrn):
    # list 
    lps = [0]*len_ptrn
    # previous longest prefix
    p_len = 0

    i = 1
    while i < len_ptrn:
        if pattern[i] == pattern[p_len]:
            p_len += 1
            lps[i] = p_len
            i += 1
        else:
            if p_len != 0:
                p_len = lps[p_len - 1]
            else:
                lps[i] = 0
                i +=1
    return lps

def test():
    test_count = 200
    i = 0
    while i < test_count:
        len_ptrn = random.randint(2,6)
        len_txt = len_ptrn*10
        pattern = generate_string(len_ptrn)
        text = generate_string(len_txt)
        print(text)
        print(pattern)
        print(KMP_search(text, pattern))
        i += 1


if __name__ == '__main__':
    test()