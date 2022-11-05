
import requests
from PIL import Image
import random
from io import BytesIO

x = 16
y = 16

def make(t):

    url = "http://ciaccodavi.de/qbdp/acg/alchemymod.php?id=" +str(random.randint(1000000000, 9999999999))
    img = requests.get(url, stream=True)


    i = Image.open(BytesIO(img.content))





    function = open("Your/Entire/Path/To/A/Existing/Datapack/With/A/functions/Folder"+str(t)+".mcfunction","w")
    function.truncate(0)

    for k in range(0,int(i.width)):
        for j in range(0,int(i.height)):
            if i.getpixel((k,j)) == (255,255,255):
                function.write('particle dust 1.0 0.0 0.0 1.0 '+ "^"+str((k/(128/x))-(x/2)) +" ^ ^" +str((j/(128/y))-(y/2)) + " 0.0 0.0 0.0 0.1 1\n")
                #function.write('particle lava ' + "^" + str((k / (128 / x)) - (x / 2)) + " ^ ^" + str((j / (128 / y)) - (y / 2)) + " 0.0 0.0 0.0 0.1 1\n")
                





for i in range(0,4):
    make(i)
