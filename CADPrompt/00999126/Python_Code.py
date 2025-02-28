import cadquery as cq
length = 1.48234
width = 0.413495
height = 0.039009

base = cq.Workplane("XY").box(length, width, height)

r_length = 0.147465
r_width = 0.183609
r_margin = 0.115044
right_cut= cq.Workplane("XY").box(r_length, r_width, height)

l_length = 0.320737
l_width = 0.187173
l_margin = 0.101171
left_cut = cq.Workplane("XY").box(l_length, l_width, height)

part = (
    base
    .cut(right_cut.translate((-length/2+r_length/2,-width/2+r_width/2+r_margin,0)))
    .cut(left_cut.translate((length/2-l_length/2,-width/2+l_width/2+l_margin,0)))
)

part = part.translate((0.008832,0,height/2))


cq.exporters.export(part, 'Ground_Truth.stl')