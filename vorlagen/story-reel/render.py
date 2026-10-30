import json, sys, subprocess
from playwright.sync_api import sync_playwright

tl = json.load(open("/home/claude/reel/timeline.json"))
html = open("/home/claude/reel/scene.html", encoding="utf-8").read().replace("__TIMELINE__", json.dumps(tl, ensure_ascii=False))
open("/home/claude/reel/build.html", "w", encoding="utf-8").write(html)

mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
FPS = 30

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 540, "height": 960}, device_scale_factor=2)
    pg.goto("file:///home/claude/reel/build.html")
    pg.wait_for_timeout(500)
    lands = pg.evaluate("window.STICKER_LANDS")
    json.dump(lands, open("/home/claude/reel/lands.json", "w"))
    if mode == "preview":
        times = [float(x) for x in sys.argv[2:]]
        for t in times:
            pg.evaluate(f"render({t})")
            pg.screenshot(path=f"/home/claude/reel/prev/f_{t:05.2f}.png")
    else:
        total = tl["total"]
        n = int(total * FPS)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "/home/claude/reel/video_silent.mp4"],
                              stdin=subprocess.PIPE)
        for f in range(n):
            pg.evaluate(f"render({f / FPS})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=93))
            if f % 150 == 0:
                print("frame", f, "/", n, flush=True)
        ff.stdin.close()
        ff.wait()
    b.close()
