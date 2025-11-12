def tearDown(self):
        if hasattr(self, '_outcome') and self._outcome.errors:
            # Take screenshot on failure
            try:
                screenshot_path = f"test_output/failure_{self.id()}.png"
                self.page.screenshot(path=screenshot_path)
                logging.info(f"Screenshot saved to {screenshot_path}")
            except Exception as e:
                logging.error(f"Failed to take screenshot: {e}")

        # Stop tracing and save
        trace_path = f"test_output/{self.id()}.zip"
        self.context.tracing.stop(path=trace_path)
        if self.page:
             self.page.close()
        if self.context:
            self.context.close()
        super().tearDown()