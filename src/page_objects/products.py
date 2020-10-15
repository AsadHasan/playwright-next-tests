"""Products Page-object"""
from __future__ import annotations
from playwright.sync_api import Page


class Products:
    """Products page"""

    def __init__(self, page: Page):
        self.page = page

    def filter_by_new_in(self) -> Products:
        """Filter products by New

        Returns:
            Products: Products page
        """
        self.page.check("[data-optionvalue='newin'] > div > div > label")
        self.page.waitForNavigation()
        return self

    def filter_by_in_stock(self) -> Products:
        """Filter products by "In Stock"

        Returns:
            Products: Products page
        """
        selector = "[data-optionvalue='available']>div>div.FeatLabel>label"
        self.page.check(selector)
        self.page.waitForNavigation()
        return self

    def get_products_heading(self) -> str:
        """Get products page's heading

        Returns:
            str: [Products page's heading
        """
        return self.page.innerText("#ResultHeader > div.SearchedFor > h1")
