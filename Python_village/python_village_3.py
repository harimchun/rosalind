#방법1 - 수동적인 방법
s = input("문자열을 입력하시오. : ")
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
d = int(input("d :"))
print(s[a:b+1], s[c:d+1])
"""
#방법2 - 자동적인 방법
s = open("/Users/harim/Downloads/rosalind_ini3-2.txt", "r")
f = s.readlines()

s = f[0]
a = int(f[1].split()[0])
b = int(f[1].split()[1])
c = int(f[1].split()[2])
d = int(f[1].split()[3])

print(s[a:b+1], s[c:d+1])
"""
