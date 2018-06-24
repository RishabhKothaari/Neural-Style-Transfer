"""
Helper script to create gif.
"""
import imageio
from os import listdir
from os.path import isfile, join

mypath = './outputdir/'
fileNames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("only files", fileNames)
print("files", type(fileNames))
files = sorted(fileNames)
print("only files", fileNames)
images = []
print("files", files)
for fileName in files:
    images.append(imageio.imread('./outputs/15/'+fileName))
# end
imageio.mimsave('./outputdir/gifname.gif', images, format='GIF', duration=1.3)
