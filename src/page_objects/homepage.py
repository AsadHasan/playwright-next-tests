"""Homepage Page-object"""
from __future__ import annotations
from playwright.sync_api import Page

from config import BASE_URL
from page_objects.products import Products


class Homepage:
    """Next's homepage"""

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> Homepage:
        """Open Next's homepage

        Returns:
            Homepage: Homepage tab
        """
        self.page.goto(BASE_URL)
        return self

    def select_category(self, category: str) -> Homepage:
        """Hover over a category on main menu,
        to see sub-categories.

        Args:
            category (str): Category on main menu

        Returns:
            Homepage: Homepage tab
        """
        self.page.hover(f"'{category}'")
        return self

    def select_sub_category(self, sub_category: str) -> Products:
        """Select a sub-category

        Args:
            sub_category (str): Sub category available in Category from
            main menu

        Returns:
            Products: Products page
        """
        self.page.click(f"'{sub_category}'")
        return Products(self.page)
