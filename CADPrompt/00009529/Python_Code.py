import cadquery as cq

r_one_length:float = 1.5
r_one_width:float = 0.55102
r_one_height:float = 0.08347
rectangle_one:cq.Workplane = cq.Workplane("XY").box(r_one_length, r_one_width, r_one_height)

r_two_length:float = 0.438776
r_two_width:float = 0.413265
r_two_height:float = 0.280162
rectangle_two = cq.Workplane("XY").box(r_two_length, r_two_width, r_two_height)

r_three_length:float = .331633
r_three_width:float = 0.382653
r_three_height:float = 0.127551
rectangle_three = cq.Workplane("XY").box(r_three_length, r_three_width, r_three_height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle_one)
    .union(rectangle_two.translate((r_one_length/2  -r_two_length/2, 0, r_one_height/2 + r_two_height/2)))
    .union(rectangle_three.translate((-r_one_length/2 + r_three_length/2, 0, r_one_height/2 + r_three_height/2)))
)

part = part.translate((0, 0, r_one_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')