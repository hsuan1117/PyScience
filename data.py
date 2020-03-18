from PIL import Image
import numpy as np

#開啟一張圖片
pic = Image.open("img1.jpg")
pic = pic.convert("L")
pic.show()
print(pic.mode)
pix = np.asarray(pic)
idx = 0
with open('output.txt', 'w') as f:
    for item in range(len(pix)):
        for item2 in range(len(pix[item])):
            if pix[item][item2] < 200:
                print("Found ({},{}) : {}".format(item2,item,pix[item][item2]))
                idx+=1
            f.write("{} ".format(pix[item][item2]))
        f.write("\r\n")
print(idx)

#print(len(pix))
#print(len(pix[0]))
