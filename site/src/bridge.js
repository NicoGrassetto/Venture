import {
  BufferGeometry,
  Color,
  Float32BufferAttribute,
  OrthographicCamera,
  Points,
  Scene,
  ShaderMaterial,
  WebGLRenderer,
} from 'three';

export function createBridgeGeometry() {
  const positions = [];
  const opacities = [];
  const sizes = [];
  const regions = [];
  const tones = [];
  let seed = 8199;
  const random = () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    return seed / 4294967296;
  };

  function point(x, y, z, opacity = 0.8, region = 0) {
    positions.push(x, y, z);
    opacities.push(opacity * (0.65 + random() * 0.35));
    sizes.push(0.9 + random() * 1.2);
    regions.push(region);
    tones.push(region === 0 && random() > 0.88 ? 0.55 : 0.025);
  }

  function line(from, to, opacity = 0.8, spacing = 0.045) {
    const count = Math.ceil(Math.hypot(...to.map((value, index) => value - from[index])) / spacing);
    for (let i = 0; i <= count; i++) {
      const t = count === 0 ? 0 : i / count;
      const coordinate = from.map((value, axis) => value + (to[axis] - value) * t + (random() - 0.5) * 0.022);
      point(...coordinate, opacity);
    }
  }

  function box(center, dimensions, opacity = 0.6, spacing = 0.09) {
    for (let normal = 0; normal < 3; normal++) {
      const u = (normal + 1) % 3;
      const v = (normal + 2) % 3;
      const uCount = Math.ceil(dimensions[u] / spacing);
      const vCount = Math.ceil(dimensions[v] / spacing);
      for (const side of [-1, 1]) {
        for (let i = 0; i <= uCount; i++) {
          for (let j = 0; j <= vCount; j++) {
            if (random() < 0.13) continue;
            const coordinate = [...center];
            coordinate[normal] += dimensions[normal] * side / 2;
            coordinate[u] += dimensions[u] * (i / uCount - 0.5);
            coordinate[v] += dimensions[v] * (j / vCount - 0.5);
            point(...coordinate, opacity);
          }
        }
      }
    }
  }

  // Two portal towers, including the stepped crowns and cross-bracing.
  for (const x of [-4.6, 4.6]) {
    for (const z of [-0.72, 0.72]) {
      box([x, 1.4, z], [0.32, 6.6, 0.32], 0.85, 0.07);
      box([x, 4.88, z], [0.24, 0.36, 0.24], 0.9, 0.06);
      box([x, -1.72, z], [0.64, 0.4, 0.68], 0.4);
      for (const offset of [-0.16, 0.16]) {
        line([x + offset, -1.8, z + 0.16], [x + offset, 4.7, z + 0.16], 0.95);
      }
    }
    for (const y of [1.35, 2.85, 4.45]) {
      box([x, y, 0], [0.3, 0.2, 1.44], 0.8, 0.075);
    }
    line([x, 2.95, -0.6], [x, 4.35, 0.6], 0.4);
    line([x, 2.95, 0.6], [x, 4.35, -0.6], 0.4);
  }

  box([0, 0, 0], [20.4, 0.22, 1.36], 0.45, 0.11);
  for (const x of [-9.9, 9.9]) {
    box([x, -0.34, 0], [0.7, 0.65, 1.95], 0.45);
  }

  const cableHeight = (x) => {
    const distance = Math.abs(x);
    if (distance <= 4.6) return 1.05 + 3.75 * (distance / 4.6) ** 2;
    const t = (distance - 4.6) / 5.4;
    return 0.18 + 4.62 * (1 - t) ** 1.5;
  };

  for (const z of [-0.79, 0.79]) {
    for (let i = 0; i <= 650; i++) {
      const x = -10 + 20 * i / 650;
      point(x, cableHeight(x), z, 1);
      point(x, cableHeight(x) + 0.035, z, 0.7);
    }
    for (let i = 0; i <= 42; i++) {
      const x = -9.85 + 19.7 * i / 42;
      line([x, 0.14, z], [x, cableHeight(x), z], 0.65, 0.055);
    }
    line([-10.2, 0.18, z], [10.2, 0.18, z], 0.9);
    line([-10.2, -0.25, z], [10.2, -0.25, z], 0.6);
    for (let i = 0; i < 36; i++) {
      const x = -10.2 + i * 20.4 / 36;
      line([x, -0.23, z], [x + 20.4 / 72, 0.1, z], 0.5, 0.06);
      line([x + 20.4 / 72, 0.1, z], [x + 20.4 / 36, -0.23, z], 0.5, 0.06);
    }
  }

  // Water and suspended mist use separate shader regions, leaving the bridge rigid.
  for (let i = 0; i < 6800; i++) {
    const x = (random() - 0.5) * 28;
    const z = (random() - 0.5) * 17;
    const fade = Math.max(0, 1 - Math.hypot(x / 14, z / 8.5));
    point(x, -2.12, z, 0.27 * fade, 1);
  }
  for (let i = 0; i < 1000; i++) {
    const x = (random() - 0.5) * 26;
    const y = -1.9 + random() * 7.8;
    const z = (random() - 0.5) * 7;
    point(x, y, z, 0.08 + random() * 0.11, 2);
  }

  const geometry = new BufferGeometry();
  geometry.setAttribute('position', new Float32BufferAttribute(positions, 3));
  geometry.setAttribute('aOpacity', new Float32BufferAttribute(opacities, 1));
  geometry.setAttribute('aSize', new Float32BufferAttribute(sizes, 1));
  geometry.setAttribute('aRegion', new Float32BufferAttribute(regions, 1));
  geometry.setAttribute('aTone', new Float32BufferAttribute(tones, 1));
  geometry.computeBoundingSphere();
  return geometry;
}

