script=donut.py
script2=blender.py
wdir=`pwd`
hdir="C:\Program Files\Side Effects Software\Houdini 18.5.449"


cd "$hdir"
source houdini_setup > /dev/null 2>&1

cd "$wdir"
hython $script
