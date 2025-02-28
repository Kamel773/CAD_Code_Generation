import cadquery as cq

base_diameter:float = 0.825
base_height:float = 0.01125

top_diameter:float = base_diameter - 0.0375*2
top_height:float = 0.73875

cut_diameter:float  = top_diameter - 0.05626*2
cut_height:float  = base_height + top_height

base:cq.Workplane = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)
top:cq.Workplane = cq.Workplane("XY").circle(top_diameter/2).extrude(top_height)
cut:cq.Workplane = cq.Workplane("XY").circle(cut_diameter/2).extrude(cut_height)

part:cq.Workplane = (
    base
    .union(top.translate((0, 0, base_height)))
    .cut(cut)
)

cq.exporters.export(part, 'Ground_Truth.stl')