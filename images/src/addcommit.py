from pyx import canvas, color, deco, deformer, path, style, text, trafo

def filesymbol(size, symbolcolor):
    wd = size
    ht = size*1.414
    knick = 0.25*wd
    p = path.path(path.moveto(0.5*wd-knick, 0.5*ht),
                  path.lineto(0.5*wd, 0.5*ht-knick),
                  path.lineto(0.5*wd, -0.5*ht),
                  path.lineto(-0.5*wd, -0.5*ht),
                  path.lineto(-0.5*wd, 0.5*ht),
                  path.lineto(0.5*wd-knick, 0.5*ht),
                  path.lineto(0.5*wd-knick, 0.5*ht-knick),
                  path.lineto(0.5*wd, 0.5*ht-knick)
                  )
    cf = canvas.canvas()
    cf.stroke(p, [symbolcolor, style.linewidth.Thick, style.linejoin.round])
    return cf

text.set(text.LatexRunner)
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')

c = canvas.canvas()
ht = 5
htlabel = 1
wd = 3.5
vdist = 0.05
hdist = 1
size = 1.2

for nr, (label, boxcolor, symbolcolor, status) in enumerate(
          (('working directory', color.hsb(0.87, 1, 0.6), color.rgb(0.6, 0, 0), 'modified'),
           ('staging area', color.hsb(0.2, 1, 0.6), color.rgb(0, 0.5, 0), 'staged'),
           ('repository (.git)', color.hsb(0.53, 1, 0.6), color.grey(0.3), 'committed'))
                                                   ):
    xmid = nr*(wd+hdist)+0.5*wd
    c.stroke(path.rect(nr*(wd+hdist), 0, wd, ht),
             [deformer.smoothed(0.3), boxcolor, style.linewidth.Thick])
    c.fill(path.rect(nr*(wd+hdist), ht+vdist, wd, htlabel),
           [deformer.smoothed(0.3), boxcolor])
    c.text(xmid, ht+vdist+0.5*htlabel, label,
           [text.halign.center, text.valign.middle, color.grey(1)])
    c.insert(filesymbol(size, symbolcolor),
             [trafo.translate(xmid, 0.5*ht)])
    c.text(xmid, 0.2*ht, status, [text.halign.center, symbolcolor])
for nr, operation in enumerate(('git add', 'git commit')):
    xmid = nr*(wd+hdist)+0.5*wd
    c.stroke(path.line(xmid+0.5*size+0.1, 0.5*ht,
                       xmid+wd+hdist-0.5*size-0.1, 0.5*ht),
             [deco.earrow.large, style.linewidth.Thick])
    cop = canvas.canvas()
    optext = text.text(0, 0, operation, [text.halign.center, text.valign.middle])
    tblarge = optext.bbox().enlarged(0.1)
    cop.fill(tblarge.path(),
             [deco.stroked([color.grey(0)]), color.grey(0.9)])
    cop.insert(optext)
    c.insert(cop, [trafo.translate((nr+1)*(wd+hdist)-0.5*hdist, 0.5*ht)])

c.writePDFfile()
