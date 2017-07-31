from pyx import canvas, color, deco, deformer, path, style, text, trafo, unit

def server(r, servercolor=color.rgb(0.5, 0.5, 0.8)):
    c = canvas.canvas()
    c.fill(path.circle(0, 0, r), [servercolor, trafo.scale(1, 0.5)])
    h = 2*r
    p = path.path(path.moveto(-r, 0),
                  path.lineto(-r, -h),
                  path.arc(0, -h, r, 180, 0),
                  path.lineto(r, 0),
                  path.arcn(0, 0, r, 0, 180),
                  path.closepath())
    c.fill(p, [servercolor, trafo.scale(1, 0.5).translated(0, -0.08*r)])
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
r = 1
c.insert(server(r))
c.text(0, 0.5*r+0.3, 'central server', [text.halign.center])

h = 1.7
l = 2
for phi in (-30, 0, 30):
    c.stroke(path.line(0, -h, 0, -h-l), [arrowcolor, style.linewidth.THICK,
                                         deco.barrow.LArge, deco.earrow.LArge,
                                         trafo.rotate(phi)])
for dx, dy in ((-2, -3.7), (0, -4.2), (2, -3.7)):
    c.insert(client(), [trafo.translate(dx, dy)])
c.text(0, -5.5, 'clients', [text.halign.center])

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
        cf.fill(path.rect(v1*dx+versionoff+0.1, y, (v2-v1)*dx-0.2, 0.8*dy),
                [color.hsb(hue, 1-(lv-1-nver)/(lv-1)*0.7, 0.6)])
for n in range(nr_revisions):
    cf.text((n+0.5)*dx+versionoff, 0.5, 'r{}'.format(n+1), [text.halign.center])
cf.stroke(path.rect(3*dx+versionoff, -2.6*dy, dx, 2.6*dy+1.0),
              [style.linewidth.THIck, deformer.smoothed(0.3)])
    
c.insert(cf, [trafo.translate(4.5, -2)])
c.writePDFfile()
