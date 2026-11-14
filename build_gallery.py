#!/usr/bin/env python3
"""Make a permanent photo/video gallery automatically from the our-gallery folder."""
from pathlib import Path
import json
folder=Path(__file__).resolve().parent/'assets'/'our-gallery'
photo={'.jpg','.jpeg','.png','.webp','.gif','.avif'}
video={'.mp4','.webm','.mov','.m4v'}
files=sorted((p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in photo|video),key=lambda p:p.name.casefold())
data=[{'type':'video' if p.suffix.lower() in video else 'photo','src':'assets/our-gallery/'+p.name,'name':p.stem.replace('_',' ').replace('-',' ')} for p in files]
(folder/'gallery.js').write_text('window.STORY_GALLERY = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
print(f'Added {len(data)} files to your gallery. Reopen index.html to see them.')
