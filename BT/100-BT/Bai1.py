'''
Bài 01:
Câu hỏi:
Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in
thành chuỗi trên một dòng, cách nhau bằng dấu phẩy
'''
'''

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print(i,end=',')
'''
j=[]
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        j.append(str(i))
print(','.join(j))