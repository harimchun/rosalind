'''
#첫 번째 방법
f = open("/Users/harim/Downloads/rosalind_ini5.txt")
print(''.join(f.readlines()[1::2])) #[1::2] 첫 번째(사실 상 두번째)위치부터 끝까지 2칸씩 더해가며 출력
'''
#두 번째 방법
f = open("/Users/harim/Downloads/rosalind_ini5.txt")
a = f.readlines()

for i in range(len(a)+1):
    if i%2==1:
        #print(a[i])
        print(a[i][:-1])
