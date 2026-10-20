"""

pytest-html reports
--------------------------------

Step1: Install the Plugin
    pip install pytest-html
    
Step2: Configure pytest.ini
    --html=myreport.html --self-contained-html --capture=tee-sys
    
    with date and time 
    --html="myreport_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').html" --self-contained-html --capture=tee-sys
    
[pytest]

addopts = --headed 
            --browser=chromium 
            --video=retain-on-failure  
            --screenshot=retain-on-failure
            --tracing=retain-on-failure
            --html=myreport.html --self-contained-html --capture=tee-sys
            -v
            -s



    


Step3: create sample tests


Step4: run the tests and generate reports


Step5: Attach screenshots to test failures (conftest.py) -- additional step












Allure reports
--------------------------------


step1: install allure pytest plugin.
    download allure_2.29.0-1_all.deb from https://github.com/allure-framework/allure2/releases
    sudo dpkg -i allure_2.29.0-1_all.deb
    


step2: install allure command line tool [to view and generate report].
    sudo apt install allure

step3: install allure in pytest.ini
    --alluredir=reports/allure-results
    
[pytest]

addopts = --headed 
            --browser=chromium 
            --video=retain-on-failure  
            --screenshot=retain-on-failure
            --tracing=retain-on-failure
            --html=myreport.html --self-contained-html --capture=tee-sys
            --alluredir=reports/allure-results 
            -v
            -s

step4: attach screenshots on test failure (conftest.py).

step5: create and run your tests.



step6: generate and view the allure reports.

    runtime : 
        allure serve reports/allure-results
    
    permanent report:
        allure generate reports/allure-results -o reports/allure-results --clean




"""
