from playwright.sync_api import Playwright
import pytest
import os

pytestmark = pytest.mark.skipif(os.getenv("CI") == "true", reason="API blocked on CI")

#@pytest.mark.skipif(os.getenv("CI") == "true", reason="API blocked on CI")
def test_get_product(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://www.automationexercise.com")
    response=api.get("/api/productsList")
    assert response.status == 200
    body = response.json()
    print(body)

#@pytest.mark.skipif(os.getenv("CI") == "true", reason="API blocked on CI")
def test_get_brands(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://www.automationexercise.com")
    response=api.get("/api/brandsList")
    assert response.status == 200
    body = response.json()
    print(body)

#@pytest.mark.skipif(os.getenv("CI") == "true", reason="API blocked on CI")
def test_search_product(playwright: Playwright):
    api = playwright.request.new_context(base_url="https://www.automationexercise.com")
    response = api.post("/api/searchProduct", form={"search_product": "top"})
    assert response.status == 200
    body = response.json()
    print(body)


