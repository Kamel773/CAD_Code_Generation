import cadquery as cq

arc:cq.Workplane = cq.Workplane("XZ").radiusArc((0.180047,0.18),0.18)
rect:cq.Workplane = cq.Workplane("XY").center(-0.0075/2,0).rect(0.0075,0.750037)

part:cq.Workplane = rect.sweep(arc).translate((0,0,0)).rotate((0,0,1),(0,0,0),180)
part = part.translate((0.180047,-0.75003/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')