import cadquery as cq

diameter:float = 1.2
cylinder_length:float = 0.25

sides:int = 6
length:float = 1.47802
extrude:float = 0.5

cylinder = cq.Workplane("XZ").cylinder(cylinder_length, diameter/2)
part:cq.Workplane = cylinder.faces("-Y").polygon(sides, length).workplane().extrude(extrude)

part = part.translate((0,cylinder_length/2+extrude,0))
part = part.rotate((1,0,0),(0,0,0),-90)

cq.exporters.export(part, 'Ground_Truth.stl')