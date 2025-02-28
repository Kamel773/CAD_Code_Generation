import cadquery as cq

cylinder_diameter:float = 1.31858
cylinder_height:float = 0.468766
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height, cylinder_diameter/2)

board_length:float = 1.5
board_width:float = 0.1875
board_height:float = 0.075
board:cq.Workplane = cq.Workplane("XY").box(board_length, board_width, board_height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(cylinder.translate((0, 0, -cylinder_height/2)))
    .union(board.translate((0, 0, board_height/2)))
)

cq.exporters.export(part, 'Ground_Truth.stl')