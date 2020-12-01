import functions_key_parameters as par

def main():
    pq = list()
    n = int((input("Insert n value:")))
    pq = par.p_q_values(n)
    p = pq[0]
    q = pq[1]
    m = par.m_value(p,q)
    c = par.c_value(m)
    d = par.d_value(m,c)
    if(n != 0 and p != 0 and q != 0 and m != 0 and c != 0 and d != 0):
        print(f"n: {n}, c: {c}, p: {p}, q: {q}, m: {m}, d: {d}.")

if __name__ == "__main__":
    main()