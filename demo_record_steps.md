# Recording Steps (short)

## Option A — Asciinema (terminal)
1. Install: `sudo apt install asciinema -y`
2. Record: `asciinema rec demo.cast`
3. Stop with Ctrl-D
4. Upload: `asciinema upload demo.cast` (optional) or convert to GIF/mp4 via `asciinema2gif`/tools

## Option B — Screen recording with ffmpeg
1. Install: `sudo apt install ffmpeg -y`
2. Find display: `echo $DISPLAY` (e.g. :0)
3. Record area (example for full screen):
   ```bash
   ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0 -f pulse -ac 2 -i default demo.mp4
   ```
4. Stop by pressing `q` in terminal running ffmpeg.

Keep demos short — practice beforehand and have outputs ready to avoid long waits.
