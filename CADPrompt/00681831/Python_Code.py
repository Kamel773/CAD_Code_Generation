import cadquery as cq
width:float = 0.295686
diameter:float = 0.955953
b_length:float = 0.163062
b_width:float = width
offset:float = 0.698688
b_height:float = diameter - offset


box:cq.Workplane = cq.Workplane("XY").box(b_length,b_width,b_height)

cylinder:cq.Workplane = cq.Workplane("XZ").cylinder(width,diameter/2)

cut_part:cq.Workplane = (
    cq.Workplane("XY")
    .add(box.translate((0,0,diameter/2-b_height/2)))
    .add(box.translate((b_length/2,0,b_height/2)).rotate((0,1,0),(0,0,0),28).translate((-b_length/2,0,diameter/2-b_height)))
    .add(box.translate((-b_length/2,0,b_height/2)).rotate((0,1,0),(0,0,0),-26).translate((b_length/2,0,diameter/2-b_height)))
 )

part:cq.Workplane = (
    cq.Workplane("XY")
    .add(cylinder)
    .cut(cut_part.translate((0.005716,0,0)))
)

part = part.translate((0,width/2,-0.272116))


cq.exporters.export(part, 'Ground_Truth.stl')