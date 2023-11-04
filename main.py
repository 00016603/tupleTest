t = ('a','b','c','d')
print(t)
t1=tuple()
print(t1)
t2='a',
print(type(t2))
t3=tuple('salam')
print(t3[0])
print(t[1:3])
print((16640, 18, 'Tsoy') > (16045, 18, 'Nikita'))

def has_match(t1,t2):
    for x,y in zip(t1,t2):
        if x==y:
            return True
        return False

t1 = [('Name', 'Armani'), ('Age' , 19)]
t2 = [('Name', 'Tsoy'), ('Age' , 20)]
has_match(t1,t2)
