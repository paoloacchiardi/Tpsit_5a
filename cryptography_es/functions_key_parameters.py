from mcm import Mcm

def p_q_values(n):
    list = [] #[0] = p, [1] = q
    if(n>=4):
        k = 2
        while(True):
            if(n % k == 0):
                list.append(int(k))
                list.append(int(n/k))
                return list
            if(k > n/2):
                break
            k += 1
    else:
        print(f"Error: n is not valid.")
        list[0] = int(0)
        list[1] = int(0)
        return list        

def m_value(p,q):
    p -= 1
    q -= 1
    return int(Mcm(p,q))

def c_value(m):
    c = 1
    while(True):
        c += 1
        if(c >= m):
            print(f"Error: m is not valid.")
            return 0
        k = 2
        possible = True
        while(possible):
            if(k < c):
                if(c % k == 0 and m % k == 0):
                    possible = False
                k += 1
            elif((k == c) and (m % k != 0)):
                return int(c)
            else:
                possible = False

def d_value(m,c):
    #(c*d) mod m = 1, (c*d) - (m*k) = 1
    d = 1
    while(True):
        d += 1
        k = 1
        while((m*k)<(c*d)):
            if(((c*d) - (m*k)) == 1):
                return int(d)
            k += 1

def parameters_values(n):
    if(n<4):
        print("Error, n is not valid.")
        return 0
    pq = list()
    pq = p_q_values(n)
    p = pq[0]
    q = pq[1]
    if(p == 0 or q == 0):
        print("Error, p/q are not valid.")
        return 0
    m = m_value(p,q)
    if(m == 0):
        print("Error, m is not valid.")
        return 0
    c = c_value(m)
    if(c == 0):
        print("Error, c is not valid.")
        return 0
    d = d_value(m,c)
    if(d == 0):
        print("Error, d is not valid.")
        return 0

    values = {}
    values["p"] = p
    values["q"] = q
    values["m"] = m
    values["c"] = c
    values["d"] = d
    return values