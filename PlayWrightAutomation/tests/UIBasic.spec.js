const { test, expect } = require("@playwright/test");

test("First Playwright test", async ({ browser }) => {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto("https://codingforkids.ro/login");
    console.log(await page.title());
    await expect(page).toHaveTitle("Login | Coding for Kids")
    await page.locator('#login-email').type("naicadnirolf.uded@gmail.com");
    await page.locator('#login-password').type("parola");
    await page.locator('button:text("Login")');
    await page.locator('button:text("Login")').click();
});