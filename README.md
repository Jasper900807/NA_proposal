數值分析提案 – 插值法的程式實作與影像進階應用

組員名單
王家衞
吳宗桓
蔣承燁
蔡承翰

一、動機簡介
上課時有教到拉格朗日插值法可以找到資料間缺失的數據，再加上之前有利用SVD實作影像壓縮，所以想了解是否能用插值法進行影像放大。

二、研究方法
Part A：議題說明
我們小組要探討的議題是將二維圖片做放大，更精確的說，是透過原圖片給定的像素點，去找到放大圖片後缺失點的值。因此，我們可以透過插值法去預測缺失點的值為何，並從一維數線上的插值法做發想，延伸到二維平面上，思考該如何使用插值法取得放大圖片的缺失點值。

Part B：問題結論猜測
由於拉格朗日插值法存在龍格現象，亦即高次多項式插值不一定總能提高插值的準確度，因此用來預測插值多項式的點應該是需要經過挑選的；另一方面，由於二維圖片存在兩軸，若僅根據其中一軸來推測缺失點的值，會導致缺失點在另一軸上的關聯性降低，因此我們推測：同時考慮兩軸上取樣點來進行插值，會得到比較好的結果。

Part C：進行步驟
在一維的數線上透過已知的取樣點去預測遺失點的值，以達到增加點的總數量，並透過視覺化來發想二維平面該如何插值。
延伸到二維平面上，先固定一軸並放大另一軸，觀察插值前後圖片的差異。
思考當圖片兩軸同時放大時，應如何插值才能達到最好的放大效果。
比較不同插值方法，並得出結論與可能的改進方法。

三、數學模型
實作使用程式：python
使用套件：numpy、matplotlib、opencv-python、math

實作方法：
最近鄰插法
拉格朗日插值法
全數據生產函數
單線性局部數據產生函數
雙線性局部數據產生函數


四、參考資料
数字图像处理笔记二 - 图片缩放(最近邻插值(Nearest Neighbor interpolation))-腾讯云开发者社区-腾讯云 (tencent.com)
图像处理之双线性插值法_双线性差值-CSDN博客
SVD 壓縮照片技術結合超解析度插值方法的探討
拉格朗日插值（Lagrange）图像缩放_图像拉格朗日插值法-CSDN博客
