# Établi icon glyph definitions (raw 1024 coordinates, pre-alignment).
# Each element: dict(t=path|line|rect|circle, ..., fill=False, color='fg'|'knock', rot=(deg,cx,cy) optional)
SUITE_FRAME_E = ("M 382 792 H 308 A 36 36 0 0 1 272 756 V 400 A 36 36 0 0 1 308 364 H 716 A 36 36 0 0 1 752 400 "
                 "V 756 A 36 36 0 0 1 716 792 H 667 A 36 36 0 0 1 631 756 V 716 A 36 36 0 0 0 595 680 "
                 "H 450 A 36 36 0 0 1 414 644 V 484 A 36 36 0 0 1 450 448 H 610")
def P(d, **k): return dict(t='path', d=' '.join(d.split()), **k)
def L(x1,y1,x2,y2, **k): return dict(t='line', x1=x1,y1=y1,x2=x2,y2=y2, **k)
def R(x,y,w,h,rx=0, **k): return dict(t='rect', x=x,y=y,w=w,h=h,rx=rx, **k)
def C(cx,cy,r, **k): return dict(t='circle', cx=cx,cy=cy,r=r, **k)

GLYPHS = {
 'suite': dict(label='Établi', els=[P(SUITE_FRAME_E), L(414,564,590,564), L(488,364,556,273)]),
 # { > } : left brace flows along the bottom (the prompt's underscore) into the right brace
 'atelier': dict(label='Atelier', els=[
    P("M 380 320 C 320 320, 310 360, 310 410 L 310 470 C 310 510, 290 530, 260 530 C 290 530, 310 550, 310 590 L 310 650 C 310 700, 320 740, 380 740 "
      "H 644 C 704 740, 714 700, 714 650 L 714 590 C 714 550, 734 530, 764 530 C 734 530, 714 510, 714 470 L 714 410 C 714 360, 704 320, 644 320"),
    P("M 456 466 L 552 530 L 456 594")]),
 # window: frame and title bar in one line (like Table), traffic-light dots, play triangle
 'vitrine': dict(label='Vitrine', els=[
    P("M 260 350 H 764 V 296 A 36 36 0 0 0 728 260 H 296 A 36 36 0 0 0 260 296 V 728 A 36 36 0 0 0 296 764 H 728 A 36 36 0 0 0 764 728 V 350"),
    C(312,305,15,fill=True), C(362,305,15,fill=True), C(412,305,15,fill=True),
    P("M 452 456 L 452 660 L 620 558 Z")]),
 # envelope: flap and outline in one line
 'courrier': dict(label='Courrier', els=[
    P("M 220 372 L 512 560 L 804 372 V 668 A 36 36 0 0 1 768 704 H 256 A 36 36 0 0 1 220 668 V 356 A 36 36 0 0 1 256 320 H 768 A 36 36 0 0 1 804 356 V 372")]),
 # gathered sheets: back sheet (open end) flows into the front sheet
 'recueil': dict(label='Recueil', els=[
    P("M 260 500 V 276 A 36 36 0 0 1 296 240 H 624 A 36 36 0 0 1 660 276 V 350 H 744 A 36 36 0 0 1 780 386 V 654 A 36 36 0 0 1 744 690 "
      "H 396 A 36 36 0 0 1 360 654 V 386 A 36 36 0 0 1 396 350 H 660"),
    L(430,470,700,470), L(430,570,610,570)]),
 # page with folded corner in one line
 'doc': dict(label='Doc', els=[
    P("M 644 260 H 336 A 36 36 0 0 0 300 296 V 728 A 36 36 0 0 0 336 764 H 728 A 36 36 0 0 0 764 728 V 380 H 644 Z"),
    L(380,520,684,520), L(380,630,590,630)]),
 # table: frame + header row in one line, one column divider
 'table': dict(label='Table', els=[
    P("M 280 420 H 744 V 316 A 36 36 0 0 0 708 280 H 316 A 36 36 0 0 0 280 316 V 708 A 36 36 0 0 0 316 744 H 708 A 36 36 0 0 0 744 708 V 420"),
    L(450,420,450,744)]),
 # Gantt: timeline axis with first and last bar in one line, middle bar offset (echoes the suite E)
 'projet': dict(label='Projet', els=[
    P("M 660 380 H 316 A 36 36 0 0 0 280 416 V 608 A 36 36 0 0 0 316 644 H 600"),
    L(440,512,780,512)]),
 # cloud: download arrow below flows into the cloud, around it, and up as the upload arrow inside
 'nuage': dict(label='Nuage', els=[
    P("M 420 676 L 444 700 L 468 676 M 444 700 V 548 H 380 C 372 548, 366 545, 360 540 C 312 540, 280 506, 280 462 C 280 416, 320 380, 366 384 "
      "C 380 332, 432 296, 488 304 C 540 312, 580 354, 588 408 C 626 400, 668 422, 684 460 C 700 498, 680 540, 640 548 H 540 V 430 "
      "M 516 454 L 540 430 L 564 454")]),
 # stopwatch: stem, dial and both hands in one line; crown bar on top
 'focus': dict(label='Focus', els=[
    P("M 512 300 V 340 A 216 216 0 1 1 512 772 A 216 216 0 1 1 512 340 V 556 L 600 498"),
    L(478,296,546,296)]),
 # nib: tail, outline and slit in one line
 'plume': dict(label='Plume', els=[P("M 500 820 L 540 760 L 380 290 H 740 L 540 760 L 558 340")]),
 # branching game tree: root runs up into the O; second branch runs through the X
 'branchxo': dict(label='BranchXO', els=[
    P("M 300 512 H 452 L 577.6 386.4 A 60 60 0 0 1 662.4 301.6 A 60 60 0 0 1 577.6 386.4"),
    L(452,512,662,722), L(662,638,578,722)]),
 # tesseract: both cubes' faces in one line, joined by one edge; one more connecting edge
 'lattttice': dict(label='Lattttice', els=[
    P("M 324 324 H 604 V 604 H 324 V 324 L 420 420 H 700 V 700 H 420 V 420"),
    L(604,604,700,700), L(604,324,700,420), L(324,604,420,700)]),
}
