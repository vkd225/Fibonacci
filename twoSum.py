elems = [1,2,3,5,7,9]

def two_solution(elems, target):
    dict = {}
    for i in xrange(len(elems)):
        key = target - elems[i]
        if key in dict:
            print(dict[key] , i)
        else:
            dict[elems[i]] = i

two_solution(elems, 9)
