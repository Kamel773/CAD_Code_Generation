import cadquery as cq
length = 0.780417
width = 0.440093
height = 0.143395


box = cq.Workplane("XY").box(length, width, height)

c_length = 0.721321
c_width = 0.382387
c_height = 0.131228
distance = 0.017381

cut_box = (
    cq.Workplane("XY")
    .box(c_length, c_width, c_height)
    .edges("|Z")
    .fillet(distance)
)

part = box.cut(cut_box.translate((0.000869,0,height/2-c_height/2)))

part = part.translate((length/2-0.030417,width/2-0.030417+0.001564,height/2))


cq.exporters.export(part, 'Ground_Truth.stl')