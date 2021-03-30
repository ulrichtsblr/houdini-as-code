from hac import *


def generate_donut():
    gen = Generator()
    nod0 = gen.add_box(v=(1, 0, 0))
    nod1 = gen.add_sphere(v=(0, 1, 0))
    nod2 = gen.add_torus(v=(0, 0, 1))
    print(nod0.get_xyz())
    print(nod1.get_xyz())
    print(nod2.get_xyz())
    return None


def generate_camera():
    gen = Generator()
    cam = gen.add_camera(v=(0, 0, 10))
    print(cam.get_xyz())
    return None


def main():
    dag = DirectedAcyclicGraph()
    generate_donut()
    generate_camera()
    dag.render(schema="donut")
    return None


if __name__ == "__main__":
    main()
