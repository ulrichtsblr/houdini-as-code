import subprocess


def counter():
    count = 0
    for i in range(0,15):
        if i%2 == 0:
            count +=1
            print(i)
        
    print(f"there are {count} even numbers")
    print("this i smy second script boys")
    #open blender
    subprocess.call(['C:\Program Files\Blender Foundation\Blender 2.91\\blender.exe'])
counter()