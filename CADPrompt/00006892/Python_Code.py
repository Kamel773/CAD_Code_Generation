import cadquery as cq

length:float = 1.5
width:float = 0.52105
height:float = 0.15789

semi_circle_diameter:float = (length/2) + 0.067116*2  
semi_circle_radius:float = semi_circle_diameter/2

prism:cq.Workplane = cq.Workplane("XY").box(length, width, height)
semi_circle:cq.Workplane = (
    cq.Workplane()
    .threePointArc((-semi_circle_radius, semi_circle_radius), (0, semi_circle_diameter))
    .close()
    .extrude(height)
    .translate((0, -semi_circle_radius, -height/2))
    .rotate((0,0,1),(0,0,0),-90)
)

part:cq.Workplane = prism.translate((0, -width/2,0)).cut(semi_circle)

part = part.translate((0, -0.104805, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')