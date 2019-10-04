[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![Documentation Status](https://readthedocs.org/projects/practice-rest-api-automation-with-python-3/badge/?version=latest)](https://practice-rest-api-automation-with-python-3.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0a3c971aa10e4e93b15944480cbf9b15)](https://www.codacy.com/manual/ikostan/REST_API_AUTOMATION?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ikostan/REST_API_AUTOMATION&amp;utm_campaign=Badge_Grade)
[![Job Status](https://inspecode.rocro.com/badges/github.com/ikostan/REST_API_AUTOMATION/status?token=7Zs_YsesnPupoK5eFy0uLj0wOxa-2Om5_GYUKnSpvJA&branch=master)](https://inspecode.rocro.com/jobs/github.com/ikostan/REST_API_AUTOMATION/latest?completed=true&branch=master)
[![Report](https://inspecode.rocro.com/badges/github.com/ikostan/REST_API_AUTOMATION/report?token=7Zs_YsesnPupoK5eFy0uLj0wOxa-2Om5_GYUKnSpvJA&branch=master)](https://inspecode.rocro.com/reports/github.com/ikostan/REST_API_AUTOMATION/branch/master/summary)
[![CircleCI](https://circleci.com/gh/ikostan/REST_API_AUTOMATION.svg?style=svg)](https://circleci.com/gh/ikostan/REST_API_AUTOMATION)
[![Build Status](https://travis-ci.org/ikostan/REST_API_AUTOMATION.svg?branch=master)](https://travis-ci.org/ikostan/REST_API_AUTOMATION)
[![codecov](https://codecov.io/gh/ikostan/REST_API_AUTOMATION/branch/master/graph/badge.svg)](https://codecov.io/gh/ikostan/REST_API_AUTOMATION)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6eefab86052a2d4be5ba/test_coverage)](https://codeclimate.com/github/ikostan/REST_API_AUTOMATION/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/6eefab86052a2d4be5ba/maintainability)](https://codeclimate.com/github/ikostan/REST_API_AUTOMATION/maintainability)

# Practice REST API test automation with Python 3

<div align="center"> 
<img width="9%" height="9%" src="https://github.com/ikostan/REST_API_AUTOMATION/blob/master/files/python-icon-18.jpg" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/REST_API_AUTOMATION/blob/master/files/rest-api-icon-8.jpg" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/REST_API_AUTOMATION/blob/master/files/iconfinder_api-code-window_532742.png" hspace="20">
<img width="9%" height="9%" src="https://github.com/ikostan/REST_API_AUTOMATION/blob/master/files/build-devops-automation-recycle_code-refresh_settings-preferences-512.png" hspace="20">
</div>

## Project Description

An API, or Application Program Interface, enables developers to integrate one app with another. To use an API, you make a request to a remote web server, and retrieve the data you need. Test Automation for APIs is needed to eliminate any possible errors, detect defects early, and ensure quality through the application development cycle. In this project, we’ll take a look at the automating API tests using Python.

### Table of Contents:<br/>

1. <a href="#main_objectives">Main Objectives</a>
2. <a href="#official_documentation_sources">Official Documentation Sources</a>
3. <a href="#additional_tech_info_resources">Additional Tech Info Resources</a>
4. <a href="#dev_env">Dev Environment</a>
5. <a href="#tools">Nice to have tools</a>
6. <a href="#about">About REST API app</a>
7. <a href="#setup">REST API app setup</a>
8. <a href="#endpoints">API endpoints and examples</a>
9. <a href="#guidelines">General guidelines: How to set up dev environment</a>
10. <a href="#tech_issues">Tech Issues and Problem Solving</a>

### Main Objectives:<br/>
<a id="main_objectives"></a>

- Creating REST API Automation
- Cover following well known HTTP methods are commonly used in REST: GET, PUT, DELETE, POST.
- Build fast and readable automation using minimal code
- Industry-ready test structure
- Build readable test report using Allure Framework
- Test code should avoid violating principles like [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle) and [KISS](https://en.wikipedia.org/wiki/KISS_principle)
- Using cloud automation platforms: [Codacy](https://www.codacy.com/), [CirclerCI](https://circleci.com), [TravisCI](https://travis-ci.org), [INSPECODE](https://inspecode.rocro.com), [Codecov](https://codecov.io)

### Official Documentation Sources<br/>
<a id="official_documentation_sources"></a>

- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [Allure Test Report](http://allure.qatools.ru/)
- [cars-api](https://github.com/qxf2/cars-api)
- [Practice API automation](http://35.167.62.251/)
- [Flask](https://www.fullstackpython.com/flask.html)
- [Practice REST API automation with Python 3’s documentation](https://practice-rest-api-automation-with-python-3.readthedocs.io/en/latest/?badge=latest)
- [Testing Flask Applications](https://flask.palletsprojects.com/en/1.0.x/testing/)

### Additional Tech Info Resources<br/>
<a id="additional_tech_info_resources"></a>

- [REST API Tutorial](https://restfulapi.net)
- [Full Pytest documentation](http://doc.pytest.org/en/latest/contents.html)
- [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)
- [Allure Framework](https://docs.qameta.io/allure/)
- [Automated REST API Testing with Python](https://dev.to/dowenb/automated-rest-api-testing-with-python-2jm5)
- [Writing Unit Tests for REST API in Python](https://hackernoon.com/writing-unit-tests-for-rest-api-in-python-web-application-2e675a601a53)
- [Guide-to automating API tests using Python](https://www.grossum.com/blog/beginner-s-guide-to-automating-api-tests-using-python)
- [Testing Flask application with basic authentication](https://gist.github.com/jarus/1160696)

### Dev Environment:<br/>
<a id="dev_env"></a>

- [Python 3.7.4](https://www.python.org/downloads/release/python-374/)
- [PyTest 5.1.1](https://pypi.org/project/pytest/)
- [Win 10 (64 bit)](https://www.microsoft.com/en-ca/software-download/windows10)
- [PyCharm 2019.2 (Community Edition)](https://www.jetbrains.com/pycharm/download/#section=windows)
- [GitHub Desktop 2.1.2](https://desktop.github.com/)
- [GIT 2.22.0.windows.1](https://git-scm.com/download/win)

### Python Packages
Full list of dependencies see [here.](https://github.com/ikostan/REST_API_AUTOMATION/blob/master/requirements.txt)

### Nice to have tools
<a id="tools"></a>

1. [Fiddler: The free web debugging proxy](https://www.telerik.com/fiddler)
2. [Kite: Code Faster in Python](https://kite.com/)

### General guidelines: How to set up dev environment.<br/>
<a id="guidelines"></a>

1. Install Python
2. Install PyCharm
3. Configure Python virtual environment and activate it
4. Install Python prerequisites/packages
5. Setup REST API app

**NOTE:** for more detailed info please see "Tech Issues and Problem Solving" section<br/>

### About REST API app
<a id="about"></a>
This REST application written in Python was built to help testers learn to write API automation. The application has endpoints for you to practice automating GET, POST, PUT and DELETE methods. We have also included permissioning and authentication too. This web application was developed by [Qxf2 Services](https://www.qxf2.com/?utm_source=carsapi&utm_medium=click&utm_campaign=From%20carspai).

### REST API app setup
<a id="setup"></a>

1. In your terminal prompt, pip install flask
2. Copy the contents of [this file](https://github.com/qxf2/cars-api/blob/master/cars_app.py) and save it (anywhere) as cars_app.py
3. In your terminal prompt, cd directory_that_has_cars_app_py
4. In your terminal prompt, python cars_app.py

If everything goes right, you should see an output similar to the following:
```bash
* Serving Flask app "cars_app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat
* Debugger is active!
* Debugger PIN: 105-519-712
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### API endpoints and examples
<a id="endpoints"></a>

- For more details please [click here](https://practice-rest-api-automation-with-python-3.readthedocs.io/en/latest/cars_app.html)

### Tech Issues and Problem Solving:<br/>
<a id="tech_issues"></a>

<details>
  <summary><b>Changing the project interpreter in the PyCharm project settings</b></summary>

1. In the **Settings/Preferences dialog** (Ctrl+Alt+S), select **Project <project name> | Project Interpreter**.
2. Expand the list of the available interpreters and click the **Show All** link.
3. Select the target interpreter. When PyCharm stops supporting any of the outdated Python versions, the corresponding project interpreter is marked as unsupported.
4. The Python interpreter name specified in the **Name** field, becomes visible in the list of available interpreters. Click **OK** to apply the changes.

For more info please [check here](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
</details>

<details>
  <summary><b>PyCharm - Choosing Your Testing Framework</b></summary>
 
1. Open the Settings/Preferences dialog, and under the node Tools, click the page **Python Integrated Tools**.
2. On this page, click the **Default Test Runner** field.
3. Choose the desired test runner:

<div align="center"> 
<img width="60%" height="60%" src="https://github.com/ikostan/SELENIUM_WEBDRIVER_WORKING_WITH_ELEMENTS/blob/master/testing_selenium_capabilities/img/py_choosing_test_runner.png" hspace="20">
</div>

For more info please see [Enable Pytest for you project](https://www.jetbrains.com/help/pycharm/pytest.html)
</details>

<details>
  <summary><b>Setting up Python3 virtual environment on Windows machine</b></summary>

1. open CMD<br/>
2. navigate to project directory, for example:<br/> 
```bash
cd C:\Users\superadmin\Desktop\Python\CodinGame
```
3. run following command:<br/> 
```bash 
pip install virtualenv
```
4. run following command:<br/> 
```bash 
virtualenv venv --python=python
```
</details>

<details>
  <summary><b>Setting up Python3 virtual environment on Linx (Ubuntu) machine</b></summary>

### How to install virtualenv

1. Install **pip** first
```bash
    sudo apt-get install python3-pip
```

2. Then install **virtualenv** using pip3
```bash
    sudo pip3 install virtualenv
```

3. Now create a virtual environment
```bash
    virtualenv venv
```
>you can use any name insted of **venv**

4. You can also use a Python interpreter of your choice:

```bash
    virtualenv -p /usr/bin/python2.7 venv
```

5. Active your virtual environment:

```bash
    source venv/bin/activate
```

6. Using fish shell:

```bash
    source venv/bin/activate.fish
```

7. To deactivate:

```bash
    deactivate
```

8. Create virtualenv using Python3:

```bash
    virtualenv -p python3 myenv
```

9. Instead of using virtualenv you can use this command in Python3:

```bash
    python3 -m venv myenv
```

[Source](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d)
</details>

<details>
  <summary><b>Activate Virtual Environment</b></summary>

In a newly created virtualenv there will be a bin/activate shell script. For Windows systems, activation scripts are provided for CMD.exe and Powershell.

1. Open Terminal
2. Run: \path\to\env\Scripts\activate 
  
[Source](https://pypi.org/project/virtualenv/1.8.2/)
</details>

<details>
  <summary><b>Auto generate requirements.txt</b></summary>

Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:
```bash
pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
```bash
pip install -r requirements.txt
```   
[Source](https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/)
</details>

<details>
  <summary><b>error: RPC failed; curl 56 Recv failure: Connection was reset</b></summary>

1. Open Git Bash<br/>
2. Run: "git config --global http.postBuffer 157286400" 
  
[Source](https://stackoverflow.com/questions/36940425/gitlab-push-failed-error)
</details>

<details>
  <summary><b>How to fix in case .gitignore is ignored by Git</b></summary>

Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore<br/> 

**NOTE:**

- First commit your current changes, or you will lose them.
- Then run the following commands from the top folder of your Git repository:

```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```
</details>

<details>
  <summary><b>How to generate Allure report with history trends (Windows OS)</b></summary>

<br/>Step by step:

1. Run tests from pytest using following arguments: -v --alluredir=allure-results
2. Copy '.\allure-report\history\' folder into '.\allure-results\history\'
3. Run: allure generate .\allure-results\ -o .\allure-report\ --clean
4. Following output should appear: Report successfully generated to .\allure-report
5. Run: allure open .\allure-report\

[Source](https://github.com/allure-framework/allure2/issues/813)
</details>

<details>
  <summary><b>Sphinx Documentation Set Up</b></summary>

<br/>Step by step:

1. Create docs directory
2. Open cmd > Go to docs directory
3. cmd > Run: sphinx-quickstart </b>
    **Note:** run with default answers
4. Go to docs/conf.py
5. Uncomment following lines:
```python
    import os
    import sys
    sys.path.insert(0, os.path.abspath('.'))
```
6. Update extensions list as following:
```python
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```
7. Update template as following:
```python
html_theme = 'sphinx_rtd_theme'

```
8. Update sys.path.insert as following:
```python
sys.path.insert(0, os.path.abspath('..'))
```
9. Go to docs/index.rst > add modules, see example below:
```bash

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
```
10. Open cmd > run: 
```python
sphinx-apidoc -o . ..
```
11. cmd > Run: make html
12. Install html template:
```python
pip install sphinx_rtd_theme
```

[Video Tutorial](https://www.youtube.com/watch?v=b4iFyrLQQh4)
[Sphinx Documentation](https://www.sphinx-doc.org/en/master/usage/quickstart.html)
[More Info](https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass)
</details>

<details>
  <summary><b>Auto-Generated Python Documentation with Sphinx</b></summary>

<br/>Step by step:

1. Open CMD
2. Go to docs directory
3. Run: make clean
4. Run: make html

[Source](https://www.youtube.com/watch?v=b4iFyrLQQh4)
</details>
