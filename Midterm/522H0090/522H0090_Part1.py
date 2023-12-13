#Hàm mean()
import statistics

data_1 = [2, 4, 6, 8, 10]
average = statistics.mean(data_1)
print("Giá trị trung bình: ", average)
print()

#Hàm fmean()
import statistics

data_2 = [9.0, 8.0, 8.5, 7.0]
weights = [0.1, 0.2, 0.2, 0.5] 
DTB = statistics.fmean(data_2, weights)
print("Điểm trung bình môn hoc: ", DTB)
print()

#Hàm geometric_mean()
import statistics

data_3 = [6, 12, 24]
GTTBHH = statistics.geometric_mean(data_3)
print("Giá trị trung bình hình học: ", round(GTTBHH))
print()

#Hàm harmonic_mean()
import statistics

data_4 = [20, 30]
GTTBDH = statistics.harmonic_mean(data_4)
print("Giá trị trung bình điều hòa: ", (GTTBDH))
print()

#Hàm median()
import statistics

data_5 = [1, 3, 6, 4, 9]
GTTV = statistics.median(data_5)
print("Giá trị trung vị: ", GTTV)
print()

#Hàm meadian_low()
import statistics

data_6 = [2, 3, 5, 4, 6, 8]
GTTVT = statistics.median_low(data_6)
print("Giá trị trung vị thấp: ", GTTVT)
print()

#Hàm meadian_high()
import statistics

data_7 = [2, 3, 5, 4, 6, 8]
GTTVC = statistics.median_high(data_7)
print("Giá trị trung vị cao: ", GTTVC)
print()

#Hàm meadian_grouped()
import statistics

data_8 = [1.5, 2.5, 3.5, 4.5, 5.5]
interval = 2
GTTVN = statistics.median_grouped(data_8, interval) 
print("Giá trị trung vị theo nhóm: ", GTTVN)
print()

#Hàm mode()
import statistics

data_9 = [2, 2, 4, 5, 8, 9, 4, 3]
GTXHNN = statistics.mode(data_9)
print("Giá trị xuất hiện nhiều nhất:", GTXHNN)
print()

#Hàm multimode()
import statistics

data_10 = [1, 3, 2, 3, 3, 4, 5, 4, 4]
DS_GTXHNN = statistics.multimode(data_10)
print("Danh sách giá trị xuất hiện nhiều nhất:", DS_GTXHNN)
print()

#Hàm quatiles()
import statistics

data_11 = [15, 25, 35, 45, 55, 65]
quantiles = statistics.quantiles(data_11, n = 4, method = 'exclusive')
print("Giá trị phân vị: ",quantiles)
print()

#Hàm pstdev()
import statistics

data_12 = [2, 4, 6, 8]
DLC = statistics.pstdev(data_12)
print("Độ lệch chuẩn của toàn bộ: ",DLC)
print()

#Hàm pvariance()
import statistics

data_13 = [2, 4, 6, 8]
PS = statistics.pvariance(data_13)
print("Phương sai (population variance): ",PS)
print()

#Hàm stdev()
import statistics

data_14 = [2, 4, 6, 8]
DLC2 = statistics.stdev(data_14, xbar = None)
print("Độ lệch chuẩn của mẫu cụ thể: ",DLC2)
print()

#Hàm variance()
import statistics

data_15 = [2, 4, 6, 8]
PS2 = statistics.variance(data_15)
print("Phương sai (sample variance): ",PS2)
print()

#Hàm covariance()
import statistics

x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]
HPS = statistics.covariance(x, y)
print("Hiệp phương sai: ", HPS)
print()

#Hàm correlation()
import statistics

x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]
HSTQ = statistics.correlation(x, y)
print("Hệ số tương quan: ", HSTQ)
print()

#Hàm linear_regression()
import statistics

x = [2, 4, 6, 8, 10]
y = [1, 3, 5, 7, 9]
HQTT = statistics.linear_regression(x, y, proportional=False)
print("Hệ số góc (slope): ", HQTT.slope)
print("Hệ số giao (intercept): ", HQTT.intercept)
print()

#NormalDist
#Hàm from_sample()
from statistics import NormalDist
data = [1, 3, 5, 7, 9]
nd1 = NormalDist.from_samples(data)
TB = nd1.mean
DC = nd1.stdev
print("Giá trị trung bình: ", TB)
print("Độ lệch chuẩn: ", DC)
print()

#Hàm sample()
from statistics import NormalDist
nd2 = NormalDist(mu = 10, sigma = 2)
n = 2
samples = nd2.samples(n)
print("Samples: ", samples)
print()

#Hàm pdf()
from statistics import NormalDist
nd3 = NormalDist(mu = 10, sigma = 2)
x = 3
pdf = nd3.pdf(x)
print("PDF: ", pdf)
print()

#Hàm cdf()
from statistics import NormalDist
nd4 = NormalDist(mu = 10, sigma = 2)
x = 3
cdf = nd4.cdf(x)
print("CDF: ", cdf)
print()

#Hàm inv_cdf()
from statistics import NormalDist
nd5 = NormalDist(mu = 10, sigma = 2)
p = 0.2
cdf = nd4.inv_cdf(p)
print("Inverse CDF: ", cdf)
print()

#Hàm overlap()
from statistics import NormalDist
nd6a = NormalDist(mu = 10, sigma = 2)
nd6b = NormalDist(mu = 15, sigma = 2)
overlap = nd6a.overlap(nd6b)
print("Overlap: ", overlap)
print()

#Hàm quantiles
from statistics import NormalDist
nd7 = NormalDist(mu = 10, sigma = 2)
n = 4
qua = nd7.quantiles(n)
print("Quantiles: ", qua)
print()

#Hàm zscose()
from statistics import NormalDist
nd8 = NormalDist(mu = 5, sigma = 2)
x = 10
zscore = nd8.zscore(x)
print("Zscore: ", zscore)
print()