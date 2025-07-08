# + Kiểu dữ liệu; + Biến; + Hàm input
#python là lập trình hướng đối tượng
# Hàm "type" xác định kiểu dữ liệu của giá trị truyền vào nó
# value; -1, 3, "Quang", True, False, 1j (số phức), 2.5 (số thực), 
# 0 và 0.0 khác nhau về kiểu dữ liệu
# Khi mình truyền 1 hàm, nhiều hàm truyền lẫn nhau nên mình phải tìm kiểu để không lẫn hoặc lọc giá trị
# dùng nhiều phân tích dữ liệu hoặc đọc code dự án, dữ liệu.

print(type(3)) # in kiểu 
print(type(-1.5))
print(type(True))
print(type(1j)) # số phức được biểu diễn dưới dạng "a + bj" a là phần thực, b là phần ảo, j^2 = -1
print(type('')) # Biến chuỗi "string"

# Biến là một cái tên cho một giá trị nào đó 
# Quy tắc đặt tên biến "Ko thể bắt đầu bằng số" và "ko chứa kí tự đặc biệt", "đặt tên có ý nghĩa và chuẩn tiếng anh"

birth_year = 2007 # snake case 
_ = 4.5
print(_)

# hàm input luôn trả về một chuỗi kí tự "str"
sentence = "I'm Quang" # Nếu đặt thành dấu " thì nó sẽ tự hiểu là đến đó là ngắt và ko hiểu đằng sau
# Muốn sửa thì chỉ cần đặt một dấu "\" trước " và sẽ được

sentence = "I\"m Quang"
print(sentence)

user_name = input("Nhập vào một tên người dùng: ")
print(user_name)

# Muốn thay thế nhiều tên biến giống nhau thì bôi đen và nhấn F2 -> thay đổi ở nhiều chỗ

num = input('Nhập vào một số: ')
print(num * 5)

# vì input chỉ nhập vào str nên num ở đây sẽ là str -> " * 5 " tức là nó sẽ lặp lại 5 lần chữ trên
# Hành động sẽ thực hiện dần từ trong ngoặc tròn ra bên ngoài 
# Nếu muốn nhập một số thì phải ép cái input thành số

second_num = int(input("Nhập một số: "))
print(second_num * 5)

# Thực hiện tính toán xong hết rồi mới print 
# Nếu muốn nó được nhập cả chuỗi số nguyên và số thực thì vì nếu int như trên chỉ dùng được cho số nguyên
# Dùng eval (Mẹo), còn nếu dùng float thì khi nhập 4 thì sẽ ra 4.0

full_num = eval(input("Nhập vào một số: "))
print(full_num)

age = int(input("Age: "))
print("I'm" + str(age))
#Vì chuỗi đi với chuỗi, số đi với số, nên age từ int phải chuyển về str để đi được với "I'm"
# dấu " + " 