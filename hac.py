import hou
import os

class Node:


    def __init__(self, node):
        if node == "camera":
            self.node = (
                hou.node("/obj")
                .createNode("cam", "CameraInstance")
            )
        if node == "box":
            self.node = (
                hou.node("/obj")
                .createNode("geo", "AbstractBoxGeometry")
                .createNode("box", "BoxInstance")
            )
        if node == "sphere":
            self.node = (
                hou.node("/obj")
                .createNode("geo", "AbstractSphereGeometry")
                .createNode("sphere", "SphereInstance")
            )
        if node == "torus":
            self.node = (
                hou.node("/obj")
                .createNode("geo", "AbstractTorusGeometry")
                .createNode("torus", "TorusInstance")
            )
        return None


    def set_xyz(self, v):
        self.node.parmTuple("t")[0].set(str(v[0]))
        self.node.parmTuple("t")[1].set(str(v[1]))
        self.node.parmTuple("t")[2].set(str(v[2]))
        return None


    def get_xyz(self):
        xyz = self.node.parmTuple("t").eval()
        return xyz


class Generator:


    def __init__(self):
        return None


    def add_camera(self, v=(0, 0, 0)):
        node = Node("camera")
        node.set_xyz(v)
        return node


    def add_box(self, v=(0, 0, 0)):
        node = Node("box")
        node.set_xyz(v)
        return node


    def add_sphere(self, v=(0, 0, 0)):
        node = Node("sphere")
        node.set_xyz(v)
        return node


    def add_torus(self, v=(0, 0, 0)):
        node = Node("torus")
        node.set_xyz(v)
        return node


class DirectedAcyclicGraph:


    def __init__(self, scene=None):
        if not scene:
            scene = os.path.join("scenes", "seed.hipnc")
        hou.hipFile.load(scene)
        return None


    def export_png(self, schema):
        opengl = (
            hou.node("/obj")
            .createNode("ropnet","RopNetInstance")
            .createNode("opengl","OpenGLInstance")
        )
        opengl.parm("camera").set("/obj/CameraInstance")
        opengl.parm("picture").set("$HIP/{}.png".format(schema))
        opengl.parm("execute").pressButton()
        return None


    def export_hip(self, schema):
        hou.hipFile.save(os.path.join("scenes", "{}.hipnc".format(schema)))
        return None


    def render(self, schema="schema"):
        self.export_png(schema)
        self.export_hip(schema)
        return None


###############################################################################


# def generate_object_network():
#     object_network = hou.node("/obj")
#     torus_geom = object_network.createNode("geo", "AbstractTorusGeometry")
#     scatter_instance = torus_geom.createNode("scatter", "scatter1")
#     scatter_instance.setInput(0, torus_instance, 0)
#     return None


# def export_obj(self):
#     torus_geom = hou.node("/obj/AbstractTorusGeometry")
#     torus = hou.node("/obj/AbstractTorusGeometry/donut")
#     file = torus_geom.createNode("file","export")
#     #connect inputs first
#     file.setInput(0,torus,0)
#     file.parm("filemode").set("write")
#     file.parm("file").set("$HIP/donut.obj")
#     null = torus_geom.createNode("null","Null")
#     null.setInput(0,file,0)
#     null.setDisplayFlag(1)
#     file.parm("reload").pressButton()
#     return None
