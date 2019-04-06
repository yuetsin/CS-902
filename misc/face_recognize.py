from PIL import Image
from math import log
imgList = []
Pixels = []
avgPixels = []
deltaE = 1.0
pictNum = 17
for i in range(1, pictNum + 1):
    imgList.append(Image.open(
        "/resources/img%d.png" % i))
    imgList[i-1] = imgList[i-1].convert('L')
    for m in range(0, 100):
        for n in range(0, 100):
            x = imgList[i - 1].getpixel((m, n))
            Pixels.append(x/255.0)

for i in range(10000):
    sumPixels = 0
    for j in range(pictNum):
        sumPixels += Pixels[i + j * 10000]
    avgPixels.append(sumPixels/pictNum/255.0)

for i in range(10000):
    for j in range(pictNum):
        deltaE *= 1.01 ** (abs(Pixels[i + j * 10000] - avgPixels[i]))


newImg = Image.new("L", (100, 100), (0))
for i in range(100):
    for j in range(100):
        newImg.putpixel((i, j), int(avgPixels[i * 100 + j] * 255))
# newImg.show()
deltaE = deltaE ** (1/17.0)
# Already gotten the people face resources.
# Now we will do some adjustments
# print avgPixels
# print deltaE

detectPicPath = raw_input("Please enter the filename of your picture: >>> ")
detectPic = Image.open(detectPicPath)
detectPic = detectPic.convert('L')
detectPic = detectPic.resize((100, 100))
currDelta = 1.0
for i in range(100):
    for j in range(100):
        currDelta *= 1.01 ** (abs(detectPic.getpixel((i, j)) /
                                  255.0 - avgPixels[i * 100 + j]))
# print currDelta, deltaE
if (log(currDelta) - log(deltaE))/log(deltaE) <= 0.4:
    print "Yes, it's a face!"
    # print 'delta', (log(deltaE) - log(currDelta))/log(deltaE)
else:
    print "No, it's not a face!"
