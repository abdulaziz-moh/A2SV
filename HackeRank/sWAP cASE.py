def swap_case(s):
    ans = []
    cap = ord('A')
    sml = ord('a')
    for c in s:
        if c.isalpha():
            if ord(c) >= sml:
                w = chr(cap + ord(c) - sml)
                ans.append(w)
            else:
                w = chr(sml + ord(c) - cap)
                ans.append(w)
        else:
            ans.append(c)
        
    return "".join(ans)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)