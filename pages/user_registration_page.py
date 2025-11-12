from pages.base_page import BasePage

class UserRegistrationPage(BasePage):
    async def register_user(self, name, email):
        # selectors assume a simple mock page with inputs #name, #email and #submit
        await self.page.fill('#name', name)
        await self.page.fill('#email', email)
        await self.page.click('#submit')
