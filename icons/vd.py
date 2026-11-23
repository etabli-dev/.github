# Android VectorDrawable (adaptive-icon foreground) from glyph definitions.
from glyphs import GLYPHS
from iconlib import placement, STROKE
def rect_d(x,y,w,h,rx):
    if not rx: return f"M{x},{y} H{x+w} V{y+h} H{x} Z"
    return (f"M{x+rx},{y} H{x+w-rx} A{rx},{rx} 0 0 1 {x+w},{y+rx} V{y+h-rx} A{rx},{rx} 0 0 1 {x+w-rx},{y+h} "
            f"H{x+rx} A{rx},{rx} 0 0 1 {x},{y+h-rx} V{y+rx} A{rx},{rx} 0 0 1 {x+rx},{y} Z")
def el_d(e):
    t=e['t']
    if t=='path': return e['d']
    if t=='line': return f"M{e['x1']},{e['y1']} L{e['x2']},{e['y2']}"
    if t=='rect': return rect_d(e['x'],e['y'],e['w'],e['h'],e['rx'])
    if t=='circle':
        cx,cy,r=e['cx'],e['cy'],e['r']; return f"M{cx-r},{cy} A{r},{r} 0 1 0 {cx+r},{cy} A{r},{r} 0 1 0 {cx-r},{cy} Z"
def vector_drawable(name, k=0.64, fg='#FFFFFF', bg='#28A745'):
    s,cx,cy=placement(name); K=(108/1024)*k*s; sw=STROKE/s
    out=[]
    for e in GLYPHS[name]['els']:
        col = bg if e.get('color')=='knock' else fg
        if e.get('fill'): paint=f'android:fillColor="{col}"'
        elif e.get('bgfill'): paint=(f'android:fillColor="{bg}" android:strokeColor="{col}" android:strokeWidth="{sw:.3f}" '
                                     f'android:strokeLineCap="round" android:strokeLineJoin="round"')
        else: paint=(f'android:strokeColor="{col}" android:strokeWidth="{sw:.3f}" '
                     f'android:strokeLineCap="round" android:strokeLineJoin="round"')
        p=f'<path android:pathData="{el_d(e)}"\n            {paint}/>'
        if e.get('rot'):
            a,px,py=e['rot']; p=f'<group android:rotation="{a}" android:pivotX="{px}" android:pivotY="{py}">\n            {p}\n        </group>'
        out.append('        '+p)
    body='\n'.join(out)
    lab=GLYPHS[name]['label']
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!-- Établi {lab}: adaptive-icon foreground, generated from the shared icon glyph
     (glyph ≈70% of the visible icon, stroke 44 @1024; aligned to the Établi suite icon, Nov 2026). -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <group android:scaleX="{K:.6f}" android:scaleY="{K:.6f}"
        android:translateX="{54-K*cx:.4f}" android:translateY="{54-K*cy:.4f}">
{body}
    </group>
</vector>
'''
def vd_to_svg(xml):
    """re-render a generated VectorDrawable as SVG for verification (handles every top-level group)"""
    import re
    groups=re.split(r'(?=<group android:scaleX)',xml)[1:]
    out=''
    for gx in groups:
        out+=_vd_group(gx)
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 108 108"><rect width="108" height="108" fill="#28A745"/>{out}</svg>'
def _vd_group(xml):
    import re
    g=re.search(r'scaleX="([\d.]+)".*?translateX="([-\d.]+)" android:translateY="([-\d.]+)"',xml,re.S)
    K,tx,ty=map(float,g.groups())
    parts=[]
    for m in re.finditer(r'(<group android:rotation="([-\d.]+)" android:pivotX="([-\d.]+)" android:pivotY="([-\d.]+)">\s*)?<path android:pathData="([^"]+)"\s*([^/]*)/>',xml):
        rot=m.group(2); d=m.group(5); attrs=m.group(6)
        fill=re.search(r'fillColor="([^"]+)"',attrs); stroke=re.search(r'strokeColor="([^"]+)"',attrs); sw=re.search(r'strokeWidth="([\d.]+)"',attrs)
        a=f'fill="{fill.group(1) if fill else "none"}" stroke="{stroke.group(1) if stroke else "none"}" stroke-width="{sw.group(1) if sw else 0}" stroke-linecap="round" stroke-linejoin="round"'
        tr=f' transform="rotate({rot} {m.group(3)} {m.group(4)})"' if rot else ''
        parts.append(f'<path d="{d}" {a}{tr}/>')
    return f'<g transform="translate({tx},{ty}) scale({K})">{"".join(parts)}</g>'
