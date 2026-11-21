import sys, os, json, io, subprocess, shutil
sys.path.insert(0, os.path.dirname(__file__))
from iconlib import *
from vd import vector_drawable
from glyphs import GLYPHS
from PIL import Image
GH=os.environ.get('ETABLI_ROOT', os.path.expanduser('~/etabli'))  # folder holding the etabli-* clones and .github
written={}
def W(repo, rel, text):
    p=os.path.join(GH,repo,rel); os.makedirs(os.path.dirname(p),exist_ok=True)
    open(p,'w').write(text); written.setdefault(repo,[]).append(rel)
def PNG(repo, rel, svg, size, rgb=False):
    render(svg,size,os.path.join(GH,repo,rel),rgb=rgb); written.setdefault(repo,[]).append(rel)
def ICNS_ICO(repo, relicns, relico, svg):
    png=subprocess.run(['rsvg-convert','-w','1024','-h','1024'],input=svg.encode(),capture_output=True,check=True).stdout
    im=Image.open(io.BytesIO(png)).convert('RGBA')
    if relicns: im.save(os.path.join(GH,repo,relicns)); written.setdefault(repo,[]).append(relicns)
    if relico:
        im.resize((256,256),Image.LANCZOS).save(os.path.join(GH,repo,relico),sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
        written.setdefault(repo,[]).append(relico)

DENS=[('mdpi',1),('hdpi',1.5),('xhdpi',2),('xxhdpi',3),('xxxhdpi',4)]
IOS_FLUTTER=[('20x20@1x',20),('20x20@2x',40),('20x20@3x',60),('29x29@1x',29),('29x29@2x',58),('29x29@3x',87),
             ('40x40@1x',40),('40x40@2x',80),('40x40@3x',120),('60x60@2x',120),('60x60@3x',180),
             ('76x76@1x',76),('76x76@2x',152),('83.5x83.5@2x',167),('1024x1024@1x',1024)]
MACOS=[16,32,64,128,256,512,1024]

def flutter(app, has_adaptive=True):
    repo=f'etabli-{app}'
    W(repo,f'design/icon-{app}.svg',full(app)); W(repo,f'docs/_icons/icon-{app}.svg',full(app))
    W(repo,f'design/icon-{app}-foreground.svg',foreground(app,w=432))
    for d,f in DENS:
        PNG(repo,f'android/app/src/main/res/mipmap-{d}/ic_launcher.png',full(app),int(48*f),rgb=True)
        PNG(repo,f'android/app/src/main/res/mipmap-{d}/ic_launcher_foreground.png',foreground(app),int(108*f))
    if not has_adaptive:
        W(repo,'android/app/src/main/res/mipmap-anydpi-v26/ic_launcher.xml',
          '<?xml version="1.0" encoding="utf-8"?>\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
          '    <background android:drawable="@color/ic_launcher_background" />\n    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n'
          '    <monochrome android:drawable="@mipmap/ic_launcher_foreground" />\n</adaptive-icon>\n')
        W(repo,'android/app/src/main/res/values/ic_launcher_background.xml',
          '<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#28A745</color>\n</resources>\n')
    for nm,sz in IOS_FLUTTER:
        PNG(repo,f'ios/Runner/Assets.xcassets/AppIcon.appiconset/Icon-App-{nm}.png',full(app),sz,rgb=True)
    for sz in MACOS:
        PNG(repo,f'macos/Runner/Assets.xcassets/AppIcon.appiconset/app_icon_{sz}.png',desktop(app),sz)

def native(app, desktop_pkg=False, extra_fg_svg=False, extra=None):
    repo=f'etabli-{app}'
    W(repo,f'design/icon-{app}.svg',full(app)); W(repo,f'docs/_icons/icon-{app}.svg',full(app))
    if extra_fg_svg: W(repo,f'design/icon-{app}-foreground.svg',foreground(app,w=432))
    W(repo,'android/app/src/main/res/drawable/ic_launcher_foreground.xml',vector_drawable(app))
    for d,f in DENS:
        PNG(repo,f'android/app/src/main/res/mipmap-{d}/ic_launcher.png',full(app),int(48*f),rgb=True)
        PNG(repo,f'android/app/src/main/res/mipmap-{d}/ic_launcher_round.png',circle_icon(app),int(48*f))
    PNG(repo,'ios/App/Assets.xcassets/AppIcon.appiconset/AppIcon.png',full(app),1024,rgb=True)
    if desktop_pkg:
        PNG(repo,'desktop/packaging/icon.png',desktop(app),512)
        ICNS_ICO(repo,'desktop/packaging/icon.icns','desktop/packaging/icon.ico',desktop(app))
    for rel,size in (extra or []):
        PNG(repo,rel,desktop(app),size)

def expo_tauri(app):
    repo=f'etabli-{app}'
    W(repo,'assets/icon.svg',full(app)); W(repo,f'docs/assets/icon-{app}.svg',full(app))
    PNG(repo,'assets/icon.png',full(app),1024,rgb=True)
    adaptive=(HDR.format(label=GLYPHS[app]['label'])+f'  <rect width="1024" height="1024" fill="{GREEN}"/>\n  {glyph_svg(app,k=0.64)}\n</svg>\n')
    if os.path.exists(os.path.join(GH,repo,'assets/adaptive-icon.svg')): W(repo,'assets/adaptive-icon.svg',adaptive)
    PNG(repo,'assets/adaptive-icon.png',adaptive,1024,rgb=True)
    PNG(repo,'assets/favicon.png',full(app),196,rgb=True)
    for rel,sz in [('src-tauri/icons/32x32.png',32),('src-tauri/icons/128x128.png',128),('src-tauri/icons/128x128@2x.png',256),('src-tauri/icons/icon.png',512)]:
        PNG(repo,rel,desktop(app),sz)
    ICNS_ICO(repo,'src-tauri/icons/icon.icns','src-tauri/icons/icon.ico',desktop(app))
    # small Établi suite mark used in the docs header
    logo=rounded('suite',rx_frac=0.22).replace('width="1024" height="1024" viewBox','width="32" height="32" viewBox')
    W(repo,'docs/assets/etabli-logo.svg',logo)

def recueil():
    repo='etabli-recueil'; app='recueil'
    W(repo,'apps/web/public/icons/recueil.svg',rounded(app))
    PNG(repo,'apps/web/public/icons/icon-192.png',rounded(app),192)
    PNG(repo,'apps/web/public/icons/icon-512.png',rounded(app),512)
    PNG(repo,'apps/web/public/icons/icon-maskable-512.png',maskable(app),512,rgb=True)
    for rel,sz in [('apps/desktop/src-tauri/icons/32x32.png',32),('apps/desktop/src-tauri/icons/128x128.png',128),('apps/desktop/src-tauri/icons/128x128@2x.png',256)]:
        PNG(repo,rel,desktop(app),sz)
    ICNS_ICO(repo,'apps/desktop/src-tauri/icons/icon.icns','apps/desktop/src-tauri/icons/icon.ico',desktop(app))

def profile():
    repo='.github'
    W(repo,'profile/icons/etabli-suite.svg',full('suite'))
    W(repo,'profile/icons/etabli-suite-dark.svg',full('suite',bg=DARK,fg=GREEN))
    for app in ['atelier','vitrine','courrier','recueil','doc','table','projet','nuage','focus','plume','branchxo','lattttice']:
        W(repo,f'profile/icons/icon-{app}.svg',full(app))

if __name__=='__main__':
    flutter('atelier'); flutter('vitrine'); flutter('courrier',has_adaptive=False)
    W('etabli-courrier','design/icon-courrier.svg',full('courrier'))
    native('doc',extra_fg_svg=True); native('table'); native('projet'); native('plume')
    native('focus',desktop_pkg=True)
    native('nuage',desktop_pkg=True,extra=[('desktop/src/main/resources/nuage-icon.png',256)])
    expo_tauri('branchxo'); expo_tauri('lattttice')
    recueil(); profile()
    for r,fs in written.items(): print(f'{r:18s} {len(fs)} files')
