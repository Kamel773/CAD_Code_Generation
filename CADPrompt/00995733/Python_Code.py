import cadquery as cq

extrude:float = 0.018672

result:cq.Workplane = (
    cq.Workplane("XY")
    .lineTo(0.024896, 0)#base
    .spline([
        (0.024896, 0.000001),
        (0.024896 - 0.041612-0.055993, 0.752339-0.002339)
    ], includeCurrent=True)
    .lineTo(0.024896 - 0.041612 - 0.055993 - 0.060246, 0.752339-0.002339)
    .lineTo(0.024896 - 0.041612 - 0.055993 - 0.060246,0.752339-0.002339 -0.018672)
    .lineTo(0.024896 - 0.041612 - 0.055993 - 0.060246 + 0.040456 , 0.752339-0.002339-0.018672)
    .spline([
        (0.024896 - 0.041612 -0.055993 - 0.060246+0.040456 , 0.752339-0.002339-0.018672-0.00001),
        #(0.018634- 0.055-.01, 0.375),
        #(0.018634- 0.055, 0.275),
        (0,0.00001)
    ], includeCurrent=True)
    .close()
    .extrude(extrude)
)

cut_block:cq.Workplane = (
    cq.Workplane("XY")
    .union(result.translate((-0.0248961,0,0)))
    .cut(cq.Workplane("XY").box(.1,.1,.1).translate((-.1/2+0.024896 - 0.041612 - 0.055993 - 0.060246 + 0.040456,.1/2+0.752339-0.002339-0.018672,0)))
)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(result)
    .cut(cut_block)
)

part = part.rotate((1,0,0),(0,0,0),-90).rotate((0,0,1),(0,0,0),180).translate((-0.146345,-extrude,0))

cq.exporters.export(part, 'Ground_Truth.stl')