# Phần chào mừng
print('*' * 60)
print('* CHÀO MỪNG QUÝ KHÁCH ĐẾN VỚI CHƯƠNG TRÌNH PHÂN LOẠI HỌC SINH *')
print('*' * 60)
print("Quý khách vui lòng nhập thông tin học sinh để chúng tôi phân loại.")
print("\nChương trình sẽ đánh giá học sinh dựa trên điểm khoa học, xã hội và kỹ năng mềm.")
print("=" * 40)

# Tiếp tục với phần nhập dữ liệu học sinh (code chính)
s = k = d = e = 0
soluong = int(input('Nhập số lượng học sinh: '))  # Convert input to integer
# Nhập dữ liệu học sinh
for i in range(1, soluong + 1):  # Adjust range to include all students
    a = input('Nhập tên học sinh: ')
    x = float(input('Nhập điểm khoa học: '))
    y = float(input('Nhập điểm xã hội: '))
    z = float(input('Nhập điểm kỹ năng mềm: '))
    
    # Tính toán phân loại
    s = (x + y + z) / 3
    print('Điểm trung bình của', a, 'là:', s)

    if (s >= 8):
        k += 1
        print(a, 'xuất sắc thật')
    elif (s >= 5.5) and (s <= 7.9):
        d += 1
        print(a, 'làm tốt lắm')
    else:
        e += 1
        print(a, 'cố lênnnn')
    
    print('-' * 10)

print('Có tổng cộng', k, 'HSG (Học sinh giỏi)')
print('Có tổng cộng', d, 'HSK (Học sinh khá)')
print('Có tổng cộng', e, 'HSTB (Học sinh trung bình)')
