# import hou not required


def generate_object_network():
    # object network and primary geometries
    object_network = hou.node("/obj")
    sphere_geom = object_network.createNode("geo", "AbstractSphereGeometry")
    box_geom = object_network.createNode("geo", "AbstractBoxGeometry")
    torus_geom = object_network.createNode("geo", "AbstractTorusGeometry")
    
    # nodes
    sphere1 = sphere_geom.createNode("sphere", "sphere1")
    sphere2 = sphere_geom.createNode("sphere", "sphere2")
    sphere3 = sphere_geom.createNode("sphere", "sphere3")
    box1 = box_geom.createNode("box", "box1")
    box2 = box_geom.createNode("box", "box2")
    box3 = box_geom.createNode("box", "box3")
    torus1 = torus_geom.createNode("torus", "torus1")
    torus2 = torus_geom.createNode("torus", "torus2")
    torus3 = torus_geom.createNode("torus", "torus3")
    scatter1 = torus_geom.createNode("scatter", "scatter1")
    scatter1.setInput(0, torus1, 0)
    return None


def main():
    infile = "base_scene.hipnc"
    outfile = "base_scene_with-net.hipnc"
    hou.hipFile.load(infile)
    generate_object_network()
    hou.hipFile.save(outfile)
    return None

main()
