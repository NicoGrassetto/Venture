import './style.css';

const themeButton = document.querySelector('[data-theme-toggle]');
const motionButton = document.querySelector('[data-motion-toggle]');
const sceneHost = document.querySelector('[data-bridge-scene]');
const sceneStatus = document.querySelector('[data-scene-status]');
const copyButton = document.querySelector('[data-copy]');
const copyStatus = document.querySelector('[data-copy-status]');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let theme = 'dark';
let paused = reducedMotion.matches;
let bridge;

themeButton.hidden = false;
themeButton.addEventListener('click', () => {
  theme = theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = theme;
  document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#171716' : '#f2f1ec';
  themeButton.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} theme`);
  bridge?.setTheme(theme);
});

function updateMotion() {
  motionButton.dataset.paused = String(paused);
  motionButton.setAttribute('aria-label', `${paused ? 'Play' : 'Pause'} bridge animation`);
  motionButton.querySelector('span').textContent = `${paused ? 'Play' : 'Pause'} motion`;
  if (bridge) {
    sceneStatus.textContent = paused ? 'Still point-cloud study' : 'Live point-cloud study';
    bridge.setPaused(paused);
  }
}

motionButton.addEventListener('click', () => {
  paused = !paused;
  updateMotion();
});
reducedMotion.addEventListener('change', (event) => {
  paused = event.matches;
  updateMotion();
});

function showStaticBridge(error) {
  console.error('Venture: the 3D bridge is unavailable. Showing the static illustration.', error);
  bridge?.dispose();
  bridge = undefined;
  sceneHost.dataset.ready = 'false';
  sceneStatus.textContent = 'Static view / 3D unavailable';
  motionButton.hidden = true;
}

import('./bridge.js')
  .then(({ mountBridge }) => {
    bridge = mountBridge(sceneHost, { theme, paused, onError: showStaticBridge });
    sceneHost.dataset.ready = 'true';
    motionButton.hidden = false;
    updateMotion();
  })
  .catch(showStaticBridge);

copyButton.hidden = false;
copyButton.addEventListener('click', async () => {
  const commands = document.querySelector('#clone-commands').textContent;
  try {
    if (!navigator.clipboard) {
      throw new Error('Clipboard access is unavailable in this browser or context.');
    }
    await navigator.clipboard.writeText(commands);
    copyButton.querySelector('span').textContent = 'Copied';
    copyStatus.textContent = 'Commands copied. Paste them into your terminal.';
  } catch (error) {
    console.warn('Venture: could not copy the clone commands.', error);
    copyButton.querySelector('span').textContent = 'Try again';
    copyStatus.textContent = 'Could not copy. Select the commands above and copy them manually.';
  }
});

window.addEventListener('pagehide', (event) => {
  if (!event.persisted) bridge?.dispose();
});
