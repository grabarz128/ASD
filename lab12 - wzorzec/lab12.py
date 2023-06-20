import time

with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

S = ' '.join(text).lower()


def naive(text, match):
        count = 0
        comparison = 0
        s_id = []
        end = len(text)
        end_match = len(match)
        m = 0
        while m != end - end_match + 1:
                i = 0 
                while i != end_match:
                        comparison += 1
                        if S[m+i] != match[i]:
                                break
                        i +=1
                        if i == end_match:
                                count += 1
                                s_id.append(m)
                                break
                m += 1
        return str(count) +";"+ str(comparison)

def hash(word, d = 256, q = 101):
    hw = 0
    for i in range(len(word)):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def rabin_karp(text,match):
        hW = hash(match)
        count = 0
        comparison = 0
        end = len(text)
        end_match = len(match)

        for m in range (0,end-end_match+1):
                hS = hash(S[m:m+end_match])
                comparison +=1
                if hS == hW:
                        if S[m:m+end_match] == match:
                                count += 1
        return str(count) +";"+ str(comparison)


def rabin_karp_rolling(text,match):
        hW = hash(match)
        count = 0
        comparison = 0
        end = len(text)
        end_match = len(match)
        collision = 0
        d = 256
        q = 101
        h= 1
        for i in range(end_match - 1):
                h = (h * d) % q

        for m in range (0,end-end_match+1):
                if m == 0:
                        hS = hash(S[m:m+end_match])
                else:
                        hS = (d * (hS - ord(text[m - 1]) * h) + ord(text[m - 1 + end_match])) % q   
                
                if hS < 0:
                        hS +=q

                comparison +=1
                if hS == hW:
                        if S[m:m+end_match] == match:
                                count += 1
                        else:
                                collision +=1


        return str(count) +";"+ str(comparison)
                
def compute_T(W):
        T = [0 for _ in range(len(W))]
        pos = 1
        cnd = 0
        T[0] = -1
        n = len(W)
        while pos < n:
                if W[pos] == W[cnd]:
                        T[pos] = T[cnd]
                else:
                        T[pos] = cnd
                        while cnd >= 0 and W[pos] != W[cnd]:
                                cnd = T[cnd]
                pos +=1
                cnd +=1
        return T

def kmp(S,W):
        nP = 0
        comparison = 0
        m = 0
        n = len(W)
        i = 0
        T = compute_T(W)
      
        while m < len(S):
                comparison +=1
                if W[i] == S[m]:
                        m +=1
                        i +=1
                        if i == n:
                                nP +=1
                                i = T[i-1]
                else:
                        i = T[i]
                        if i<0:
                                m +=1
                                i +=1
        return str(nP) +";"+ str(comparison)  +";"+ str(T)


#t_start = time.perf_counter()
print(naive(S,'time.'))
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

#t_start = time.perf_counter()
print(rabin_karp_rolling(S,'time.'))
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

#t_start = time.perf_counter()
print(kmp(S,'time.'))
#t_stop = time.perf_counter()
#print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
