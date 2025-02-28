import cadquery as cq

b_length:float = 1.05974
b_width:float = 0.362338
b_height:float = 0.341991
box:cq.Workplane = cq.Workplane("XY").box(b_length, b_width, b_height)

i_length:float = 0.954546
i_width:float = 0.261039
i_height:float = 0.314632
box_interior:cq.Workplane = cq.Workplane("XY").box(i_length, i_width, i_height)

r_length:float = 0.041039
r_width:float = 0.136796
r_height:float = 0.314632
right_box:cq.Workplane = cq.Workplane("XY").box(r_length,r_width,r_height)

l_length:float = 0.041039
l_width:float = 0.136796
l_height:float = 0.314632
left_box:cq.Workplane = cq.Workplane("XY").box(l_length,l_width,l_height)

h_length:float = 1.0
diameter:float = 0.108522
handle:cq.Workplane = cq.Workplane("YZ").cylinder(h_length,diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(box)
    .cut(box_interior.translate((
        -b_length/2+i_length/2+0.050649,
        -b_width/2+i_width/2+0.046797,
        -b_height/2+i_height/2
    )))
    .union(right_box.translate((
        -b_length/2+r_length/2-0.000435,
        0,
        -b_height/2-r_height/2+0.04136
    )))
    .union(left_box.translate((
        i_length/2+l_length/2-0.006869,
        0,
        -b_height/2-l_height/2
    )))
    .union(handle.translate((
        -0.006869,
        0,
        -b_height/2-l_height/2-diameter/2+0.015775
    )))
)

part = part.translate((0.22013,0.072078,b_height/2))

cq.exporters.export(part, 'Ground_Truth.stl')