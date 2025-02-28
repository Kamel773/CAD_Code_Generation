import cadquery as cq

height:float = 0.010714
diameter:float = 1.5
hole_diameter:float = diameter - 0.171429*2

ring:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
)

cut_diameter:float = 0.105429
center_offset:float = diameter - hole_diameter

cut_circles:cq.Workplane = (
    cq.Workplane("XY")
    .polarArray(
        radius = diameter/2 - center_offset/4, 
        startAngle = 0, 
        angle = 360, 
        count = 3
    ).cylinder(height,cut_diameter/2)
)

part:cq.Workplane = ring.cut(cut_circles)

part = part.rotate((0,0,1),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')