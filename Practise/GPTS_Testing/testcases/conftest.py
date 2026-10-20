"""
if this setup function iscan be utilized by a function then
@pytest.fixture(scope='function')

or if this function can be utilized by whole class
@pytest.fixture(scope='class')


"""
import os
import pytest
from selenium import webdriver




@pytest.fixture(scope='function')
def setup(request,browser,url):
    global driver
    if browser == "chrome":
        print("Launching Chrome Browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Launching FireFox Browser")
        driver = webdriver.Firefox()
    else:
        print("Provide Valid Browser")

    driver.get("https://www.yatra.com/")
    # driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

    


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
    # parser.addoption("--platform")


@pytest.fixture(scope="session",autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session",autouse=True)
def url(request):
    return request.config.getoption("--url")

# pytest -vs --browser firefox


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.yatra.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # report_directory = "../screenshots"
            print("Report Directory : ",report_directory)
            # file_name = str(int(round(time.time()*1000))) + ".png"
            file_name = report.nodeid.replace("::","_") + ".png"
            print("File Name : ",file_name)
            destinationFile = os.path.join(report_directory,file_name)
            print("Destination File : ",destinationFile)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height:200px;"'\
                'onclick="window.open(this.src)" align="right"/></div>'% file_name
            extras.append(pytest_html.extras.html(html))
        report.extras = extras

def pytest_html_report_title(report):
    report.title = "Selenium Automation Python Tutorial report"
