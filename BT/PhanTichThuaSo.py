def PhanTich(n):
    i=2
    print(n,"=",end='')
    while n>2:
        if n%i==0:
            print(i,end='')
            if n!=i:
                print("X",end='')
            n/=i
        else:
            i+=1
def main():
    while True:
        print("Nhap gia tri n:")
        n=int(input())
        if n>=1:
            break
    PhanTich(n)
main()
'''
"""
 * Phân tích số nguyên thành tích các thừa số nguyên tố
 *
 * @param positiveInt
 * @return
"""
def phanTichSoNguyen(n):
    i = 2;
    listNumbers = [];
    # phân tích
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            listNumbers.append(i);
        else:
            i = i + 1;
    # nếu listNumbers trống thì add n vào listNumbers
    if (len(listNumbers) == 0):
        listNumbers.append(n);
    return listNumbers;
 
n = int(input("Nhập số nguyên dương n = "));
# phân tích số nguyên dương n
listNumbers = phanTichSoNguyen(n);
size = len(listNumbers);
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listNumbers[i]) + " x ";
sb = sb + str(listNumbers[size-1]);
# in kết quả ra màn hình
print("Kết quả:", n, "=", sb);
'''

