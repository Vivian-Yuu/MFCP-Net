import cv2
import numpy as np
import matplotlib.pyplot as plt

def high_pass_filter(img, ratio=0.1):
    # 确保是RGB图像
    if len(img.shape) != 3 or img.shape[2] != 3:
        raise ValueError("Input image must be RGB.")

    rows, cols, _ = img.shape
    crow, ccol = rows // 2, cols // 2

    # 高频图像初始化
    high_freq_img = np.zeros_like(img)

    # 对每个通道处理
    for ch in range(3):
        # 1. 对通道进行傅里叶变换
        f = np.fft.fft2(img[:, :, ch])
        fshift = np.fft.fftshift(f)

        # 2. 创建掩码：低频区域设为0，其余为1
        mask = np.ones((rows, cols), np.uint8)
        r = int(ratio * rows / 2)
        c = int(ratio * cols / 2)
        mask[crow - r:crow + r, ccol - c:ccol + c] = 0

        # 3. 应用掩码
        fshift_high = fshift * mask

        # 4. 逆傅里叶变换
        f_ishift = np.fft.ifftshift(fshift_high)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)

        # 归一化到0-255
        img_back = np.clip(img_back, 0, 255)
        high_freq_img[:, :, ch] = img_back.astype(np.uint8)

    return high_freq_img

# 读取图像
img = cv2.imread('your_image.jpg')  # 替换成你的文件路径
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # OpenCV读取是BGR格式，转为RGB

# 提取高频信息
high_freq_result = high_pass_filter(img, ratio=0.1)

# 显示结果
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("High Frequency Image")
plt.imshow(high_freq_result)
plt.axis('
