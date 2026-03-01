import asyncio
import sys
from datetime import datetime

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

# Defaults (tweak as needed)
HEADLESS = True
MAX_SCROLL_ROUNDS = 25
PAUSE_MS = 800
STABLE_ROUNDS_TO_STOP = 3


def log(msg: str) -> None:
    now = datetime.now().astimezone()
    ts = now.strftime("%Y-%m-%d %H:%M:%S.") + f"{now.microsecond // 1000:03d}" + now.strftime("%z")
    ts = ts[:-2] + ":" + ts[-2:]
    print(f"[{ts}] {msg}", flush=True)


async def scroll_to_load_all(page):
    last_height = 0
    stable = 0

    for i in range(1, MAX_SCROLL_ROUNDS + 1):
        height = await page.evaluate("() => document.body.scrollHeight")
        if height == last_height:
            stable += 1
        else:
            stable = 0
            last_height = height

        log(f"scroll {i}/{MAX_SCROLL_ROUNDS} height={height} stable={stable}")
        if stable >= STABLE_ROUNDS_TO_STOP:
            break

        await page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(PAUSE_MS)

        try:
            await page.wait_for_load_state("networkidle", timeout=5000)
        except PlaywrightTimeoutError:
            pass


async def run(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=HEADLESS)
        page = await browser.new_page()

        log(f"goto {url}")
        await page.goto(url, wait_until="domcontentloaded")

        try:
            await page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass

        await scroll_to_load_all(page)

        log("dumping html")
        html = await page.content()  # rendered DOM HTML snapshot
        await browser.close()

        log(f"done chars={len(html)}")
        print(html)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <url>", file=sys.stderr)
        sys.exit(2)
    asyncio.run(run(sys.argv[1]))


if __name__ == "__main__":
    main()
