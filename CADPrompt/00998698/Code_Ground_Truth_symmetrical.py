import cadquery as cq

diameter = 0.5
width = 0.433013
spacer = 0.155128
sides = 6
height = 0.75

hex = (
    cq.Workplane("XY")
    .polygon(sides, diameter)
    .extrude(height)
)

connector = (
    cq.Workplane("XY")
    .box(diameter,width+spacer,0.125)
    .translate((0,(width+spacer)/2,0.125/2))
)

part = (
    hex
    .union(hex.translate((0,width+spacer,0)))
    .union(connector)
)

part = part.rotate((0,0,1),(0,0,0),-60).translate((00.339552,-0.348832,0))

cq.exporters.export(part, 'Code_Ground_Truth.stl')