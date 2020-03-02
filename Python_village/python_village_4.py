"""
#방법1. 수동으로 입력해주기
a = 100
b = 200
sub = 0
for i in range(a, b+1):
    if i%2 ==1:
       sub += i

print (sub)
a = int(input("첫 번째 숫자 : "))
b = int(input("두 번째 숫자 : "))
sub = 0
for i in range(a, b+1):
    if i%2 ==1:
       sub += i

print (sub)
"""
#방법2. 자동으로 입력해주기
s = open("/Users/harim/Downloads/rosalind_ini4-2.txt", "r")
f = s.readlines()
print("Ⅰ. f : ", f)
print("Ⅱ. f[0] :",f[0])
print("Ⅲ. f[0].split : ", f[0].split())
print("----------------------------------------------")

print ("첫 번째 숫자 : ", f[0].split()[0])
print ("두 번째 숫자 : ", f[0].split()[1], "\n")
print("--------------------------------------------------------------")

a = int(f[0].split()[0])
b = int(f[0].split()[1])

sub =0

for i in range(a, b+1):
    if i%2==1:
        sub +=i
print ("%s부터 %s까지의 숫자 중에서 홀수인것을 더한 값은\n%s \n입니다. "%(a, b, sub))