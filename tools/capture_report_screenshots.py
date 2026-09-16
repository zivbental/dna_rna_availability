"""Capture the real self-contained HTML report for presentation slides."""

from pathlib import Path
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
report = root / "runs/20260913-175402/report.html"
assets = root / ".presentation_assets"
assets.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1500, "height": 1050}, device_scale_factor=1)
    page.goto(report.as_uri(), wait_until="load")
    page.screenshot(path=str(assets / "report_overview.png"), full_page=False)

    page.locator("#ranked-candidates").scroll_into_view_if_needed()
    page.screenshot(path=str(assets / "report_ranked.png"), full_page=False)

    page.locator("#candidate-1814-1833").scroll_into_view_if_needed()
    page.screenshot(path=str(assets / "report_candidate.png"), full_page=False)
    browser.close()

print(assets)
