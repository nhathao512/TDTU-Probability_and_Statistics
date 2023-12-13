import cv2
import numpy as np
import matplotlib.pyplot as plt

# THUẬT TOÁN CÂN BẰNG LƯỢC ĐỒ

# Đọc ảnh từ file image.jpg bằng hàm cv2.imread()
img = cv2.imread('image.jpg')

# Chuyển ảnh sang thang độ xám bằng hàm cv2.cvtColor()
hinh_xam = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Lấy kích thước chiều cao và chiều rộng của ảnh đã chuyển sang màu xám
h_cao, w_rong = hinh_xam.shape

# Tạo mảng temp có kích thước 256 phần tử, mỗi phần tử là số lượng pixel có cùng giá trị cấp xám
temp = np.zeros(256)

# Duyệt qua từng pixel của ảnh, tăng giá trị tương ứng trong mảng temp
for i in range(h_cao):
    for j in range(w_rong):
        temp[hinh_xam[i,j]] = temp[hinh_xam[i,j]] + 1

# Chuẩn hóa lược đồ bằng cách chia cho tổng số pixel
temp = temp / (h_cao * w_rong)

#Tính hàm phân phối tích lũy (CDF) từ histogram
cdf = np.zeros(256)
cdf[0] = temp[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + temp[i]

# Nhân CDF với 255 để thu được các giá trị mới sau khi cân bằng
GTM = np.round(cdf * 255)

# Gán lại các giá trị mới cho từng pixel trong ảnh gốc để tạo ra ảnh cân bằng
e_img = np.zeros_like(hinh_xam)     # lưu ảnh đã cân bằng
for i in range(h_cao):
    for j in range(w_rong):
        e_img[i, j] = GTM[hinh_xam[i, j]]

# Hiển thị ảnh gốc và ảnh đã cân bằng lược đồ
cv2.imshow('Anh goc (Gray Image)', hinh_xam)
cv2.imshow('Anh da can bang (Equalized Image)', e_img)
cv2.waitKey(0)

# Lược đồ của ảnh gốc
plt.hist(hinh_xam.ravel(), 256, [0,256])  # Chuyển ảnh về dạng một chiều
plt.title('Luoc do cua anh goc')    # Đặt tên tiêu đề
plt.show()  #Hiển thị lược đồ

# Lược đồ của ảnh đã được cân bằng
plt.hist(e_img.ravel(), 256, [0,256]) # Chuyển ảnh về dạng một chiều
plt.title('Luoc do cua anh da can bang')  # Đặt tên tiêu đề
plt.show() #Hiển thị lược đồ