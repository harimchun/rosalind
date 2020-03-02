#첫 번째 방법
s = ""
counting_dict = {}
for i in s.split(" "):
    if i in counting_dict:
        counting_dict[i] = counting_dict[i]+1
    else:
        counting_dict[i] = 1

for k, v in counting_dict.items():
    print(k,v)
"""
#두 번째 방법
f = open("/Users/harim/Downloads/rosalind_ini6_4_dataset.txt").readline()
s = f.rstrip('\n')
counting_dict = {}
for i in s.split(" "):
    if i in counting_dict:
        counting_dict[i] = counting_dict[i]+1
    else:
        counting_dict[i] = 1

for k, v in counting_dict.items():
    print(k,v)"""
