from PIL import Image
import numpy as np
import time
import plotly.graph_objects as go
import plotly.express as px

MAX_BLACK_COLOR_NUM = 255
fig = go.Figure()


def getPixels(pic_path):
    pic = Image.open(pic_path)
    pic = pic.convert("L")
    pix = np.asarray(pic)
    return pix


def calc(pic_path):
    # 動態輸入圖片
    print(pic_path)
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
            if pix[item][item2] < MAX_BLACK_COLOR_NUM and last == item2 - 1:
                cnt += 1
                last = item2
            elif pix[item][item2] < MAX_BLACK_COLOR_NUM:
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
    print("")
    return data


_data = calc("Dataset/img1.jpg")
fig.add_trace(go.Scatter(
    x=[v[0] for v in _data],
    y=[v[1] for v in _data],
    mode='markers',
    name='markers'
))

_data = calc("Dataset/img2.jpg")
fig.add_trace(go.Scatter(
    x=[v[0] for v in _data],
    y=[v[1] for v in _data],
    mode='markers',
    name='markers'
))

_data = calc("Dataset/img3.jpg")
fig.add_trace(go.Scatter(
    x=[v[0] for v in _data],
    y=[v[1] for v in _data],
    mode='markers',
    name='markers'
))

_data = calc("Dataset/img4.jpg")
fig.add_trace(go.Scatter(
    x=[v[0] for v in _data],
    y=[v[1] for v in _data],
    mode='markers',
    name='markers'
))

fig.update_layout(
    title="指紋清晰度實驗",
    xaxis_title="灰階值 (越大越白)",
    yaxis_title="數量",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig.show()
