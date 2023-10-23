## 灰階

import numpy as np
import cv2

# 放大倍率
Magni = 3

# 最近鄰插值法
def nearest_neighbour(src, dst_shape):
    # 獲取原圖大小
    src_height, src_width = src.shape[0], src.shape[1]
    # 計算新圖大小
    dst_height, dst_width = dst_shape[0], dst_shape[1]

    dst = np.zeros(shape = (dst_height, dst_width), dtype=np.uint8)
    for dst_x in range(dst_height):
        for dst_y in range(dst_width):
            # 尋找對應座標
            src_x = dst_x * (src_width/dst_width)
            src_y = dst_y * (src_height/dst_height)
            
            # 無條件捨去
            src_x = int(src_x)             
            src_y = int(src_y)

            # 插值
            dst[dst_x, dst_y] = src[src_x, src_y]
    return dst


src = cv2.imread("/project/NA_proposal/img3.png", cv2.IMREAD_GRAYSCALE)
dst = nearest_neighbour(src, dst_shape=(src.shape[0]*Magni, src.shape[1]*Magni))

# 顯示

cv2.namedWindow('src', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('src', src.shape[1], src.shape[0])
cv2.imshow("src",src) 
cv2.namedWindow('dst', cv2.WINDOW_NORMAL) 
cv2.resizeWindow('dst', dst.shape[1], dst.shape[0])
cv2.imshow("dst",dst)
cv2.waitKey(0)
