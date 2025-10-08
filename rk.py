def rabin_karp(text, pattern):
    d, q = 256, 101          
    M, N = len(pattern), len(text)
    p = t = 0
    h = 1
    for i in range(M-1): h = (h*d) % q       
    for i in range(M):                        
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    result = []
    for i in range(N-M+1):
        if p == t and text[i:i+M] == pattern:
            result.append(i)
        if i < N-M:
            t = (d*(t - ord(text[i])*h) + ord(text[i+M])) % q
            t = (t + q) % q                    
    return result


text = input("Enter text: ")
pattern = input("Enter pattern: ")
matches = rabin_karp(text, pattern)
print("Pattern found at indices:", matches)
