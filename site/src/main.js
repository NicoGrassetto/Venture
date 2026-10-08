import './style.css';

const sceneHost = document.querySelector('[data-bridge-scene]');
const sceneError = document.querySelector('[data-scene-error]');
const copyButton = document.querySelector('[data-copy]');
const copyStatus = document.querySelector('[data-copy-status]');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
let bridge;

reducedMotion.addEventListener('change', (event) => {
  bridge?.setPaused(event.matches);
});

function showStaticBridge(error) {
  console.error('Venture: the 3D bridge is unavailable. Showing the static illustration.', error);
  bridge?.dispose();
  bridge = undefined;
  sceneHost.dataset.ready = 'false';
  sceneError.hidden = false;
}

import('./bridge.js')
  .then(({ mountBridge }) => {
    bridge = mountBridge(sceneHost, { paused: reducedMotion.matches, onError: showStaticBridge });
    sceneHost.dataset.ready = 'true';
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
