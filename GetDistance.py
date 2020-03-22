import numpy as np
import PIL.Image as img
import plotly

MAX_BLACK_COLOR_CODE = 200

def cango(x):
    # debug
    """
    if x == 0:
        return 0
    else:
        return 1
    """
    if x < MAX_BLACK_COLOR_CODE:
        return 1
    else:
        return 0


def getDistance(pic_path="Dataset/img1.jpg"):
    pic = img.open(pic_path)
    pic = pic.convert("L")
    pic = np.asarray(pic)
    total = []
    total2 = []
    # debug
    """
    pic = [
        [0,0,1,1,1,0,1,0,0,0,0,1,1,0]
    ]
    """

    for i in range(len(pic)):
        # 持續長度
        arr = []

        # 間隔長度
        arr2 = []

        inside = False
        start = 0
        end = 0
        first = True
        for j in range(len(pic[i])):
            if j == len(pic[i])-1:
                if cango(pic[i][j]):
                    arr.append(end-start+1)
                    total.append(end-start+1)
            elif j == 0:
                if cango(pic[i][j]):
                    start = j
                    if not cango(pic[i][j+1]):
                        arr.append(1)
                        total.append(1)
            else:
                if cango(pic[i][j]):
                    if not cango(pic[i][j-1]):
                        start = j
                        if first:
                            first = False
                        else:
                            arr2.append(start-end-1)
                            total2.append(start-end-1)
                    if not cango(pic[i][j+1]):
                        end = j
                        arr.append(end-start+1)
                        total.append(end-start+1)
            # print("{} {} {}".format(j,start,end))
        for i in range(len(arr)):
            if not i == len(arr)-1:
                print("[{:03d}] <-- {:03d} --> ".format(arr[i],arr2[i]),end="")
            else:
                print("[{:03d}]".format(arr[i]))
    print("===寬度===")
    print("平均  {}".format(np.mean(total)))
    print("標準差 {}".format(np.std(total)))
    print("眾數 {}".format(np.argmax(np.bincount(total))))
    print("四分位數 {} {} {}".format(*np.percentile(total, [25, 50, 75])))
    print("")
    print("===間隔===")
    print("平均 {}".format(np.mean(total2)))
    print("標準差 {}".format(np.std(total2)))
    print("眾數 {}".format(np.argmax(np.bincount(total2))))
    print("四分位數 {} {} {}".format(*np.percentile(total2, [25, 50, 75])))


getDistance("Dataset/img3.jpg")