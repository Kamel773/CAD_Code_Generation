import cadquery as cq

length:float = 0.990099
width:float = 0.415842
height:float = 0.990099
diameter:float = 0.517113
hole_diameter:float = diameter - 0.022623*2
extrude:float = 0.334158
z_offset:float = 0.025308

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("-Y")
    .workplane(offset=0)
    .center(0,-z_offset)
    .circle(diameter/2)
    .extrude(extrude)
    .faces("<Y")
    .hole(hole_diameter)
).translate((0,-width/2,z_offset))

cq.exporters.export(part, 'Ground_Truth.stl')