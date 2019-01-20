# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
# contributed by Sokolov Yura
# modified by Tupteq

def fannkuch(n):
    count = range(1, n+1)
    max_flips = 0
    m = n-1
    r = n
    check = 0
    perm1 = range(n)
    perm = range(n)
    perm1_ins = perm1.insert
    perm1_pop = perm1.pop

    while 1:
        if check < 30:
            #print "".join(str(i+1) for i in perm1)
            check += 1

        while r != 1:
            count[r-1] = r
            r -= 1

        if perm1[0] != 0 and perm1[m] != m:
            perm = perm1[:]
            flips_count = 0
            k = perm[0]
            while k:
                tmp = perm[:k+1]
                tmp.reverse()
                perm[:k+1] = tmp
                flips_count += 1
                k = perm[0]

            if flips_count > max_flips:
                max_flips = flips_count

        while r != n:
            perm1_ins(r, perm1_pop(0))
            count[r] -= 1
            if count[r] > 0:
                break
            r += 1
        else:
            return max_flips

def main(n1, n2=9):
    for i in range(n1):
        fannkuch(n2)

if __name__ == "__main__":
    main(10)

def entry_point(argv):
    main(int(argv[1]), int(argv[2]))
    return 0

def target(*args):
    return entry_point, None
