## face-evaluate 人脸识别测试数据集

#### 1. 来源：

西方人脸  https://github.com/ZhaoJ9014/face.evoLVe.PyTorch#Data-Zoo CASIA-WebFace

东方人脸A https://github.com/X-zhangyang/Real-World-Masked-Face-Dataset RMFD

东方人脸B https://github.com/deepinsight/insightface/wiki/Dataset-Zoo#asian-celeb-94k-ids28m-images8-recommend Asian-Celeb

#### 2. 方法：

每人取20张可定位到人脸的照片（使用dlib检测人脸），10张用于训练，10张用于识别测试。

#### 3. 文件夹说明：

| 文件夹         | 说明             |
| -------------- | ---------------- |
| train2 / test2 | 东方人脸A，50人  |
| train3 / test3 | 西方人脸，50人   |
| train4 / test4 | 东方人脸B，50人  |
| train6 / test6 | 东方人脸B，      |
| train8 / test8 | 东方人脸A，412人 |
| train9 / test9 | 西方人脸，539人  |

