// node render_frames.js job.json  (serve the folder first: npx http-server -p 8765)
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const job = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const fps = job.canvas.fps, total = Math.ceil(job.duration_sec * fps);
  const gpu = ['--use-angle=d3d11', '--ignore-gpu-blocklist', '--enable-gpu-rasterization'];
  const soft = ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'];
  const browser = await chromium.launch({ args: process.env.SOFTWARE_GL ? soft : gpu });
  const page = await browser.newPage({ viewport: { width: job.canvas.width, height: job.canvas.height } });
  page.on('pageerror', e => console.log('PAGE ERROR', e.message));
  await page.goto('http://localhost:8765/scene.html');
  await page.waitForFunction(() => window.ready === true, null, { timeout: 120000 });
  fs.mkdirSync('frames', { recursive: true });
  for (let f = 0; f < total; f++) {
    await page.evaluate(t => window.update(t), f / fps);
    await page.screenshot({ path: `frames/${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    if (f % 30 === 0) console.log('frame', f, '/', total);
  }
  await browser.close();
})();
