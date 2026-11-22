import assert from 'node:assert/strict';
import { chromium, expect } from '@playwright/test';
const origin = 'http://127.0.0.1:4327';
const browser = await chromium.launch({
  executablePath: process.env.CONTROL_CHROMIUM,
  args: ['--disable-background-networking', '--renderer-process-limit=1'],
});
try {
  const page = await browser.newPage({ serviceWorkers: 'block' });
  const requests = [];
  const sockets = [];
  await page.route('**/*', (route) => {
    const request = route.request();
    const url = new URL(request.url());
    const allowed = url.origin === origin &&
      request.method() === 'GET' && !url.search && !request.postData();
    requests.push({ allowed, path: url.pathname });
    return allowed ? route.continue() : route.abort();
  });
  await page.routeWebSocket('**/*', (route) => {
    sockets.push(route.url());
    return route.close();
  });
  await page.goto(origin, { timeout: 10_000 });
  await page.waitForFunction(
    () => !document.querySelector('astro-island')?.hasAttribute('ssr'),
    null, { timeout: 10_000 },
  );
  assert.equal(requests.filter(({ path }) => path.endsWith('.wasm')).length, 0);
  await page.setInputFiles('input[type=file]', '../control.pdf');
  await expect(page.getByText('No hidden content found')).toBeVisible({ timeout: 15_000 });
  const wasm = requests.filter(({ path }) => path.endsWith('.wasm')).length;
  assert.ok(wasm > 0);
  assert.ok(requests.every(({ allowed }) => allowed));
  assert.equal(sockets.length, 0);
  console.log(JSON.stringify({ requests: requests.length, wasm, disallowed: 0, websockets: 0 }));
} finally {
  await browser.close();
}
