import cadquery as cq

length:float = 0.848067
width:float = 0.197368

diameter_one:float = 0.157782
ring_one:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter_one/2)

cut_one_diameter:float = 0.094737
cut_one:cq.Workplane = cq.Workplane("XZ").cylinder(width, cut_one_diameter/2)

diameter_two:float = 0.196626
ring_two:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter_two/2)

cut_two_diameter:float = 0.094737
cut_two:cq.Workplane = cq.Workplane("XZ").cylinder(width, cut_two_diameter/2)

c_length:float = length - diameter_two/2 - diameter_one/2
c_height:float = 0.126316
connector:cq.Workplane = cq.Workplane("XY").box(c_length,width,c_height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(connector)
    .union(ring_one.translate((+length/2-diameter_one/2,0,0)))
    .cut(cut_one.translate((+length/2-diameter_one/2,0,0)))
    .union(ring_two.translate((-length/2+diameter_two/2,0,0)))
    .cut(cut_two.translate((-length/2+diameter_two/2,0,0)))
)

part = part.translate((length/2-diameter_two/2,-width/2,0))


cq.exporters.export(part, 'Ground_Truth.stl')