const vertexShader = `
  uniform float uTime;
  uniform float uPixelRatio;
  attribute float aOpacity;
  attribute float aSize;
  attribute float aRegion;
  attribute float aTone;
  varying float vOpacity;
  varying float vTone;

  void main() {
    vec3 p = position;
    if (aRegion > 0.5 && aRegion < 1.5) {
      p.y += sin(p.x * 0.8 + uTime * 0.35) * cos(p.z * 0.8 + uTime * 0.2) * 0.09;
    } else if (aRegion > 1.5) {
      p.x += sin(uTime * 0.12 + p.y) * 0.17;
      p.y += cos(uTime * 0.15 + p.x) * 0.08;
    }
    vOpacity = aOpacity * (0.88 + 0.12 * sin(position.x * 2.0 + uTime * 0.45));
    vTone = aTone;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
    gl_PointSize = aSize * uPixelRatio;
  }
`;

const fragmentShader = `
  uniform vec3 uColor;
  uniform vec3 uAccent;
  varying float vOpacity;
  varying float vTone;

  void main() {
    float distanceToCenter = length(gl_PointCoord - vec2(0.5));
    float alpha = (1.0 - smoothstep(0.2, 0.5, distanceToCenter)) * vOpacity;
    if (alpha < 0.015) discard;
    gl_FragColor = vec4(mix(uColor, uAccent, vTone), alpha);
    #include <tonemapping_fragment>
    #include <colorspace_fragment>
  }
`;

