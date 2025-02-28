import cadquery as cq

width:float = 0.75
diameter:float = 0.249945
padding:float = 0.125404

cylinder:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter/2)

part = cylinder.cut(cylinder.translate((0,0,padding)))
part = part.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')