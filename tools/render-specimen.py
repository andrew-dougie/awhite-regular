"""Create the README specimen from the included font's vector outlines."""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
root=Path(__file__).resolve().parents[1];info=json.loads((root/'font.json').read_text());font=TTFont(root/'fonts'/info['format']/info['filename']);cmap=font.getBestCmap();glyphs=font.getGlyphSet();units=font['head'].unitsPerEm
paths=['<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="780" viewBox="0 0 1280 780"><rect width="1280" height="780" rx="20" fill="#17131e"/><path d="M64 220H1216 M64 492H1216" stroke="#67543c" stroke-width="2"/>']
def line(text,x,y,size,color):
 natural=sum(font['hmtx'][cmap.get(ord(c),'.notdef')][0] for c in text)
 scale=min(size/units,1140/max(1,natural));cursor=0
 for c in text:
  if c==' ' and ord(c) not in cmap:
   cursor+=font['hmtx']['.notdef'][0];continue
  name=cmap.get(ord(c),'.notdef');pen=SVGPathPen(glyphs);glyphs[name].draw(pen)
  paths.append(f'<path fill="{color}" d="{pen.getCommands()}" transform="translate({x+cursor*scale:.3f} {y}) scale({scale} {-scale})"/>');cursor+=font['hmtx'][name][0]
line(info['title'],64,166,112,'#ffdd8d')
line('Play    Resume    Try again',70,302,58,'#fff1d2')
line('Return to main menu',70,383,58,'#8de2a1')
line('New high score!    12,345',70,455,50,'#89caff')
line('ABCDEFGHIJKLMNOPQRSTUVWXYZ',70,565,43,'#fff1d2')
line('abcdefghijklmnopqrstuvwxyz',70,633,44,'#fff1d2')
line('0123456789   + - ! ? & @ # %',70,700,43,'#d1bcd7')
paths.append('</svg>');(root/'docs/specimen.svg').write_text('\n'.join(paths))
