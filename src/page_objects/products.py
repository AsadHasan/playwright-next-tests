"""Products Page-object"""
from __future__ import annotations
from typing import List
from playwright.sync_api import ElementHandle, Page


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
            str: Products page's heading
        """
        return self.page.innerText("#ResultHeader > div.SearchedFor > h1")

    def get_number_of_results(self) -> int:
        """Get total number of results

        Returns:
            int: Total number of results
        """
        number_of_results_text = self.page.innerText("#total-results-count")
        return [
            int(character)
            for character in number_of_results_text.split()
            if character.isdigit()
        ][0]

    def all_results_thumbnail_images_have_newin_banner(self) -> bool:
        """Do all result images have "New In" banner?

        Returns:
            bool: Whether all result images have "New In" banner
        """
        selector: str = ".Page .Images"
        images: List[ElementHandle] = self.page.querySelectorAll(selector)
        return all(img.querySelector(".NewIn") is not None for img in images)
