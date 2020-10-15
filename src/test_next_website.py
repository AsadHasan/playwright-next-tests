"""Tests for Next's website."""
from playwright.sync_api import Page

from page_objects.homepage import Homepage


def test_search_and_filter_mens_shoes(page: Page) -> None:
    """Failure of this test implies that Men's shoes cannot
    be searched and then filtered by "New" and "In stock"
    filters

    Args:
        page (Page): Browser page/tab
    """
    heading: str = (
        Homepage(page)
        .open()
        .select_category("MEN")
        .select_sub_category("Shoes")
        .filter_by_new_in()
        .filter_by_in_stock()
        .get_products_heading()
    )
    assert "New In" in heading
    assert "In Stock" in heading
