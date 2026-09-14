"""Export WOFF2 and the character map from the included desktop font."""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
root=Path(__file__).resolve().parents[1];info=json.loads((root/'font.json').read_text())
font=TTFont(root/'fonts'/info['format']/info['filename']);font.recalcTimestamp=False
(root/'fonts/woff2').mkdir(exist_ok=True)
font.flavor='woff2';font.save(root/'fonts/woff2'/info['woff2'])
(root/'fonts/characters.json').write_text(json.dumps({f'U+{c:04X}':chr(c) for c in sorted(font.getBestCmap())},ensure_ascii=False,indent=2)+'\n')
print('Packaged',info['title'],len(font.getBestCmap()),'characters.')
