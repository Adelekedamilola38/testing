import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()


    if "page" in item.fixturenames and rep.failed:
        page = item.funcargs["page"]
        page.screenshot(path=f"screenshots/{item.name}.png")