# MFCP-Net
[RESIDE数据集](https://pan.baidu.com/share/init?surl=NqAaec3MFwFU9ZM2lfR_4w) 提取码：v8ku 

[SOTS数据集](https://drive.google.com/open?id=1qZlnJN4ybjunc2BGh6kjOUfFdVxuNS-P)

[模型](https://pan.baidu.com/s/1xlfk_FNEDJimDQlk8FLn1Q) 提取码：1234

## 摘要
图像去雾是计算机视觉中的关键问题。近年来，基于深度学习的端到端方法已成为主流，并取得了显著成效。然而，此类方法在高频信息的提取与利用方面仍存在不足，导致去雾图像在清晰度和真实感上表现有限。为此，本文提出一种基于多尺度特征协同感知的去冗余去雾网络（MFCP-Net），通过设计多特征协同感知模型（Multi-scale Feature Perception and Cooperation Model, MFPCM）与多特征自适应融合模型（Multi-feature Adaptive Fusion Model, MAFM），提升对高频信息的建模能力。具体而言，多特征协同感知模型包括高频信息感知模块和高频特征编码器。前者基于快速傅里叶变换将图像从空间域转换到频域，有效提取边缘、纹理等高频细节；后者结合多尺度处理对高频特征进行深度编码与重建。多特征自适应融合模型则引入通道注意力机制，自适应调整特征权重，突出关键高频信息，压制冗余和噪声，从而提升最终去雾图像的质量与细节保留能力。为了验证其有效性，与12种经典的图像去雾算法进行了对比实验。在SOTS数据集上，我们的平均峰值信噪比达到了34.77 dB，相比于性能第二的模型提升了2.9%。源代码可以在https://github.com/Vivian-Yuu/MFCP-Net获取。
