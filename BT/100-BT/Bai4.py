'''
Câu hỏi:
Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện
điều khiển, tạo ra một danh sách và một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Gợi ý:
 Viết lệnh yêu cầu nhập vào các giá trị sau đó dùng quy tắc chuyển đổi kiểu dữ
liệu để hoàn tất
'''
values=input("Nhập vào các giá trị:")
l=values.split(",")
t=tuple(l)
print (l)
print (t)
