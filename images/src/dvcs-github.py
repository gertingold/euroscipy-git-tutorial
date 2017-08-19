from math import sin, cos, pi
from pyx import canvas, color, deco, deformer, path, style, text, trafo, unit

def server(r, servercolor=color.rgb(0.5, 0.5, 0.8), transparency=0):
    c = canvas.canvas()
    c.fill(path.circle(0, 0, r), [servercolor, color.transparency(transparency),
                                  trafo.scale(1, 0.5).translated(0, 0.5*r)])
    h = 2*r
    p = path.path(path.moveto(-r, 0),
                  path.lineto(-r, -h),
                  path.arc(0, -h, r, 180, 0),
                  path.lineto(r, 0),
                  path.arcn(0, 0, r, 0, 180),
                  path.closepath())
    c.fill(p, [servercolor, color.transparency(transparency),
               trafo.scale(1, 0.5).translated(0, 0.5*r-0.08*r)])
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
pos = [(0, 1), (sin(2*pi/3), cos(2*pi/3)), (-sin(2*pi/3), cos(2*pi/3))]
sfak = 1.5
for x, y in pos:
    c.insert(server(0.3), [trafo.translate(sfak*x, sfak*y)])
    c.insert(client(), [trafo.scale(0.5).translated(3*x, 3*y+0.15)])
    c.stroke(path.line(2.7*x, 2.7*y, 1.9*x, 1.9*y),
               [arrowcolor, deco.earrow.large, deco.barrow.large, style.linewidth.THick])
for phi in (0, 120, 240):
    c.stroke(path.curve(-sfak*sin(2*pi/3)+0.4, -0.5*sfak+0.15,
                        -sfak*sin(2*pi/3)+0.8, -0.5*sfak+0.35,
                        sfak*sin(2*pi/3)-0.8, -0.5*sfak+0.35,
                        sfak*sin(2*pi/3)-0.4, -0.5*sfak+0.15),
                 [arrowcolor, deco.earrow.large, deco.barrow.large, style.linewidth.THick,
                  trafo.rotate(phi)])
c.insert(server(0.5, color.hsb(0.5, 0.8, 0.5), 0.13))
c.text(0.8, 0.2, 'Gitlab / Github server', [color.hsb(0.5, 0.8, 0.5), text.size.small])

c.writePDFfile()
