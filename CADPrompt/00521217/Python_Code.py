import cadquery as cq
base_diameter:float = 0.059646
base_height:float = 0.750036

top_diameter:float = 0.11752
top_height:float = 0.09375

base:cq.Workplane = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)
top:cq.Workplane = cq.Workplane("XY").circle(top_diameter/2).extrude(top_height) 

part:cq.Workplane = base.union(top.translate((0, 0, base_height)))

part = part.translate((0, 0, -base_height))
cq.exporters.export(part, 'Ground_Truth.stl')