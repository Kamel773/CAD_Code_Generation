import cadquery as cq

diameter:float = 0.321427
cylinder_length:float = 0.75025

sides:int = 6
length:float = 0.61859
extrude:float = 0.214286

cylinder = cq.Workplane("XZ").cylinder(cylinder_length, diameter/2)
part:cq.Workplane = cylinder.faces("-Y").polygon(sides, length).workplane().extrude(extrude)

part = part.translate((0,cylinder_length/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')