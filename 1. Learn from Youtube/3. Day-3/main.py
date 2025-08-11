'''
 "pip install autopep8"
 "==" equal to
 "!=" not equal to
 > greater than
 < less than
 >= greater than or equal to
 <= less than or equal to
 list [] ko thể sửa
 tuple () Không thể thay đổi, Có thứ tự cố định, dữ liệu được sắp xếp theo thứ tự được thêm vào.
 dict {} có thể sửa, Không có thứ tự cố định, các phần tử không được sắp xếp theo một trật tự nào.

/ -> float
// -> int
print(round(2.6)) -> sẽ làm tròn đến số gần nó nhất là 3 
số chẵn sẽ làm tròn xuống
số lẻ sẽ làm tròn lên
print(round(2.6556, 2)) làm tròn sau dấu phẩy 2 chữ số

mã AC2
print('a' > 'b') -> False
khi dùng ord('a') -> 97
khi dùng chr(97) -> a

Thứ tự giảm dần là: not and or

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
'''
def nhap_so():
    return int(input("Nhập số: "))

def kiem_tra_chan_le(n):
    if n % 2 == 0:
        return "chẵn"
    else:
        return "lẻ"

def hien_thi_ket_qua(ket_qua):
    print("Số bạn nhập là số", ket_qua)

so = nhap_so()
ket_qua = kiem_tra_chan_le(so)
hien_thi_ket_qua(ket_qua)

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)


print("Python is " + x)
myfunc()

x = ["apple", "banana", "cherry"]
print(type(x))

a = "I am Quang"
print(a[0:3])
print("Quang" in a)
print("Minh" not in a)

name = input("Tên: ")
age = int(input("Tuổi: "))
print(name, age, sep="|")  #nếu muốn cách giữa 2 từ bằng dấu nào đó

print(round(2.5666, 2))
'''

'''
Bài toán tử 

print(1 > 2 and 4 > 5) -> False and False -> False
print(False or True) -> True or False = True

and => first if False else second
python quy ước: 0 là False, 1 là True
Falsy: 0, 0.0, 9j, None, (), [], set(), '' (giá trị trống)
'''

print(1 and 2)