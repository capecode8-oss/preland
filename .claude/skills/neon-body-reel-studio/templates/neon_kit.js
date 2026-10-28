// Neon glowing body-silhouette kit (SVG + CSS, no WebGL, renders fast on any computer).
// Deterministic: every animated thing is a function of t (seconds). Use with window.update(t).
export const NEON = {
  bgTop: '#0B1020', bgBottom: '#16203F',            // deep navy, calm
  teal: '#5EE6D3', cyan: '#7DD3FC', violet: '#A78BFA', // main glows
  rose: '#FF8FB1', peach: '#FFB48A',                  // women / warm, soft, never saturated red
  amber: '#FFD27A', mint: '#8BF0C1',                  // accents, good news
  alert: '#FF9E7A',                                   // "warning" = soft coral, NOT red
  text: '#FFFFFF', dim: '#7C86A8',
};
export const ease = { out: t => 1 - Math.pow(1 - t, 3), inOut: t => (t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3)/2), clamp: t => Math.min(1, Math.max(0, t)) };
export const prog = (t, s, d, f = ease.out) => f(ease.clamp((t - s) / d));

export function defs() {
  return `<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${NEON.bgTop}"/><stop offset="1" stop-color="${NEON.bgBottom}"/></linearGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="22"/></filter>
  </defs>`;
}
// bokeh circles in the background, drifting slowly with t
export function bokeh(t, w = 1080, h = 1920, n = 14) {
  let s = '';
  for (let i = 0; i < n; i++) {
    const x = (i * 197) % w, y = ((i * 331) % h) + Math.sin(t * .3 + i) * 18, r = 40 + (i * 29) % 90, c = [NEON.violet, NEON.teal, NEON.rose][i % 3];
    s += `<circle cx="${x}" cy="${y}" r="${r}" fill="${c}" opacity="0.07" filter="url(#soft)"/>`;
  }
  return s;
}
// full body silhouette in a 300x700 box. gender: 'f' | 'm'. pulse in 0..1 adds a breathing glow.
// Two passes: first ALL glowing strokes (union outline), then ALL dark fills on top, so limbs merge into one clean neon outline.
export function body({ gender = 'f', color = NEON.rose, scale = 1, x = 0, y = 0, pulse = 0, fill = '#111A38' } = {}) {
  const f = gender === 'f', sh = f ? 36 : 48, hip = f ? 40 : 30;
  const seg = [ // [x1,y1,x2,y2,width]
    [150, 62, 150, 62, 70],                                              // head
    [150, 112, 150, 130, 22],                                            // neck
    [150 - sh, 140, 150 + sh, 140, 30],                                  // shoulders
    [150 - sh + 6, 150, 150 - hip + 8, 330, f ? 66 : 74], [150 + sh - 6, 150, 150 + hip - 8, 330, f ? 66 : 74], // torso
    [150 - sh - 6, 152, 150 - sh - 30, 300, 26], [150 + sh + 6, 152, 150 + sh + 30, 300, 26],                  // arms
    [150 - hip + 8, 340, 150 - hip, 640, 42], [150 + hip - 8, 340, 150 + hip, 640, 42],                         // legs
  ];
  const line = (s, c, w, extra = '') => `<line x1="${s[0]}" y1="${s[1]}" x2="${s[2]}" y2="${s[3]}" stroke="${c}" stroke-width="${w}" stroke-linecap="round" ${extra}/>`;
  const glowLayer = `<g filter="url(#glow)">${seg.map(s => line(s, color, s[4])).join('')}</g>`;
  const darkLayer = seg.map(s => line(s, fill, s[4] - 8)).join('');
  const aura = `<ellipse cx="150" cy="330" rx="${120 + pulse * 20}" ry="${300 + pulse * 20}" fill="${color}" opacity="${0.06 + pulse * 0.06}" filter="url(#soft)"/>`;
  return `<g transform="translate(${x} ${y}) scale(${scale})">${aura}${glowLayer}${darkLayer}</g>`;
}
// glowing organ blob (heart/lung/brain as simple shapes). kind: 'heart'|'circle'
export function organ({ x, y, r = 40, color = NEON.rose, beat = 0 }) {
  const k = 1 + beat * 0.12;
  return `<g transform="translate(${x} ${y}) scale(${k})"><circle r="${r * 1.8}" fill="${color}" opacity=".18" filter="url(#soft)"/><circle r="${r}" fill="${color}" opacity=".85" filter="url(#glow)"/><circle r="${r * .45}" cx="${-r * .25}" cy="${-r * .25}" fill="#fff" opacity=".35"/></g>`;
}
// vertical ruler with labelled ticks (e.g. years). value in 0..1 shows a glowing marker
export function ruler({ x, y, h = 560, color = NEON.amber, value = 0, ticks = 6, label = '' }) {
  let s = `<line x1="${x}" y1="${y}" x2="${x}" y2="${y + h}" stroke="${color}" stroke-width="5" opacity=".7" filter="url(#glow)"/>`;
  for (let i = 0; i <= ticks; i++) s += `<line x1="${x - 12}" y1="${y + h * i / ticks}" x2="${x + 12}" y2="${y + h * i / ticks}" stroke="${color}" stroke-width="3" opacity=".6"/>`;
  const my = y + h - h * value;
  s += `<circle cx="${x}" cy="${my}" r="14" fill="${color}" filter="url(#glow)"/>`;
  if (label) s += `<text x="${x}" y="${y + h + 46}" fill="${color}" font-size="30" font-family="Montserrat" font-weight="700" text-anchor="middle">${label}</text>`;
  return s;
}
// karaoke subtitles: words already spoken are white, current is accent, upcoming are dim gray. words=[{w,start,end}]
export function karaoke(words, t, { y = 1260, size = 76, perLine = 3 } = {}) {
  const i = words.findIndex(w => t < w.end); const cur = i < 0 ? words.length - 1 : i;
  const from = Math.floor(cur / (perLine * 2)) * perLine * 2, chunk = words.slice(from, from + perLine * 2);
  const lines = [chunk.slice(0, perLine), chunk.slice(perLine)];
  return lines.map((ln, li) => `<text x="540" y="${y + li * (size + 14)}" font-size="${size}" font-family="Montserrat" font-weight="700" text-anchor="middle">` +
    ln.map(w => { const idx = words.indexOf(w); const c = idx < cur ? NEON.text : idx === cur ? NEON.amber : NEON.dim; return `<tspan fill="${c}">${w.w} </tspan>`; }).join('') + `</text>`).join('');
}
export const frame = (inner) => `<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920">${defs()}<rect width="1080" height="1920" fill="url(#bg)"/>${inner}</svg>`;
