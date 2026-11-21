import subprocess, os, io
from glyphs import GLYPHS
GREEN='#28A745'; DARK='#121417'; WHITE='#FFFFFF'
STROKE=44          # final stroke at 1024
TARGET=720         # max outer extent of glyph at 1024 (≈70% fill, matches the suite icon)
OPTICAL={'vitrine':670,'doc':680,'table':660,'lattttice':660,'recueil':700,'branchxo':700}         # optical size balance for square glyphs

def el_svg(e, fg, knock, sw):
    col = knock if e.get('color')=='knock' else fg
    tr = f' transform="rotate({e["rot"][0]} {e["rot"][1]} {e["rot"][2]})"' if e.get('rot') else ''
    if e.get('fill'): paint=f'fill="{col}" stroke="none"'
    elif e.get('bgfill'): paint=f'fill="{knock}" stroke="{col}"'
    else: paint=f'fill="none" stroke="{col}"' + (f' stroke-width="{sw:.3f}"' if e.get('color')=='knock' else '')
    t=e['t']
    if t=='path': return f'<path d="{e["d"]}" {paint}{tr}/>'
    if t=='line': return f'<line x1="{e["x1"]}" y1="{e["y1"]}" x2="{e["x2"]}" y2="{e["y2"]}" {paint}{tr}/>'
    if t=='rect': return f'<rect x="{e["x"]}" y="{e["y"]}" width="{e["w"]}" height="{e["h"]}" rx="{e["rx"]}" {paint}{tr}/>'
    if t=='circle': return f'<circle cx="{e["cx"]}" cy="{e["cy"]}" r="{e["r"]}" {paint}{tr}/>'

def raw_group(name, fg, knock, sw):
    g=GLYPHS[name]
    body='\n    '.join(el_svg(e,fg,knock,sw) for e in g['els'])
    return f'<g stroke-width="{sw:.3f}" stroke-linecap="round" stroke-linejoin="round">\n    {body}\n  </g>'

_cache={}
def centerline_bbox(name):
    if name in _cache: return _cache[name]
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="2048" height="2048" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="#000"/>{raw_group(name,"#fff","#fff",1)}</svg>'
    png=subprocess.run(['rsvg-convert'],input=svg.encode(),capture_output=True,check=True).stdout
    from PIL import Image
    im=Image.open(io.BytesIO(png)).convert('L').point(lambda v:255 if v>60 else 0)
    x0,y0,x1,y1=im.getbbox(); bb=(x0/2,y0/2,x1/2,y1/2)
    _cache[name]=bb; return bb

_place_cache={}
def placement(name):
    """scale s and centre so the glyph's outer extent = target, centred at 512,512"""
    if name in _place_cache: return _place_cache[name]
    if name=='suite':
        r=(1.40,512,532.5); _place_cache[name]=r; return r          # approved size C
    x0,y0,x1,y1=centerline_bbox(name)
    w,h=x1-x0,y1-y0; T=OPTICAL.get(name,TARGET)
    stroked=GLYPHS[name].get('stroked',True)
    s=(T-(STROKE if stroked else 0))/max(w,h)
    r=(s,(x0+x1)/2,(y0+y1)/2); _place_cache[name]=r; return r
def glyph_svg(name, fg=WHITE, knock=GREEN, k=1.0, cx0=512, cy0=512):
    """glyph group placed in 1024 space; k = extra scale (foreground/maskable/desktop body)"""
    s,cx,cy=placement(name); S=s*k
    sw=STROKE*k/S
    return f'<g transform="translate({cx0},{cy0}) scale({S:.5f}) translate({-cx:.2f},{-cy:.2f})">\n  {raw_group(name,fg,knock,sw)}\n  </g>'

CLIP_ROUNDED='<clipPath id="tile"><rect width="1024" height="1024" rx="{rx}"/></clipPath>'
HDR='<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024" role="img" aria-label="{label}">\n  <!-- Établi {label} icon. Coder design system: #28A745 tile, white glyph, one-line glyph ≈70% of the tile, stroke 44 @1024 (aligned to the suite icon, Nov 2026). -->\n'
def full(name, bg=GREEN, fg=WHITE):
    lab=GLYPHS[name]['label']
    return HDR.format(label=lab)+f'  <rect width="1024" height="1024" fill="{bg}"/>\n  {glyph_svg(name,fg,bg)}\n</svg>\n'
def foreground(name, k=0.64, w=1024):
    lab=GLYPHS[name]['label']
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w}" viewBox="0 0 1024 1024">\n'
            f'  <!-- Établi {lab}: Android adaptive-icon foreground (glyph scaled into the safe zone; background #28A745). -->\n'
            f'  {glyph_svg(name,WHITE,GREEN,k)}\n</svg>\n')
def rounded(name, rx_frac=0.1875):
    """full canvas, rounded corners baked in (web 'any' icons)"""
    lab=GLYPHS[name]['label']; rx=1024*rx_frac
    return (HDR.format(label=lab)+f'  <defs><clipPath id="tile"><rect width="1024" height="1024" rx="{rx:.0f}"/></clipPath></defs>\n'
            f'  <rect width="1024" height="1024" rx="{rx:.0f}" fill="{GREEN}"/>\n  <g clip-path="url(#tile)">{glyph_svg(name)}</g>\n</svg>\n')
def desktop(name):
    """macOS template: 824 body at 100px inset, corner radius 185; transparent margin"""
    lab=GLYPHS[name]['label']
    return (HDR.format(label=lab)+'  <defs><clipPath id="body"><rect x="100" y="100" width="824" height="824" rx="185"/></clipPath></defs>\n'
            f'  <rect x="100" y="100" width="824" height="824" rx="185" fill="{GREEN}"/>\n  <g clip-path="url(#body)">{glyph_svg(name,k=824/1024)}</g>\n</svg>\n')
def maskable(name):
    lab=GLYPHS[name]['label']
    return HDR.format(label=lab)+f'  <rect width="1024" height="1024" fill="{GREEN}"/>\n  {glyph_svg(name,k=0.78)}\n</svg>\n'
def circle_icon(name):
    lab=GLYPHS[name]['label']
    return (HDR.format(label=lab)+'  <defs><clipPath id="round"><circle cx="512" cy="512" r="512"/></clipPath></defs>\n'
            f'  <circle cx="512" cy="512" r="512" fill="{GREEN}"/>\n  <g clip-path="url(#round)">{glyph_svg(name,k=0.86)}</g>\n</svg>\n')

def render(svg, size, out, rgb=False):
    os.makedirs(os.path.dirname(out) or '.', exist_ok=True)
    png=subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size)],input=svg.encode(),capture_output=True,check=True).stdout
    from PIL import Image
    im=Image.open(io.BytesIO(png))
    if rgb: im=im.convert('RGB')
    else: im=im.convert('RGBA')
    im.save(out)
    return out
