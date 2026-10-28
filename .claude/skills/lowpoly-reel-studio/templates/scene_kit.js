// Low-poly reel kit for Three.js (r160+). ES module. Deterministic: call update(t) with time in seconds, no real-time clocks.
import * as THREE from 'three';

export const PALETTE = {
  eveningBg: 0xff9a6b, morningSky: 0x8fd3f5, wall: 0xe9c9b5, counterTop: 0xf4efe9, counterBody: 0x7d5c8a,
  heroShirt: 0x5b7fd6, skin: 0xf1b88d, hair: 0x4a2f23, accent: 0xffd24a, red: 0xe63946, green: 0x3ddc84, white: 0xffffff,
};

export const ease = {
  outCubic: t => 1 - Math.pow(1 - t, 3),
  inOutCubic: t => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
  outBack: t => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(t - 1, 3) + c1 * Math.pow(t - 1, 2); },
  clamp01: t => Math.min(1, Math.max(0, t)),
};
// progress of an action starting at `start` lasting `dur` seconds, eased
export const prog = (t, start, dur, fn = ease.outCubic) => fn(ease.clamp01((t - start) / dur));

export function makeRenderer(w = 1080, h = 1920, mount = document.body) {
  const r = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  r.setSize(w, h); r.shadowMap.enabled = true; r.shadowMap.type = THREE.PCFSoftShadowMap; mount.prepend(r.domElement);
  return r;
}

export const mat = (color, o = {}) => new THREE.MeshStandardMaterial({ color, flatShading: true, roughness: .9, ...o });
export function mesh(scene, geo, m, x = 0, y = 0, z = 0, rx = 0, ry = 0, rz = 0) {
  const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.rotation.set(rx, ry, rz); o.castShadow = o.receiveShadow = true; scene.add(o); return o;
}
export const box = (w, h, d) => new THREE.BoxGeometry(w, h, d);

// mood: 'evening' | 'morning'
export function makeLights(scene, mood = 'evening') {
  const eve = mood === 'evening';
  const key = new THREE.DirectionalLight(eve ? 0xffb98a : 0xffffff, eve ? 1.6 : 2.4);
  key.position.set(-6, 7, 8); key.castShadow = true; key.shadow.mapSize.set(2048, 2048); key.shadow.radius = 4;
  Object.assign(key.shadow.camera, { left: -10, right: 10, top: 10, bottom: -10 }); scene.add(key);
  scene.add(new THREE.HemisphereLight(eve ? 0xffd9c0 : 0xffffff, eve ? 0x6a4a6a : 0xaabbcc, eve ? .9 : 1.1));
  if (eve) { const l = new THREE.PointLight(0xffc46b, 60, 16, 1.6); l.position.set(-4.4, 4.6, -1.6); scene.add(l); }
  scene.background = new THREE.Color(eve ? 0x3a2a3f : 0xdff1fb);
}

// Apartment kitchen-living room: floor, back wall with window + city, counter island, sofa, plant, lamp, rug.
export function makeRoom(scene, mood = 'evening') {
  const eve = mood === 'evening', sky = eve ? PALETTE.eveningBg : PALETTE.morningSky, wall = eve ? 0xe9c9b5 : 0xf6e6d6;
  mesh(scene, box(26, .2, 22), mat(eve ? 0xb98a62 : 0xd9b48a), 0, -.1, 0);
  mesh(scene, box(8, 14, .4), mat(wall), -7.5, 7, -6); mesh(scene, box(8, 14, .4), mat(wall), 7.5, 7, -6);
  mesh(scene, box(7, 6, .4), mat(wall), 0, 11, -6); mesh(scene, box(7, 3.4, .4), mat(wall), 0, 1.7, -6);
  mesh(scene, box(7, 4.6, .1), new THREE.MeshBasicMaterial({ color: sky }), 0, 5.7, -6.15);
  const bc = eve ? [0x5a3d5e, 0x6c4a63, 0x7a5568] : [0xa9c7dd, 0xbcd6e6, 0x93b4cc];
  for (let i = 0; i < 9; i++) { const h = 1.2 + ((i * 37) % 5) * .6; mesh(scene, box(.9, h, .6), mat(bc[i % 3]), -3.2 + i * .8, 3.4 + h / 2 - .1, -6.5); }
  const fr = mat(0xf4efe9);
  mesh(scene, box(7.4, .25, .5), fr, 0, 3.3, -5.9); mesh(scene, box(7.4, .25, .5), fr, 0, 8, -5.9);
  mesh(scene, box(.25, 4.9, .5), fr, -3.6, 5.65, -5.9); mesh(scene, box(.25, 4.9, .5), fr, 3.6, 5.65, -5.9);
  mesh(scene, box(9, .06, 5), mat(eve ? 0x6fa8a0 : 0x8fd0c4), 0, .03, .5);
  mesh(scene, box(5.2, 1.1, 2.1), mat(0xd9604a), -4.3, .55, -3.6); mesh(scene, box(5.2, 1.5, .6), mat(0xc9503b), -4.3, 1.4, -4.55);
  mesh(scene, new THREE.CylinderGeometry(.55, .4, .9, 7), mat(0xc67b4f), 4.4, .45, -4.2);
  mesh(scene, new THREE.IcosahedronGeometry(.9, 0), mat(0x3fae6a), 4.4, 1.7, -4.2);
  mesh(scene, box(10.5, 2.3, 2.4), mat(PALETTE.counterBody), 0, 1.15, -.6); mesh(scene, box(10.9, .28, 2.8), mat(PALETTE.counterTop), 0, 2.44, -.6);
  return { counterTopY: 2.58 };
}

