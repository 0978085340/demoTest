def dem_so_luong_tieng_viet(chuoi):
    # Dictionary chứa các chữ cái Telex và tương ứng Tiếng Việt
    telex_to_vietnamese = {
        'aw': 'ă', 'aa': 'â', 'dd': 'đ', 'ee': 'ê', 'oo': 'ô', 'ow': 'ơ', 'w': 'ư'
    }
    
    so_luong = 0
    i = 0
    while i < len(chuoi):
        for k in range(2, 4):  # Kiểm tra các chuỗi con có độ dài từ 2 đến 3 ký tự
            telex = chuoi[i:i+k]
            if telex in telex_to_vietnamese:
                so_luong += 1
                i += k - 1
                break
        i += 1

    return so_luong

# Thử nghiệm chức năng với một chuỗi đầu vào
chuoi = input("Nhập chuỗi chữ cái Latin: ")
so_luong = dem_so_luong_tieng_viet(chuoi)
print("Số lượng chữ cái Tiếng Việt có thể tạo ra từ chuỗi nhập vào là:", so_luong)
