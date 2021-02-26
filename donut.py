def generate():
    torus_geom = hou.node("/obj").createNode("geo", "AbstractTorusGeometry")
    torus = torus_geom.createNode("torus", "donut")
    camera = hou.node("/obj").createNode("cam", "donutcamera")
    #print(len(camera.parmTuple))
    #v = hou.Vector3
    #v.z = 10
    #print(v.z)
    #camera.origin = v
    #print(camera.origin())
    print(dir(camera.parmTuple))
    #print(camera.parmTuple.tx)
    print(camera.parmTuple("t"))
    print(camera.parmTuple("t")[0])
    print(camera.parmTuple("t")[1])
    #print(dir(camera.parmTuple("t")[2]))
    camera.parmTuple("t")[2].set("10")
    print(camera.parmTuple("t").eval())
    #print(camera.showOrigin())
    #print(camera.localTransform())
    #print(hou.pwd())
    #print(hou.cd("/obj/donutcamera"))
    #print(hou.pwd())
    #n = hou.pwd()
    #t = hou.hmath.buildTranslate((1, 2, 3))
    #camera.setCookTransform(t)
    return None

def main():
    infile = "base_scene.hipnc"
    outfile = "donut.hipnc"
    hou.hipFile.load(infile)
    generate()
    hou.hipFile.save(outfile)
    return None

main()
#camera.parmTuple("t")
