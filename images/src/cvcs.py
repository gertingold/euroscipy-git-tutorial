from pyx import canvas, color, deco, path, style, text, trafo, unit

servercolor = color.rgb(0.5, 0.5, 0.8)
arrowcolor = color.grey(0.5)
clientcolor = color.rgb(0.8, 0.5, 0.5)

text.set(text.LatexRunner)                                                                           
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
unit.set(xscale=1.3)

c = canvas.canvas()
r = 1
c.fill(path.circle(0, 0, r), [servercolor, trafo.scale(1, 0.5)])
h = 2
p = path.path(path.moveto(-r, 0),
              path.lineto(-r, -h),
              path.arc(0, -h, r, 180, 0),
              path.lineto(r, 0),
              path.arcn(0, 0, r, 0, 180),
              path.closepath())
c.fill(p, [servercolor, trafo.scale(1, 0.5).translated(0, -0.08)])
c.text(0, 0.5*r+0.3, 'central server', [text.halign.center])

h = 1.7
l = 2
for phi in (-30, 0, 30):
    c.stroke(path.line(0, -h, 0, -h-l), [arrowcolor, style.linewidth.THICK,
                                         deco.barrow.LArge, deco.earrow.LArge,
                                         trafo.rotate(phi)])
for dx, dy in ((-2, -3.7), (0, -4.2), (2, -3.7)):
    r = 0.3
    c.fill(path.circle(0, 0, r), [clientcolor, trafo.translate(dx, dy)])
    r = 0.5
    p = path.path(path.moveto(-r, 0),
                  path.curveto(-r, r, r, r, r, 0),
                  path.closepath())
    c.fill(p, [clientcolor, trafo.translate(dx, dy-1.3*r)])
c.text(0, -5.5, 'clients', [text.halign.center])
c.writePDFfile()
