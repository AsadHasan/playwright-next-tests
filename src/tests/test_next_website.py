"""Tests for Next's website."""
from playwright.sync_api import Page
from utils import get_results_filtered_by_new_and_in_stock, search_and_get_results


def test_search_and_filter_mens_shoes(page: Page) -> None:
    """Failure of this test implies that Men's shoes cannot
    be searched and then correctly filtered by "New" and
    "In stock" filters.

    Args:
        page (Page): Browser page/tab
    """
    products_page, total_results = search_and_get_results(page, "MEN", "Shoes")
    (
        products_page,
        number_filtered_results,
        heading,
    ) = get_results_filtered_by_new_and_in_stock(products_page)

    # Check heading shows filtering
    assert "New In" in heading
    assert "In Stock" in heading

    # Check results count correctly changed after filtering
    # and that all result images show "New In" filter banner
    assert number_filtered_results <= total_results
    if number_filtered_results > 0:
        assert products_page.all_results_thumbnail_images_have_newin_banner()
