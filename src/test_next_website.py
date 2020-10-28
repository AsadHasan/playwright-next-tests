"""Tests for Next's website."""
from playwright.sync_api import Page

from page_objects.homepage import Homepage
from page_objects.products import Products


def test_search_and_filter_mens_shoes(page: Page) -> None:
    """Failure of this test implies that Men's shoes cannot
    be searched and then correctly filtered by "New" and
    "In stock" filters.

    Args:
        page (Page): Browser page/tab
    """
    # Search for Men's shoes
    homepage: Homepage = Homepage(page)
    products_page: Products = (
        homepage.open().select_category("MEN").select_sub_category("Shoes")
    )
    number_of_unfiltered_results: int = products_page.get_number_of_results()

    # Filter by "New In" and "In Stock"
    products_page.filter_by_new_in().filter_by_in_stock()
    number_filtered_results = products_page.get_number_of_results()
    heading: str = products_page.get_products_heading()

    # Check heading shows filtering
    assert "New In" in heading
    assert "In Stock" in heading

    # Check results count correctly changed after filtering
    # and that all result images show "New In" filter banner
    assert number_filtered_results <= number_of_unfiltered_results
    if number_filtered_results > 0:
        assert products_page.all_results_thumbnail_images_have_newin_banner()
