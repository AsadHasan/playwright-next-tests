"""Helper functions to search and filter results"""
from typing import NamedTuple, Type
from playwright.sync_api import Page
from page_objects.homepage import Homepage
from page_objects.products import Products

Results: Type[Results] = NamedTuple("Results", page=Products, total=int)
FilteredResults: Type[FilteredResults] = NamedTuple(
    "FilteredResults", page=Products, total_filtered_results=int, heading=str
)


def search_and_get_results(page: Page, category: str, sub_category: str) -> Results:
    """Search from homepage and get results on next page

    Args:
        page (Page): Browser tab
        category (str): Category of options
        sub_category (str): Sub category of items

    Returns:
        Results: Tuple of Products page and results count
    """
    homepage: Homepage = Homepage(page)
    products_page: Products = (
        homepage.open().select_category(category).select_sub_category(sub_category)
    )
    return Results(products_page, products_page.get_number_of_results())


def get_results_filtered_by_new_and_in_stock(
    products_page: Products,
) -> FilteredResults:
    """Get reulsts filtered by "new" and "in stock" items

    Args:
        products_page (Products): Products tab

    Returns:
        FilteredResults: Tuple of Products page, total filtered results
        and resulting heading
    """
    products_page.filter_by_new_in().filter_by_in_stock()
    number_filtered_results: int = products_page.get_number_of_results()
    heading: str = products_page.get_products_heading()
    return FilteredResults(products_page, number_filtered_results, heading)
