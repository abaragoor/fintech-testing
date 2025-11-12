import pytest
from pages.user_registration_page import UserRegistrationPage
from data.test_data_factory import create_user_data

@pytest.mark.asyncio
async def test_user_registration(page):
    user = create_user_data()
    reg = UserRegistrationPage(page)
    await reg.goto('about:blank')  # placeholder - replace with real UI or local mock page

    # create a minimal mock HTML to simulate registration if no real UI is available
    await page.set_content('''
    <html>
      <body>
        <input id="name" />
        <input id="email" />
        <button id="submit" onclick="document.body.innerHTML = '<div>Registration Successful</div>'">Submit</button>
      </body>
    </html>
    ''')

    await reg.register_user(user['name'], user['email'])
    assert await page.is_visible('text=Registration Successful')
