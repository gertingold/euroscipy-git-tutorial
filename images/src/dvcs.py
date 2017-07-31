from math import sin, cos, pi
from pyx import canvas, color, deco, deformer, path, style, text, trafo, unit

def server(r, servercolor=color.rgb(0.5, 0.5, 0.8)):
    c = canvas.canvas()
    c.fill(path.circle(0, 0, r), [servercolor, trafo.scale(1, 0.5).translated(0, 0.5*r)])
    h = 2*r
    p = path.path(path.moveto(-r, 0),
                  path.lineto(-r, -h),
                  path.arc(0, -h, r, 180, 0),
                  path.lineto(r, 0),
                  path.arcn(0, 0, r, 0, 180),
                  path.closepath())
    c.fill(p, [servercolor, trafo.scale(1, 0.5).translated(0, 0.5*r-0.08*r)])
    return c

def client(clientcolor=color.rgb(0.8, 0.5, 0.5)):
    c = canvas.canvas()
    r = 0.3
    c.fill(path.circle(0, 0, r), [clientcolor])
    r = 0.5
    p = path.path(path.moveto(-r, 0),
                  path.curveto(-r, r, r, r, r, 0),
                  path.closepath())
    c.fill(p, [clientcolor, trafo.translate(0, -1.3*r)])
    return c

arrowcolor = color.grey(0.5)

text.set(text.LatexRunner)                                                                           
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
unit.set(xscale=1.3)

c = canvas.canvas()
for x, y in ((0, 1), (sin(2*pi/3), cos(2*pi/3)), (-sin(2*pi/3), cos(2*pi/3))):
    c.insert(server(0.5), [trafo.translate(x, y)])
    c.insert(client(), [trafo.scale(0.5).translated(2*x, 2*y)])


c.writePDFfile()
