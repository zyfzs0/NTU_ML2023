# 主要程式程式碼參考網站（具體程式碼參考詳解見程式碼中的注釋）
1、Change the network structure (increase the number of layers)
https://blog.csdn.net/qq_43613342/article/details/127018677?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168321094516800182172074%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168321094516800182172074&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-2-127018677-null-null.142^v86^insert_down1,239^v2^insert_chatgpt&utm_term=%E6%9D%8E%E5%AE%8F%E6%AF%85hw8&spm=1018.2226.3001.4187
2、Decoder auxiliary network
https://blog.csdn.net/weixin_46846685/article/details/127699597
3、resnet network
http://www.taodudu.cc/news/show-4804642.html
4、Residual network + Parameter settings
https://blog.csdn.net/iwill323/article/details/127919157
5、Decoder auxiliary network + format writting
https://blog.csdn.net/weixin_42369818/article/details/125292835?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168321094516800182172074%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168321094516800182172074&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-125292835-null-null.142^v86^insert_down1,239^v2^insert_chatgpt&utm_term=%E6%9D%8E%E5%AE%8F%E6%AF%85hw8&spm=1018.2226.3001.4187


## 使用model介绍

modify parameters
CNN model / ResNet model
reducing late dim 
more epoch
small batch size 
residual network
Auxiliary network


### 本次homework的特殊聲明（重要，尤其是第二點）
1、程式部分的編寫
本次工作由於一直上不到strong line且有點複雜，囙此我在最後參攷的網路資源較多，所以程式碼中的相關reference也都較多，我已經在各個部分都標明了相關的參攷網站，最終呈現的程式碼比較複雜，尤其是輔助網絡的加入（參攷了一比特網路程式博主的部落格），謝謝老師。
2、最终结果
由於我是參攷著網路上的資源進行輔助網絡aux = Auxiliary（）.cuda（）的編寫，囙此許多操作是與resnet模型並行操作，包括計算損失率和生成最後結果等，囙此最後會生成兩個文件prediction_ a.csv和prediction.csv。 我在所有輔助網絡模型的相關檔和程式都加了_ a的尾碼。 但是，我最後提交的是prediction_ a.csv文件作為最終結果，希望助教老師在驗證程式中也要使用prediction_ a.csv文件進行驗證。

 


