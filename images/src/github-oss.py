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

text.set(text.LatexRunner)
c = canvas.canvas()

wd = 6
ht = 3.5
githubcolor = color.rgb(0, 0, 0.7)
c.stroke(path.rect(0, 0, wd, ht), [deformer.smoothed(0.1),
                                   githubcolor,
                                  style.linewidth.Thick])

clabel = canvas.canvas()
labeltext = text.text(0, 0, r'\textsf{Github}', [color.grey(1)])
extrawd = 0.15
labelbox = labeltext.bbox().enlarged(extrawd)
clabel.fill(labelbox.path(), [githubcolor, deformer.smoothed(0.1)])
clabel.insert(labeltext)
c.insert(clabel, [trafo.translate(extrawd, ht+extrawd)])

c.insert(repo('upstream', color.hsb(0.55, 1, 0.6), color.hsb(0.55, 0.1, 1)),
         [trafo.translate(0.5, 2.8)])
c.insert(repo('origin', color.hsb(0.15, 1, 0.6), color.hsb(0.15, 0.1, 1)),
         [trafo.translate(4.6, 0.8)])
c.insert(repo('local Git repo', color.hsb(0.05, 1, 0.6), color.hsb(0.05, 0.1, 1)),
         [trafo.translate(2.9, -1.6)])

opcolor = color.hsb(0.3, 1, 0.4)
c.stroke(path.line(2.1, 2.5, 4.4, 1.2),
         [deco.earrow, style.linestyle.dashed, opcolor])
c.text(2.4, 1.7, r'\textsf{fork}', [opcolor])
c.text(2.4, 1.4, r'\scriptsize\textsf{(only once)}', [opcolor])

p = path.path(path.moveto(5, 1.3),
              path.curveto(5, 1.7, 4.6, 2.9, 2.1, 2.9))
c.stroke(p, [deco.earrow, opcolor])
c.text(3.8, 2.9, r'\textsf{pull request}', [opcolor])

p = path.path(path.moveto(0.7, 2.5),
              path.curveto(0.7, 1.5, 1.0, -1.5, 2.65, -1.5))
c.stroke(p, [deco.earrow, opcolor])
c.text(0.2, -1.2, r'\textsf{pull \scriptsize or}', [opcolor])
c.text(0.2, -1.7, r'\textsf{fetch/merge}', [opcolor])

p = path.path(path.moveto(4.0, -1.1),
              path.curveto(4.0, 0, 5, -0.9, 5, 0.5))
c.stroke(p, [deco.earrow, opcolor])
c.text(4.3, -0.8, r'\textsf{push}', [opcolor])

c.writePDFfile()
