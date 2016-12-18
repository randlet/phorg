import glob
import os
import shutil
import sys

import piexif


if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
    print("Usage: phorg /path/to/dir/to/organize")
    exit()

root = sys.argv[1]

dirname = "organized"
outdir = os.path.join(root, dirname)
if not os.path.exists(outdir):
    os.mkdir(outdir)


DT_ORIG = 36867
globber = os.path.join(root, "*jpg")


for f in glob.glob(globber):

    exif = piexif.load(f)
    try:
        date = exif['Exif'][DT_ORIG].split(" ")[0].replace(":", "-")
    except:
        print("Couldn't process %s" % f)
        continue

    datedir =  os.path.join(outdir, date)
    if not os.path.isdir(datedir):
        os.mkdir(datedir)

    shutil.move(f, os.path.join(datedir, os.path.basename(f)))




