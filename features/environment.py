import os
import sys
import time
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# ensure project root is on path so features can import modules
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from config.config import load_config


RESULTS_DIR = PROJECT_ROOT / "results"
SCREENSHOTS_DIR = RESULTS_DIR / "screenshots"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


def before_all(context):
    cfg = load_config()
    headless = os.getenv("HEADLESS", str(cfg.get("headless", False))).lower() == "true"
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1400,1000")

    service = ChromeService(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(cfg.get("implicit_wait", 5))
    context.base_url = cfg.get("base_url")


def after_all(context):
    try:
        context.driver.quit()
    except Exception:
        pass


def after_scenario(context, scenario):
    try:
        if scenario.status == "failed":
            ts = time.strftime("%Y%m%d-%H%M%S")
            name = "{}_{}.png".format("_".join(scenario.name.split()), ts)
            path = SCREENSHOTS_DIR / name
            context.driver.save_screenshot(str(path))
            try:
                src_path = SCREENSHOTS_DIR / (name + ".html")
                with open(src_path, "w", encoding="utf-8") as f:
                    f.write(context.driver.page_source)
            except Exception:
                pass
    except Exception:
        pass