// Blocky hero with expressions: 'neutral'|'tempted'|'effort'|'happy'|'shock'. Returns {group, head, armL, armR, setExpression, blink}
export function makeHero(scene, { shirt = PALETTE.heroShirt, x = .6, y = 2.4, z = -1.2 } = {}) {
  const g = new THREE.Group(); scene.add(g);
  const add = (geo, m, px, py, pz, par = g) => { const o = new THREE.Mesh(geo, m); o.position.set(px, py, pz); o.castShadow = true; par.add(o); return o; };
  const bodyMat = mat(shirt); add(box(2, 2.4, 1.2), bodyMat, 0, 1.2, 0);
  const head = new THREE.Group(); head.position.set(0, 3.2, 0); g.add(head);
  add(box(1.7, 1.7, 1.5), mat(PALETTE.skin), 0, 0, 0, head); add(box(1.85, .7, 1.65), mat(PALETTE.hair), 0, .95, -.05, head); add(box(1.85, 1, .5), mat(PALETTE.hair), 0, .45, -.55, head);
  const eyeW = [-.4, .4].map(x => add(box(.34, .38, .08), mat(0xffffff), x, .1, .76, head));
  const pupils = [-.4, .4].map(x => add(box(.16, .2, .1), mat(0x1a1a1a), x, .08, .8, head));
  const brows = [-.4, .4].map(x => add(box(.5, .1, .08), mat(0x3a2418), x, .5, .78, head));
  const mouth = add(box(.6, .12, .08), mat(0x8c2f3a), 0, -.5, .77, head);
  const armL = new THREE.Group(), armR = new THREE.Group(); armL.position.set(-1.25, 2.2, 0); armR.position.set(1.25, 2.2, 0); g.add(armL, armR);
  [armL, armR].forEach(a => { add(box(.55, 1.9, .55), bodyMat, 0, -.9, 0, a); add(box(.6, .6, .6), mat(PALETTE.skin), 0, -2, 0, a); });
  g.position.set(x, y, z); g.rotation.y = -.12;
  const E = {
    neutral: { bl: .05, br: -.05, by: .5, mw: .6, mh: .12 }, tempted: { bl: .25, br: -.25, by: .52, mw: .8, mh: .34 },
    effort: { bl: -.35, br: .35, by: .42, mw: .55, mh: .1 }, happy: { bl: .12, br: -.12, by: .5, mw: .9, mh: .2 }, shock: { bl: .3, br: -.3, by: .62, mw: .5, mh: .5 },
  };
  function setExpression(name) {
    const e = E[name] || E.neutral; brows[0].rotation.z = e.bl; brows[1].rotation.z = e.br; brows.forEach(b => b.position.y = e.by);
    mouth.scale.set(e.mw / .6, e.mh / .12, 1);
  }
  function blink(t) { const k = (t % 2.6) > 2.5 ? .1 : 1; eyeW.forEach(m => m.scale.y = k); pupils.forEach(m => m.scale.y = k); }
  setExpression('neutral');
  return { group: g, head, armL, armR, setExpression, blink };
}

// Props. All return the mesh/group so you can animate position/scale with prog().
export function sugarSpoon(scene) {
  const g = new THREE.Group(); scene.add(g);
  const add = (geo, m, x, y, z) => { const o = new THREE.Mesh(geo, m); o.position.set(x, y, z); o.castShadow = true; g.add(o); return o; };
  add(new THREE.CapsuleGeometry(.05, .8, 3, 6), mat(0xc9d1d9, { metalness: .4 }), 0, 0, 0).rotation.z = Math.PI / 2;
  add(new THREE.SphereGeometry(.22, 7, 5), mat(0xc9d1d9, { metalness: .4 }), .5, 0, 0).scale.set(1, .4, 1);
  for (let i = 0; i < 12; i++) add(box(.09, .09, .09), mat(0xffffff), .4 + (i % 4) * .07, .1 + Math.floor(i / 4) * .06, (i % 3 - 1) * .07);
  return g;
}
export const can = (scene, color = PALETTE.red) => { const g = new THREE.Group(); scene.add(g); [[new THREE.CylinderGeometry(.34, .34, 1.05, 8), mat(color), 0], [new THREE.CylinderGeometry(.35, .35, .09, 8), mat(0xdddddd), .56]].forEach(([geo, m, y]) => { const o = new THREE.Mesh(geo, m); o.position.y = y; o.castShadow = true; g.add(o); }); return g; };
export const glassJar = (scene, h = 3) => mesh(scene, new THREE.CylinderGeometry(1, .9, h, 10, 1, true), mat(0xcfefff, { transparent: true, opacity: .35, side: 2 }), 0, h / 2, 0);

// Camera helpers: slow dolly toward target (pct = 0.06 means 6 percent closer over the shot)
export function setCamera(cam, { pos = [.6, 6.4, 19.5], look = [.6, 4.5, -1.2] } = {}) { cam.position.set(...pos); cam.lookAt(...look); }
export function dolly(cam, base, look, t, dur, pct = .06) { const k = prog(t, 0, dur, ease.inOutCubic) * pct; cam.position.set(base[0] + (look[0] - base[0]) * k, base[1] + (look[1] - base[1]) * k, base[2] + (look[2] - base[2]) * k); cam.lookAt(...look); }
