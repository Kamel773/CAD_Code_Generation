import cadquery as cq
top_length:float = 0.059055
top_width:float = 0.11811
top_height:float = 0.088583
top_box:cq.Workplane = cq.Workplane("XY").box(top_length, top_width, top_height)

mid_length:float = 1.25274
mid_width:float = 0.982742
mid_height:float = 0.041339
mid_box:cq.Workplane = cq.Workplane("XY").box(mid_length, mid_width, mid_height)

base_length:float = 1.5
base_width:float = 1.2
base_height:float = 0.147638
base_box:cq.Workplane = cq.Workplane("XY").box(base_length, base_width, base_height)

cut_length:float = 0.975
cut_width:float = 0.675
cut_height:float = 0.11811
cut_box:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, cut_height)

width_padding:float = 0.314204
length_padding:float = 0.390573

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(base_box)
    .cut(cut_box.translate((0,0,-base_height/2 + cut_height/2)))
    .union(mid_box.translate((0,0,base_height/2 + mid_height/2)))
    .union(top_box.translate((mid_length/2 - top_length/2 - length_padding, mid_width/2 - top_width/2 - width_padding, base_height/2 + mid_height+top_height/2)))
    .union(top_box.translate((-mid_length/2 + top_length/2 + length_padding, mid_width/2 - top_width/2 - width_padding, base_height/2 + mid_height+top_height/2)))
)

part = part.translate((0,0,base_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')