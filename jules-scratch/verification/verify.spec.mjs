import { test, expect } from '@playwright/test';

test('modal test', async ({ page }) => {
  await page.goto('http://localhost:3000');
  await page.click('button:has-text("Order Service")');
  await page.waitForSelector('.modal-overlay.is-open');
  const modal = await page.$('.modal');
  await modal.screenshot({ path: 'jules-scratch/verification/screenshot.png' });
});
