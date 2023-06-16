import os

import pandas as pd


def getfiles():
    filenames = os.listdir('D:\MachineL\hw2')
    scorelist = []
    filelist = []
    for name in filenames:
        if '.csv' in name:
            filelist.append(name)
            scorelist.append(float(name.replace('.csv', '')))
    return filelist, scorelist


if __name__ == '__main__':
    files, scores = getfiles()
    print(files, scores)
    picks = []
    labels = []
    ids = []
    for fname in files:
        picks.append(pd.read_csv(fname)['Class'])
    for id in range(527364):
        num = []
        for i in range(41):
            num.append(0)
        for i in range(len(picks)):  # 对于id号第i个模型的结果
            label = picks[i][id]
            num[label] += scores[i]
        labels.append(num.index(max(num)))

    with open('submission.csv', 'w') as f:
        f.write('Id,Class\n')
        for i in range(527364):
            f.write(str(i) + ',' + str(labels[i]) + '\n')
