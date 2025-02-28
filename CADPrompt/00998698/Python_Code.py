import cadquery as cq

diameter = 0.5
width = 0.433013
spacer = 0.155128
sides = 6
height = 0.75

hexes = (
    cq.Sketch()
    .push([(0,0),(width+spacer,-0.018963)])
    .regularPolygon(diameter/2,sides)
)

hex_base = (
    cq.Sketch()
    .push([(0,0),(width+spacer,-0.018963)])
    .regularPolygon(diameter/2,sides)
    .wires()
    .hull()
)

hexagans = (
    cq.Workplane("XY")
    .placeSketch(hexes)
    .extrude(height)
)

base = (
    cq.Workplane("XY")
    .placeSketch(hex_base)
    .extrude(0.125)
)

part = (
    cq.Workplane("XY")
    .union(hexagans)
    .union(base)
)


part = part.rotate((0,0,1),(0,0,0),30+180).translate((00.339552,-0.348832,0))

cq.exporters.export(part, 'Ground_Truth.stl')