# declare and initialize variables
script=donut.py
wdir=`pwd`
hdir=/opt/hfs18.5

# source houdini environment
cd $hdir
source houdini_setup > /dev/null 2>&1

# execute script
cd $wdir
hython $script
