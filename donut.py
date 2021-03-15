def generate():
    torus_geom = hou.node("/obj").createNode("geo", "AbstractTorusGeometry")
    torus = torus_geom.createNode("torus", "donut")
    rop_network = torus_geom.createNode("ropnet","Rop_network")
    opengl = rop_network.createNode("opengl","openGL_rendernode")
    camera = hou.node("/obj").createNode("cam", "donutcamera")
    opengl.parm("camera").set("/obj/donutcamera")
    opengl.parm("picture").set("$HIP/render.png")
    camera.parmTuple("t")[2].set("10")
    print(camera.parmTuple("t").eval())
    return None
def render():
    opengl_render = hou.node("/obj/AbstractTorusGeometry/Rop_network/openGL_rendernode")
    opengl_render.parm("execute").pressButton()

def exportobj():
    torus_geom = hou.node("/obj/AbstractTorusGeometry")
    torus = hou.node("/obj/AbstractTorusGeometry/donut")
    file = torus_geom.createNode("file","export")
    #connect inputs first
    file.setInput(0,torus,0)
    file.parm("filemode").set("write")
    file.parm("file").set("$HIP/donut.obj")
    null = torus_geom.createNode("null","Null")
    null.setInput(0,file,0)
    null.setDisplayFlag(1)
    file.parm("reload").pressButton()

def main():
    infile = "base_scene.hiplc"
    outfile = "donut.hiplc"
    hou.hipFile.load(infile)
    generate()
    render()
    exportobj()
    hou.hipFile.save(outfile)
    return None

main()
#camera.parmTuple("t")
