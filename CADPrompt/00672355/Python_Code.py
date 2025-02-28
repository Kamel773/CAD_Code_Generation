import cadquery as cq

height:float = 0.475
diameter:float = 0.95

length:float = 0.7
width:float = 0.275
box_height:float = 0.075

part:cq.Workplane = (
    cq.Workplane("XZ")
    .cylinder(height,diameter/2)
    .faces("-Y")
    .workplane()
    .transformed((90,0,0),(0,0,width/2))
    .box(length, width, box_height)
)

part = part.translate((0,-height/2,0))
cq.exporters.export(part, 'Ground_Truth.stl')