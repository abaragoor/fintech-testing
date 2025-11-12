import pytest
from pages.user_registration_page import UserRegistrationPage
from data.test_data_factory import create_transaction_data

@pytest.mark.asyncio
async def test_create_transaction_ui(page):
    # A very simple flow creating a transaction in a mock page
    await page.set_content('''
    <html>
      <body>
        <input id="userId" />
        <input id="amount" />
        <input id="recipientId" />
        <button id="submit" onclick="document.body.innerHTML = '<div>Transaction Created</div>'">Create</button>
      </body>
    </html>
    ''')
    await page.fill('#userId', '123')
    await page.fill('#amount', '100.50')
    await page.fill('#recipientId', '456')
    await page.click('#submit')
    assert await page.is_visible('text=Transaction Created')
