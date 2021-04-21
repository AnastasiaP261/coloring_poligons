import cairo
from triangle import triangles

width = 230
height = 110

colors = (
    (0.255, 0.182, 0.193),              # pink
    (0.255, 0.255, 0.180),              # yellow
    (0.135, 0.206, 0.250),              # blue
    (0.144, 0.238, 0.144)               # green
)


def draw_graph():
    center = (width / 2, height / 2)
    with cairo.SVGSurface("image.svg", width, height) as surface:
        cr = cairo.Context(surface)

        for triag in triangles:
            cr.move_to(center[0] + triag.p1.x, center[1] - triag.p1.y)
            cr.line_to(center[0] + triag.p2.x, center[1] - triag.p2.y)
            cr.line_to(center[0] + triag.p3.x, center[1] - triag.p3.y)
            cr.close_path()

            cr.set_source_rgb(round(colors[triag.allow_colors][0] * 4.44444, 3),
                              round(colors[triag.allow_colors][1] * 4.44444, 3),
                              round(colors[triag.allow_colors][2] * 4.44444, 3))
            cr.fill_preserve()

            cr.set_source_rgb(0, 0, 0)
            cr.set_line_width(0.3)
            cr.stroke()
