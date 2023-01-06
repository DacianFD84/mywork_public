const { test } = require("@playwright/test");

test("First Playwright test", async ({ browser }) => {
    const context = await browser.newContext();
    const page = await context.newPage;
    await page.goto("https://codingforkids.ro/login")


});

test("Second Playwright test", async ({ page }) => {
    //const context = await browser.newContext();
    //const page = await context.newPage;

    await page.goto("https://codingforkids.ro/login")


});