import cadquery as cq

length:float = 0.19091
width:float = 0.01705
height:float = 0.75

part:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part = part.translate((length/2, -width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')