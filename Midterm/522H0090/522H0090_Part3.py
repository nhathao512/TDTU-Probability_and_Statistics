import cv2
import numpy as np
import matplotlib.pyplot as plt

# THUẬT TOÁN PHÙ HỢP LƯỢC ĐỒ

# Đọc ảnh từ file image.jpg bằng hàm cv2.imread()
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

# Chuyển ảnh sang thang độ xám bằng hàm cv2.cvtColor()
hinh1_xam = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
hinh2_xam = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Lấy kích thước chiều cao và chiều rộng của ảnh đã chuyển sang màu xám
h1_cao, w1_rong = hinh1_xam.shape
h2_cao, w2_rong = hinh2_xam.shape

# Tạo mảng temp có kích thước 256 phần tử, mỗi phần tử là số lượng pixel có cùng giá trị cấp xám
temp1 = np.zeros(256)
temp2 = np.zeros(256)

# Duyệt qua từng pixel của ảnh, tăng giá trị tương ứng trong mảng temp
for i in range(h1_cao):
    for j in range(w1_rong):
        temp1[hinh1_xam[i,j]] = temp1[hinh1_xam[i,j]] + 1

for i in range(h2_cao):
    for j in range(w2_rong):
        temp2[hinh2_xam[i,j]] = temp2[hinh2_xam[i,j]] + 1

# Chuẩn hóa histogram bằng cách chia cho tổng số pixel
temp1 = temp1 / (h1_cao * w1_rong)
temp2 = temp2 / (h2_cao * w2_rong)

#Tính hàm phân phối tích lũy (CDF) từ histogram
cdf1 = np.zeros(256)
cdf2 = np.zeros(256)

cdf1[0] = temp1[0]
for i in range(1, 256):
    cdf1[i] = cdf1[i-1] + temp1[i]

cdf2[0] = temp2[0]
for i in range(1, 256):
    cdf2[i] = cdf2[i-1] + temp2[i]

# Tạo ánh xạ từ ảnh nguồn đến ảnh tham chiếu
frame = np.zeros(256, dtype=int)
for i in range(256):
    min = float("inf")  #gán giá trị dương vô cùng
    min_val = 0
    for j in range(256):
        valu = np.abs(cdf2[j] - cdf1[i])
        if (valu < min):    #Nếu valu nhỏ hơn min gán min = valu, min_val = j
            min = valu
            min_val = j
    frame[i] = min_val

# Ánh xạ các giá trị pixel từ ảnh nguồn sang ảnh đã cân bằng
m_img = np.zeros_like(hinh1_xam, dtype = np.uint8)

for y in range(h1_cao):
    for x in range(w1_rong):
        pixel_value = hinh1_xam[y, x]
        m_img[y, x] = frame[pixel_value]

# Hiển thị ảnh nguồn, ảnh tham chiếu, và ảnh đã cân bằng
cv2.imshow('Anh goc', img1)
cv2.imshow('Anh tham chieu', img2)
cv2.imshow('Anh da can bang', m_img)
cv2.waitKey(0)

# Lược đồ của ảnh gốc
plt.hist(img1.ravel(), 256, [0, 256])
plt.title('Luoc do cua anh nguon')
plt.show()

# Lược đồ của ảnh tham chiếu
plt.hist(img2.ravel(), 256, [0, 256])
plt.title('Luoc do cua anh tham chieu')
plt.show()

# Hiển thị lược đồ của ảnh đã được cân bằng
plt.hist(m_img.ravel(), 256, [0, 256])
plt.title('Luoc do cua anh da can bang')
plt.show()