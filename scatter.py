from PIL import Image
import numpy as np
import time
import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure()


def getPixels(pic_path):
    pic = Image.open(pic_path)
    pic = pic.convert("L")
    pix = np.asarray(pic)
    return pix


def calc(pic_path):
    # 動態輸入圖片

    # 開啟一張圖片
    pic = Image.open(pic_path)

    # 轉為灰階模式
    pic = pic.convert("L")

    # 顯示圖片
    # pic.show()
    # print(pic.mode)

    # 讀取圖片 0是黑，255是白
    pix = np.asarray(pic)
    start_time = time.time()
    arr = []
    cnt = 0
    for item in range(len(pix)):
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
                cnt = 1
                last = item2
    data = {}
    for item in range(256):
        if arr.count(item):
            data[item] = arr.count(item)

    data = sorted(data.items(), key=lambda d: d[1])
    print("--- %s seconds ---" % (time.time() - start_time))
    return data


fig.add_trace(go.Scatter(
    x=[v[0] for v in calc("img1.jpg")],
    y=[v[1] for v in calc("img1.jpg")],
    mode='markers',
    name='markers'
))
fig.add_trace(go.Scatter(
    x=[v[0] for v in calc("img2.jpg")],
    y=[v[1] for v in calc("img2.jpg")],
    mode='markers',
    name='markers'
))
fig.add_trace(go.Scatter(
    x=[v[0] for v in calc("img3.jpg")],
    y=[v[1] for v in calc("img3.jpg")],
    mode='markers',
    name='markers'
))
fig.add_trace(go.Scatter(
    x=[v[0] for v in calc("img4.jpg")],
    y=[v[1] for v in calc("img4.jpg")],
    mode='markers',
    name='markers'
))
fig.show()
