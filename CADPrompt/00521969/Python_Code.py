import cadquery as cq

length:float = 0.74999
width:float =  0.73843
height:float = 0.11078
fillet:float = 0.038

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)
rectangle_two = cq.Workplane("XY").box(length, width*2, height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle).translate((-length/2, width/2, 0))
    .cut(rectangle_two.translate((0, width, 0)).rotate((0,0,1),(0,0,0),-0.857).translate((length/2, 0, 0)))
).translate((length, 0, height/2)).edges("|Z").fillet(fillet)

cq.exporters.export(part, 'Ground_Truth.stl')