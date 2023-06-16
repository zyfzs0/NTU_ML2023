# 主要程式程式碼參考網站（具體程式碼參考詳解見程式碼中的注釋）
1、Dynamical lambs  （動態調整lamb）
https://blog.csdn.net/qq_43613342/article/details/127033097
chatgpt
2、two-step training method of DIRT (DIRT的兩步訓練方法) 
https://blog.csdn.net/iwill323/article/details/128067213
https://arxiv.org/abs/1802.08735
3、Visualization （視覺化）
https://blog.csdn.net/iwill323/article/details/128067213

## 使用model介绍

modify parameters
Dynamical lambs
two-step training method of DIRT
Visualization

### 本次homework的特殊聲明（重要）
1、model部分的选择
本次工作我使用了DIRT的兩步訓練法，所以相當於在這部分程式碼中進行了兩次train，依靠的是前一個train後形成的teacher網絡，並不是預訓練模型！！！ 特此說明，怕引起誤會

 


