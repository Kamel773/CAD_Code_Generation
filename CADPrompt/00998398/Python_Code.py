import cadquery as cq

extrude = 0.75
mid_length = 0.234841
bottom_length = 0.11742
mid_height = 0.280088
top_height = 0.204477
bottom_height = 0.279461

mid_shift = 0.004644
bottom_shift = 0.002349

pts = [
       
    (0,top_height),
    (-mid_length/2+mid_shift,0),
    (-bottom_length/2+bottom_shift,-bottom_height),
    (bottom_length/2+bottom_shift,-bottom_height),
    (mid_length/2+mid_shift,0),
]

part = (
    cq.Workplane("XZ")
    .polyline(pts)
    .close()
    .extrude(0.75)
)

cq.exporters.export(part, 'Ground_Truth.stl')