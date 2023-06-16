# 主要程式程式碼參考網站（具體程式碼參考詳解見程式碼中的注釋）
1、
https://gitcode.net/mirrors/tmylla/ner_zh?utm_source=csdn_github_accelerator
2、
https://www.cnblogs.com/shona/p/11563112.html
3、
https://blog.csdn.net/misite_J/article/details/109036725?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-109036725-blog-128934139.pc_relevant_3mothn_strategy_recovery&spm=1001.2101.3001.4242.1&utm_relevant_index=3


## 使用model介绍

該模型主要應用於命名實體識別，即自然語言處理方面，但同樣適用於語音辨識與分類。 從一段自然語言文字或語音中找出相關實體，並標注出其位置以及類型，是資訊選取，問答系統，句法分析，機器翻譯等應用領域的重要基礎工具，具體應用我也是從網路上尋找的資源並自我學習的。



### 模型融合即voting.py程式應用說明

我使用的為最簡易的模型融合——投票系統（沒有經過任何人工處理，都是通過程式工作）。 我是通過普通hw2在kaggle中的多次提交結果將csv檔案命名為對應分數，方便最後的按照分數統計投票出每一項最合適的劃分。 具體的操作過程需要多個提交後的基礎prediction.csv以*（score）*.csv命名並與voting.py放置在同一目錄下（详细目录结构请见文件夹中的dir_show.png），運行voting.py，最終得出submission.csv，使我的分數從0.788左右提升到0.80004。
