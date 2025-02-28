import cadquery as cq

b_length:float = 0.830095
b_width:float = 0.830095
b_height:float = 0.1703531

base:cq.Workplane = cq.Workplane("XY").box(b_length, b_width, b_height)

c_length:float = 0.676879
c_width:float = 0.676879
c_height:float = 0.105467
cut_base:cq.Workplane = cq.Workplane("XY").box(c_length, c_width, c_height)

tube_diameter:float = 0.327945
tube:cq.Workplane = cq.Workplane("XY").cylinder(c_height, tube_diameter/2)

stud_diameter:float = 0.25606
stud_height:float = 0.094448
stud:cq.Workplane = cq.Workplane("XY").cylinder(stud_height, stud_diameter/2)

def add_stud(loc) -> cq.Shape:
    global stud
    global stud_height
    return stud.translate((0,0,stud_height/2)).val().located(loc) #type: ignore

part:cq.Workplane = (
    cq.Workplane("XY")
    .add(base)
    .cut(cut_base.translate((0,0,-b_height/2+c_height/2)))
    .union(tube.translate((0,0,-b_height/2+c_height/2)))
    .faces(">Z")
    .edges()
    .toPending()
    .offset2D(-0.21+0.003551)
    .vertices()
    .eachpoint(add_stud, combine=True)
)

part = part.translate((0.080095,-0.079879,b_height/2))

cq.exporters.export(part, 'Ground_Truth.stl')