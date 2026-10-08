import assert from 'node:assert/strict';
import { test } from 'node:test';
import { createBridgeGeometry } from '../src/bridge.js';

test('the particle sculpture has bounded, finite geometry and matching attributes', () => {
  const geometry = createBridgeGeometry();
  const positions = geometry.getAttribute('position');
  assert.ok(positions.count > 15000 && positions.count < 45000, `Unexpected particle count: ${positions.count}`);
  for (const [name, attribute] of Object.entries(geometry.attributes)) {
    assert.equal(attribute.count, positions.count, `${name} must describe every point`);
    assert.ok(attribute.array.every(Number.isFinite), `${name} must be finite`);
  }
  geometry.computeBoundingBox();
  assert.ok(geometry.boundingBox.min.x >= -14 && geometry.boundingBox.max.x <= 14);
  assert.ok(geometry.boundingBox.min.y >= -2.2 && geometry.boundingBox.max.y <= 6);
  assert.ok(geometry.boundingSphere.radius < 18);
  geometry.dispose();
});

test('both suspension towers rise above the continuous bridge deck', () => {
  const geometry = createBridgeGeometry();
  const positions = geometry.getAttribute('position');
  const regions = geometry.getAttribute('aRegion');
  let leftTower = 0;
  let rightTower = 0;
  let centerDeck = 0;
  for (let i = 0; i < positions.count; i++) {
    if (regions.getX(i) !== 0) continue;
    const x = positions.getX(i);
    const y = positions.getY(i);
    if (Math.abs(x + 4.6) < 0.2 && y > 4.6) leftTower++;
    if (Math.abs(x - 4.6) < 0.2 && y > 4.6) rightTower++;
    if (Math.abs(x) < 0.5 && Math.abs(y) < 0.3) centerDeck++;
  }
  assert.ok(leftTower > 100 && rightTower > 100, 'Both Golden Gate towers must be present');
  assert.ok(centerDeck > 100, 'The deck must connect through the center span');
  geometry.dispose();
});

test('water and mist are distinct from the rigid architectural points', () => {
  const geometry = createBridgeGeometry();
  const regions = Array.from(geometry.getAttribute('aRegion').array);
  assert.equal(regions.filter((region) => region === 1).length, 6800);
  assert.equal(regions.filter((region) => region === 2).length, 1000);
  assert.ok(regions.every((region) => [0, 1, 2].includes(region)));
  const opacities = geometry.getAttribute('aOpacity').array;
  assert.ok(opacities.every((opacity) => opacity >= 0 && opacity <= 1));
  geometry.dispose();
});

test('geometry is deterministic across reloads', () => {
  const first = createBridgeGeometry();
  const second = createBridgeGeometry();
  for (const name of Object.keys(first.attributes)) {
    assert.deepEqual(first.getAttribute(name).array, second.getAttribute(name).array);
  }
  first.dispose();
  second.dispose();
});
