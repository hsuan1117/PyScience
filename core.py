from PIL import Image
import numpy as np
import time
import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure()

start_time = time.time()
# 動態輸入圖片
pic_path = "Dataset/甲.jpg"  # input("Image path?")

# 開啟一張圖片
pic = Image.open(pic_path)

# 轉為灰階模式
pic = pic.convert("L")

# 顯示圖片
# pic.show()
# print(pic.mode)

# 讀取圖片 0是黑，255是白
pix = np.asarray(pic)

print("以下列出非白色的座標")
idx = 0
with open('Output/output_{}.txt'.format(pic_path.split("/")[len(pic_path.split("/"))-1]), 'w') as f:
    for item in range(len(pix)):
        for item2 in range(len(pix[item])):
            if pix[item][item2] < 200 :
                print("Found ({},{}) : {}".format(item2, item, pix[item][item2]))
                idx += 1
            f.write("{} ".format(pix[item][item2]))
        f.write("\r\n")
print("共{}個座標點".format(idx))
print("\n以下列出每列黑色長度持續多長")
arr = []
cnt = 0
for item in range(len(pix)):
    toPrint = []
    cnt2 = 0
    last = -1

    for item2 in range(len(pix[item])):
        if pix[item][item2] < 200 and last == item2 - 1:
            cnt += 1
            last = item2
        elif pix[item][item2] < 200:
            if cnt != 0:
                cnt2 += 1
                arr.append(pix[item][item2])
                toPrint.append(cnt)
            cnt = 1
            last = item2

    if toPrint :
        print("第{}列 ".format(item), end="")
        for iit in toPrint:
            print("共{}長".format(iit), end=" ")
        print("({})".format(cnt2))

print("\n以下列出每個顏色共出現過幾次")
data = {}
for item in range(256):
    if arr.count(item):
        data[item] = arr.count(item)
        print("{} => {}個".format(item, arr.count(item)))

data = sorted(data.items(), key=lambda d: d[1])
print("\n以下列出每個顏色共出現過幾次(以次數排序)")
for item in range(len(data)):
    print("{} => {}個".format(data[item][0],data[item][1]))

print("--- %s seconds ---" % (time.time() - start_time))

fig.add_trace(go.Scatter(
    x=[v[0] for v in data],
    y=[v[1] for v in data],
    mode='markers',
    name='markers'
))
fig.show()