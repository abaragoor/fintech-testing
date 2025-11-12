class BasePage:
    def __init__(self, page):
        self.page = page

    async def goto(self, url):
        await self.page.goto(url)

    async def screenshot_on_fail(self, name):
        await self.page.screenshot(path=name)