export function mountBridge(host, { theme, paused, onError }) {
  const renderer = new WebGLRenderer({ alpha: true, antialias: false, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setClearColor(0x000000, 0);
  renderer.domElement.setAttribute('aria-hidden', 'true');
  const geometry = createBridgeGeometry();
  const material = new ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uPixelRatio: { value: renderer.getPixelRatio() },
      uColor: { value: new Color() },
      uAccent: { value: new Color() },
    },
    vertexShader,
    fragmentShader,
    transparent: true,
    depthWrite: false,
  });
  const scene = new Scene();
  const bridge = new Points(geometry, material);
  scene.add(bridge);
  const camera = new OrthographicCamera(-12, 12, 10, -10, 0.1, 100);
  camera.position.set(12, 7.2, 18);
  camera.lookAt(0, 0.8, 0);
  host.append(renderer.domElement);

  let frame = null;
  let lastTime = 0;
  let elapsed = 0;
  let inView = true;
  let disposed = false;
  let pointerX = 0;
  let pointerY = 0;
  bridge.rotation.y = -0.08;

  function render() {
    if (!disposed) renderer.render(scene, camera);
  }

  function tick(time) {
    if (disposed) return;
    elapsed += Math.max(0, Math.min((time - lastTime) / 1000, 0.05));
    lastTime = time;
    material.uniforms.uTime.value = elapsed;
    const targetY = -0.08 + Math.sin(elapsed * 0.14) * 0.035 + pointerX * 0.1;
    bridge.rotation.y += (targetY - bridge.rotation.y) * 0.025;
    bridge.rotation.x += (pointerY * 0.025 - bridge.rotation.x) * 0.025;
    render();
    if (!disposed) frame = window.requestAnimationFrame(tick);
  }

  function updateLoop() {
    if (frame !== null) window.cancelAnimationFrame(frame);
    frame = null;
    if (!disposed && !paused && inView && document.visibilityState === 'visible') {
      lastTime = performance.now();
      frame = window.requestAnimationFrame(tick);
    }
  }

  function resize() {
    if (disposed) return;
    const { width, height } = host.getBoundingClientRect();
    if (width === 0 || height === 0) return;
    const aspect = width / height;
    const halfHeight = Math.max(6.8, 10.8 / aspect);
    camera.left = -halfHeight * aspect;
    camera.right = halfHeight * aspect;
    camera.top = halfHeight;
    camera.bottom = -halfHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
    render();
  }

  function movePointer(event) {
    if (paused || event.pointerType !== 'mouse') return;
    const bounds = host.getBoundingClientRect();
    pointerX = (event.clientX - bounds.left) / bounds.width - 0.5;
    pointerY = (event.clientY - bounds.top) / bounds.height - 0.5;
  }

  function resetPointer() {
    pointerX = 0;
    pointerY = 0;
  }

  function setTheme(nextTheme) {
    material.uniforms.uColor.value.set(nextTheme === 'light' ? '#41483b' : '#deded4');
    material.uniforms.uAccent.value.set(nextTheme === 'light' ? '#90553f' : '#d2a28a');
    render();
  }

  function contextLost(event) {
    event.preventDefault();
    dispose();
    onError(new Error('The WebGL context was lost.'));
  }

  const resizeObserver = new ResizeObserver(resize);
  const visibilityObserver = new IntersectionObserver(([entry]) => {
    inView = entry.isIntersecting;
    updateLoop();
  });
  function dispose() {
    if (disposed) return;
    disposed = true;
    updateLoop();
    resizeObserver.disconnect();
    visibilityObserver.disconnect();
    host.removeEventListener('pointermove', movePointer);
    host.removeEventListener('pointerleave', resetPointer);
    document.removeEventListener('visibilitychange', updateLoop);
    renderer.domElement.removeEventListener('webglcontextlost', contextLost);
    geometry.dispose();
    material.dispose();
    renderer.dispose();
    renderer.domElement.remove();
  }

  renderer.domElement.addEventListener('webglcontextlost', contextLost);
  host.addEventListener('pointermove', movePointer);
  host.addEventListener('pointerleave', resetPointer);
  document.addEventListener('visibilitychange', updateLoop);
  resizeObserver.observe(host);
  visibilityObserver.observe(host);
  setTheme(theme);
  resize();
  updateLoop();

  return {
    setTheme,
    setPaused(value) {
      paused = value;
      updateLoop();
    },
    dispose,
  };
}
