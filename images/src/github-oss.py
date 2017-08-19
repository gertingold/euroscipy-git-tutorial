import os, sys
from pyx import canvas, color, deco, deformer, path, style, text, trafo

def repo(label, colorfg, colorbg):
    crepo = canvas.canvas()
    labeltext = text.text(0, 0, r'\textsf{{{}}}'.format(label),
                          [colorfg])
    extrawd = 0.15
    labelbox = labeltext.bbox().enlarged(extrawd)
    crepo.fill(labelbox.path(), [colorbg, deformer.smoothed(0.05),
                                  deco.stroked([colorfg])])
    crepo.insert(labeltext)
    return crepo

def read(size, color):
    size = size*0.25
    cread = canvas.canvas()
    cread.fill(path.circle(0, 0, 0.35), [color, trafo.scale(size)])
    p = path.path(path.moveto(0.8, 0),
                  path.curveto(0.2, 0.5, -0.2, 0.5, -0.8, 0),
                  path.curveto(-0.2, -0.5, 0.2, -0.5, 0.8, 0),
                  path.closepath())
    cread.stroke(p, [color, style.linewidth.thick, trafo.scale(size)])
    return cread

def write(size, color):
    size = size*0.3
    cwrite = canvas.canvas()
    p = path.path(path.moveto(-0.2, 0.8),
                  path.lineto(0.2, 0.8),
                  path.lineto(0.2, 0),
                  path.lineto(0, -0.2),
                  path.lineto(-0.2, 0),
                  path.lineto(-0.2, 0.8),
                  path.closepath(),
                  path.moveto(0, 0.8),
                  path.lineto(0, 0.05),
                  path.moveto(-0.2, 0),
                  path.arcn(-0.1, 0, 0.1, 180, 20),
                  path.arcn(0.1, 0, 0.1, 160, 0))
    cwrite.stroke(p, [color, trafo.scale(size).rotated(-30).translated(0,-0.4*size)])
    return cwrite

basename = os.path.splitext(sys.argv[0])[0]

text.set(text.LatexRunner)
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
c = canvas.canvas()

wd = 6.9
ht = 3.5
githubfgcolor = color.grey(0.4)
githubbgcolor = color.grey(0.97)
maintainercolor = color.hsb(0.7, 1, 0.5)
usercolor = color.hsb(0.05, 1, 0.5)
c.stroke(path.rect(0, 0, wd, ht), [deformer.smoothed(0.1),
                                   githubfgcolor,
                                   style.linewidth.Thick,
                                   deco.filled([githubbgcolor])])

clabel = canvas.canvas()
labeltext = text.text(0, 0, r'\textsf{\bfseries Github}', [color.grey(1)])
extrawd = 0.15
labelbox = labeltext.bbox().enlarged(extrawd)
clabel.fill(labelbox.path(), [githubfgcolor, deformer.smoothed(0.1)])
clabel.insert(labeltext)
c.insert(clabel, [trafo.translate(extrawd, ht+extrawd)])

c.text(wd+0.4, ht-0.5, r'\footnotesize\textsf{read/write permissions}')
c.insert(read(1, usercolor), [trafo.translate(wd+0.7, ht-0.9)])
c.insert(write(1, usercolor), [trafo.translate(wd+1.05, ht-0.9)])
c.text(wd+1.5, ht-1.0, r'\footnotesize\textsf{user}', [usercolor])
c.insert(write(1, maintainercolor), [trafo.translate(wd+1.05, ht-1.3)])
c.insert(read(1, maintainercolor), [trafo.translate(wd+0.7, ht-1.3)])
c.text(wd+1.5, ht-1.4, r'\footnotesize\textsf{maintainer}', [maintainercolor])

c.insert(repo('upstream', color.hsb(0.55, 1, 0.6), color.hsb(0.55, 0.1, 1)),
         [trafo.translate(0.5, 2.8)])
c.insert(read(1, maintainercolor), [trafo.translate(0.85, 2.3)])
c.insert(write(1, maintainercolor), [trafo.translate(1.2, 2.3)])
c.insert(read(1, usercolor), [trafo.translate(1.65, 2.3)])

c.insert(repo('local Git repo', color.hsb(0.04, 1, 0.6), color.hsb(0.04, 0.1, 1)),
         [trafo.translate(2.9, -1.6)])
c.insert(read(1, usercolor), [trafo.translate(5.75, -1.6)])
c.insert(write(1, usercolor), [trafo.translate(6.1, -1.6)])

c.writePDFfile('{}_1.pdf'.format(basename))

c.insert(repo('origin', color.hsb(0.13, 1, 0.6), color.hsb(0.13, 0.1, 1)),
         [trafo.translate(4.6, 0.8)])

c.insert(read(1, maintainercolor), [trafo.translate(6.1, 1.05)])
c.insert(read(1, usercolor), [trafo.translate(6.1, 0.75)])
c.insert(write(1, usercolor), [trafo.translate(6.45, 0.75)])

opcolor = color.hsb(0.3, 1, 0.4)
c.stroke(path.line(2.1, 2.5, 4.4, 1.2),
         [deco.earrow, style.linestyle.dashed, opcolor])
c.text(2.3, 1.6, r'\textsf{fork}', [opcolor])

c.writePDFfile('{}_2.pdf'.format(basename))

c.text(2.3, 1.3, r'\scriptsize\textsf{(only once)}', [opcolor])

p = path.path(path.moveto(5, 1.3),
              path.curveto(5, 1.7, 4.6, 2.9, 2.4, 2.9))
c.stroke(p, [deco.earrow, opcolor])
c.text(4.1, 2.7, r'\textsf{pull request}', [opcolor])

p = path.path(path.moveto(0.5, 2.5),
              path.curveto(0.5, 0, 1.0, -1.5, 2.65, -1.5))
c.stroke(p, [deco.earrow, opcolor])
c.text(0.1, -1.3, r'\textsf{pull \scriptsize or}', [opcolor])
c.text(0.1, -1.75, r'\textsf{fetch/merge}', [opcolor])

p = path.path(path.moveto(4.0, -1.1),
              path.curveto(4.8, -0.5, 5, 0., 5, 0.5))
c.stroke(p, [deco.earrow, opcolor])
c.text(4.7, -0.8, r'\textsf{push}', [opcolor])

p = path.path(path.moveto(4.8, 0.5),
              path.curveto(4.0, 0, 3.8, -0.5, 3.8, -1.1))
c.stroke(p, [deco.earrow, opcolor])
c.text(3.2, -0.5, r'\textsf{pull}', [opcolor])


c.writePDFfile('{}_3.pdf'.format(basename))
