import cadquery as cq

length:float = 1.5
width:float = 0.017559
height:float = 0.546823

diameter:float = 0.301003
top_padding:float = 0.050167

hole = cq.Workplane("XZ").cylinder(width,diameter/2).translate((length/2-diameter/2-0.446488,0,height/2-diameter/2-top_padding))
box = cq.Workplane("XY").box(length, width, height)

part:cq.Workplane = (
    box
    .cut(hole)
    .cut(hole.translate((-diameter-0.050167,0,0)))
    .cut(hole.translate((-diameter*2-0.050167*2,0,0)))
)

part = part.translate((0,width/2,-height/2)).rotate((0,0,1),(0,0,0),180)

cq.exporters.export(part, 'Ground_Truth.stl')