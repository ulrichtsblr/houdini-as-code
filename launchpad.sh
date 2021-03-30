# user parameters
script="main.py"
houdini_version="18.5.499"
operating_system="linux"

# initialize navigation
wdir=`pwd`
if [[ "$operating_system" -eq "linux" ]]
then
    hdir="/opt/hfs$houdini_version"
else
    if [[ "$operating_system" -eq "windows" ]]
    then
        hdir="C:\Program Files\Side Effects Software\Houdini $houdini_version"
    else
        echo "invalid operating system"
    fi
fi

# initialize houdini environment
cd "$hdir"
source houdini_setup > /dev/null 2>&1

# run hython script
cd "$wdir"
hython $script
