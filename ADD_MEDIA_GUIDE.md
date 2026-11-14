# Add unlimited photos and videos later

## Quick preview — no file work
Open `index.html`, scroll to **All Our Memories**, and click **Preview photos & videos**. You can select lots of photos/videos at once. They appear immediately, but these temporary choices will vanish when the page is closed. They are **not uploaded** or saved.

## Make photos/videos part of the website permanently
1. Put your photos and videos in `assets/our-gallery/`. Any descriptive filenames are fine. Formats: JPG, JPEG, PNG, WebP, GIF, AVIF, MP4, WebM, MOV, M4V. For best compatibility, use JPG/PNG photos and MP4 (H.264) video.
2. Open Terminal on Mac. Type `cd ` (with a space), drag the extracted `our-love-story-2d` folder into Terminal, then press Return.
3. Run `python3 build_gallery.py` and press Return.
4. Reopen `index.html` in Safari. The gallery now loads all your files automatically, no limit on count.
5. When you add more files later, run the script again. Keep the entire folder together when sharing/publishing the website.

NOTE: Many big videos can make the ZIP and the published site huge. Compress videos for smooth phone playback. Videos won't autoplay. Keep this personal site private until you're comfortable sharing the photos publicly.

## Birthday message
Put the birthday video named `birthday-message.mp4` in `assets/` to activate the video button inside the letter gift.

## Your illustrations
`assets/fizz-original.png` and `assets/arthi-original.png` are the exact unmodified characters you supplied. The final marriage chapter uses your new uploaded couple artwork `assets/our-future-together.png`, unchanged.
