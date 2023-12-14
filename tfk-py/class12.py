class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
       m1 = self.m1 + other.m1
       m2 = self.m2 + other.m2
       s3 = student(m1, m2)
       return (s3)
    def __gt__(self,other):
        a1 = self.m1 + self.m2
        a2 = other.m1 + other.m2
        if a1 > a2:
            return True
        else:
            return False
    def __mul__(self,other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        b3 = student(m1, m2)
        return (b3)
    def __str__(self):
        return '{} {} '.format(self.m1,self.m2)

s1 = student(23, 34)
s2 = student(34, 56)
s3 = s1 + s2
b3 = s1 * s2
print(s3.m1)
print(s3.m2)
print(s3.m1 + s3.m2)
print(b3.m1)
print(s2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")
