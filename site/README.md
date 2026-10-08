# Venture landing page

A working design proposal for Venture, inspired by the charcoal split-screen,
monospace details, and particle artwork in the
[devl.dev reference](https://www.devl.dev/c/auth/check-email). The layout,
copy, illustrations, and Three.js bridge geometry are original; no reference
site code or artwork is included.

## Design

- An asymmetric split screen: a Golden Gate Bridge point cloud on the left,
  the message "Your bridge from idea to reality" on the right.
- A dark-only charcoal/ivory palette with a text-only Venture wordmark and
  an uncluttered bridge scene: no study labels, coordinates, badges, or
  theme/motion controls.
- The bridge uses International Orange (`#f04a00`), an sRGB approximation of
  the bridge district's published CMYK 0/69/100/6
  [paint specification](https://www.goldengate.org/bridge/history-research/bridge-features/color-art-deco-styling/).
  The static illustration and favicon use the same color; water and mist stay
  neutral. On-screen colors approximate paint and vary with displays and lighting.
- Slow movement, rippling particle water, and gentle mouse parallax rather than
  a freely rotating model. The two towers and suspension cables stay readable.
- A primary quick-start link, a GitHub link, three harness principles, and
  copyable clone commands. No accounts, fictional testimonials, or signup form.
- On small screens the message comes first, followed by the bridge and details.

This is a static website, not a hosted version of the harness. Its optional
Node.js dependencies are isolated here; using the Python harness does not
require Node.js, npm, or Three.js.

## Local preview

Use Node.js 24 LTS (minimum 22.12), then run from the repository root:

```bash
npm --prefix site ci
npm --prefix site run dev
```

Open the local URL printed by Vite. To test and preview the production output:

```bash
npm --prefix site test
npm --prefix site run build
npm --prefix site run preview
```

The build contains local CSS, JavaScript, Three.js, and SVG assets. There are
no runtime CDNs, external fonts, analytics, or backend services.
Vite also emits `third-party-licenses.txt` with the bundled dependency notices.

## Enable GitHub Pages

The [deployment workflow](../.github/workflows/deploy-pages.yml) is ready.
Publishing is deliberately left to the repository owner:

1. Commit and push the landing-page changes (including the npm lockfile and
   workflow) to the repository's `main` branch.
2. Open the repository's **Settings > Pages > Build and deployment**.
3. Set **Source** to **GitHub Actions**. Do not select "Deploy from a branch";
   this site needs the included Vite build.
4. Open **Actions > Deploy landing page > Run workflow**, choose `main`, and
   run it. If a push already started a run before Pages was enabled, rerun it.
5. When the deployment is green, open:
   <https://nicograssetto.github.io/Venture/>

These instructions use the current GitHub repository name,
`NicoGrassetto/Venture`. The older `entrepreneurship-skills` repository URL
redirects to it; GitHub Pages project URLs use the current repository name.

Future pushes that change this site or its workflow rebuild and deploy
automatically. Pull requests build and test only; they do not publish.
Actions must be enabled, and any protection rules on the `github-pages`
environment must allow `main` (and may require approval).

Only the generated `site/dist/` directory is uploaded, never the repository
root or private venture workspaces. Relative asset URLs support GitHub's
`/Venture/` project path as well as a custom domain.

For a custom domain, set **Settings > Pages > Custom domain**, configure your
domain's DNS using [GitHub's instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site),
verify ownership, and enable **Enforce HTTPS** when available. No custom
domain is required for the default URL above.

## Accessibility and verification

The page uses semantic HTML, keyboard focus indicators, a skip link, live
copy/error status, and a scrollable, keyboard-focusable command block.
The message and primary actions precede the decorative scene in reading and
keyboard order, including on mobile.
The animation respects system reduced-motion preferences without on-page
controls. Rendering also stops while the scene is offscreen or the tab is
hidden. The device pixel ratio is capped to bound GPU work.

An original static SVG stays visible without JavaScript, if Three.js cannot
load, if WebGL cannot start, or after WebGL context loss. The rest of the
page remains usable. A scene error notice appears only if the animation fails,
and logs retain the cause; clipboard failures provide manual-copy instructions.

`npm test` checks geometry bounds, finite/matching attributes, both towers,
the central deck, separate water/mist regions, deterministic generation,
consistent International Orange assets, and the absence of removed hero UI.
For visual checks, preview the production build at desktop and narrow mobile
widths; verify dark-only rendering under both system color preferences,
automatic reduced motion, copy, and unavailable WebGL. The harness's existing
Python test suite remains separate.
