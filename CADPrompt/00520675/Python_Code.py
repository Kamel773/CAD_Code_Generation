import cadquery as cq

diameter:float = 1.5
height:float = 0.6
cut_distance:float = 0.075
part:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2).faces("Z").shell(-cut_distance)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')