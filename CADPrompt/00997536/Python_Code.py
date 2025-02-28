import cadquery as cq

diameter:float = 0.988192
height:float = 0.75
sides:float = 8
inner_diameter:float = 0.79436

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

octagon:cq.Workplane = (
    cq.Workplane("XY")
    .polygon(sides, inner_diameter)
    .extrude(height)
    .translate((0, 0, -height/2))
    .rotate((0,0,1),(0,0,0),22.5)
)

part:cq.Workplane = cylinder.cut(octagon).translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')