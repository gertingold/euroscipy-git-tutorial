from math import sin, cos, pi
import random
from pyx import canvas, color, deco, deformer, path, style, text, trafo, unit

def gethashstring():
    hash = hex(random.getrandbits(28))[2:]
    return r'\ttfamily\bfseries {}'.format(hash)

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

random.seed(812357)

arrowcolor = color.grey(0.5)

text.set(text.LatexRunner)                                                                           
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
unit.set(xscale=1.3)

c = canvas.canvas()
pos = [(0, 1), (sin(2*pi/3), cos(2*pi/3)), (-sin(2*pi/3), cos(2*pi/3))]
for x, y in pos:
    c.insert(server(0.3), [trafo.translate(1.5*x, 1.5*y)])
    c.insert(client(), [trafo.scale(0.5).translated(3*x, 3*y+0.15)])
    c.stroke(path.line(2.7*x, 2.7*y, 1.9*x, 1.9*y),
               [arrowcolor, deco.earrow.large, deco.barrow.large, style.linewidth.THick])
pos.append(pos[0])
fak = 0.3
for (x1, y1), (x2,y2) in zip(pos[:-1], pos[1:]):
    c.stroke(path.line(1.5*x1+fak*(x2-x1), 1.5*y1+fak*(y2-y1),
                       1.5*x2-fak*(x2-x1), 1.5*y2-fak*(y2-y1)), 
               [arrowcolor, deco.earrow.Large, deco.barrow.Large, style.linewidth.THIck])

dy = 0.8
dx = 1.5
versionoff = 1.5
cf = canvas.canvas()
hueoff = 0.17
nr_revisions = 0
for nr, (name, versions) in enumerate((('file 1', (0, 2, 4, 5)),
                                       ('file 2', (0, 1, 2, 3, 5)),
                                       ('file 3', (1, 4, 5)))):
    nr_revisions = max(nr_revisions, max(versions))
    hue = hueoff+nr/3
    cf.text(0, -nr*dy, name, [color.hsb(hue, 1, 0.5), text.valign.middle])
    for nver, (v1, v2) in enumerate(zip(versions[:-1], versions[1:])):
        y = -(nr+0.4)*dy
        lv = len(versions)-1
        xll = v1*dx+versionoff+0.1
        yll = y
        width = (v2-v1)*dx-0.2
        height = 0.8*dy
        cf.fill(path.rect(xll, yll, width, height),
                [color.hsb(hue, 1-(lv-1-nver)/(lv-1)*0.7, 0.6)])
        cf.text(xll+0.5*width, yll+0.5*height, gethashstring(),
                [text.size(-4), text.halign.center, text.valign.middle, color.grey(1)])
for n in range(nr_revisions):
    xcenter = (n+0.5)*dx+versionoff
    y = 0.5
    cf.text(xcenter, y, gethashstring(), [text.size(-4), text.halign.center])
    if n:
        yshift = 0.1
        cf.stroke(path.line(xcenter-0.33*dx, y+yshift, xcenter-0.67*dx, y+yshift),
                  [deco.earrow])
cf.stroke(path.rect(3*dx+versionoff, -2.6*dy, dx, 2.6*dy+1.0),
              [style.linewidth.THIck, deformer.smoothed(0.3)])
    
c.insert(cf, [trafo.translate(4.5, 1)])

c.writePDFfile()




