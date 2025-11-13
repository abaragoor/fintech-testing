# pages/transaction_page.py
from pages.base_page import BasePage

class TransactionPage(BasePage):
    """
    Page Object Model for the Transaction Creation Page.
    Simulates entering userId, recipientId, and amount to create a transaction.
    """

    def __init__(self, page):
        super().__init__(page)
        # Selectors
        self.user_id_input = "#userId"
        self.amount_input = "#amount"
        self.recipient_id_input = "#recipientId"
        self.submit_button = "#submit"
        self.success_message = "text=Transaction Created"

    async def create_transaction(self, user_id: str, recipient_id: str, amount: float):
        """Fills in the form and submits the transaction."""
        await self.page.fill(self.user_id_input, user_id)
        await self.page.fill(self.recipient_id_input, recipient_id)
        await self.page.fill(self.amount_input, str(amount))
        await self.page.click(self.submit_button)

    async def verify_success_message(self):
        """Verifies that the transaction success message is visible."""
        return await self.page.is_visible(self.success_message)
