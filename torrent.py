'''
bt种子trackers添加器

by 毕玉峰

411201060@qq.com

2019年06月11日 星期二
'''



import bencoder, os

def add_trcackers(filename):
    f = open('torrent/' + filename, "rb")  # 读入文件

    d = bencoder.decode(f.read())
    #print(d[b'announce-list'])
    trackers = 'track.txt' # 保存trackers的文本文档,可编辑,可自行添加trackers
    track_list = []

    with open(trackers) as f:
        for line in f:
            if len(line) > 1:
                l = line.rstrip()
                n = []
                n.append(l)

                track_list.append(n)
    #print(000, len(track_list))

    #print(len(track_list))
    a = track_list + d[b'announce-list']
    l2 = []
    for i in a:
        if i not in l2:
            l2.append(i)
    print(len(l2))
    d[b'announce-list'] = l2
    with open('torrent/' + filename, "wb") as n:
        n.write(bencoder.encode(d))  # 写入文件
    print('共',len(d[b'announce-list']), '个trackers.')



i = 0 # 初始化种子计数器
'''
遍历torrent文件夹,为所有种子添加trackers
'''

for filename in os.listdir('torrent'):
    if filename.endswith('.torrent'):
        i = i + 1
        add_trcackers(filename)
        print(i,'正在添加trackers...',filename)
print('共为',i,'个种子添加trackers.')