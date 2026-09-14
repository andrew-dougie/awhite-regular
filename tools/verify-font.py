"""Validate family names, coverage, outlines and metrics across both formats."""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
from fontTools.pens.recordingPen import RecordingPen
root=Path(__file__).resolve().parents[1];info=json.loads((root/'font.json').read_text())
a=TTFont(root/'fonts'/info['format']/info['filename']);b=TTFont(root/'fonts/woff2'/info['woff2'])
for f in [a,b]:
 assert f['name'].getDebugName(1)==info['family']
 assert f['name'].getDebugName(6)==info['postScriptName']
 assert len(f.getBestCmap())==info['characters']
 assert f['OS/2'].usWeightClass==info['weight']
assert a.getBestCmap()==b.getBestCmap()
assert a['hmtx'].metrics==b['hmtx'].metrics
for name in set(a.getBestCmap().values()):
 pa=RecordingPen();pb=RecordingPen();a.getGlyphSet()[name].draw(pa);b.getGlyphSet()[name].draw(pb);assert pa.value==pb.value,name
print(info['title']+': desktop and web metadata, coverage, outlines and metrics passed.')
