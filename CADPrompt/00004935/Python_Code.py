import cadquery as cq
base_diameter:float = 1.5
base_height:float = 0.114796

top_diameter:float = 1.17857
top_height:float = 0.306123

base:cq.Workplane = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)
top:cq.Workplane = cq.Workplane("XY").circle(top_diameter/2).extrude(top_height) 

part:cq.Workplane = base.union(top.translate((0, 0, base_height)))

cq.exporters.export(part, 'Ground_Truth.stl')