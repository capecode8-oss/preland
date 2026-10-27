# Windows render notes
- Check: node -v (20+), ffmpeg -version, py --version. Install with winget: OpenJS.NodeJS.LTS, Gyan.FFmpeg, Python.Python.3.12.
- Project: npm init -y, npm i three playwright, npx playwright install chromium. Serve the folder with `npx http-server -p 8765` (ES modules need http, not file://).
- Chromium flags for the GPU: --use-angle=d3d11 --ignore-gpu-blocklist --enable-gpu-rasterization. Without a GPU the flags --use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader work but are slow (many seconds per frame).
- Word timing: py -m pip install faster-whisper (CPU is fine, model small).
- Remotion alternative: npm create video@latest, npm i three @remotion/three @react-three/fiber, render with npx remotion render --gl=angle --concurrency=50% --codec=h264 --crf=18. Use Studio for live preview.
- Always render ONE still per shot first and a 3 s test clip before the full render.
