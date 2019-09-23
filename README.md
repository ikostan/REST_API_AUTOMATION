[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0a3c971aa10e4e93b15944480cbf9b15)](https://www.codacy.com/manual/ikostan/REST_API_AUTOMATION?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ikostan/REST_API_AUTOMATION&amp;utm_campaign=Badge_Grade)

# <i class="fab fa-python"></i>Practice REST API automation with Python 3

### Table of Contents:<br/>

:one: <a href="#main_objectives">Main Objectives</a><br>
:two: <a href="#official_documentation_sources">Official Documentation Sources</a><br>
:three: <a href="#additional_tech_info_resources">Additional Tech Info Resources</a><br>
:four: <a href="#dev_env">Dev Environment</a><br>
:five: <a href="#tools">Nice to have tools</a><br>
:six: <a href="#about">About REST API app</a><br>
:seven: <a href="#setup">REST API app setup</a><br>
:eight: <a href="#endpoints">API endpoints and examples</a><br>
:nine: <a href="#guidelines">General guidelines: How to set up dev environment</a><br>
:one::zero: <a href="#tech_issues">Tech Issues and Problem Solving</a><br>
:one::one: <a href="https://github.com/ikostan/TestAutomationFrameworkUsingAppiumWithPython/tree/master/tests">Tests</a><br>
:one::two: <a href="https://github.com/ikostan/TestAutomationFrameworkUsingAppiumWithPython/tree/master/utils">Utils</a><br/><br>

### Main Objectives:<br/>

<a id="main_objectives"></a>

- Creating REST API Automation
- Build fast and readable automation using minimal code
 - Industry-ready test structure
 - Build readable test report using Allure Framework
 - Test code should avoid violating principles like [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), [SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle) and [KISS](https://en.wikipedia.org/wiki/KISS_principle)
- Using cloud automation platforms: [Codacy](https://www.codacy.com/), [CirclerCI](https://circleci.com), [TravisCI](https://travis-ci.org), [INSPECODE](https://inspecode.rocro.com), [Codecov](https://codecov.io)

### Official Documentation Sources:<br/>

<a id="official_documentation_sources"></a>

- [Allure Test Report](http://allure.qatools.ru/)
- [cars-api](https://github.com/qxf2/cars-api)
- [Practice API automation](http://35.167.62.251/)
- [Flask](https://www.fullstackpython.com/flask.html)

### Additional Tech Info Resources<br/>

<a id="additional_tech_info_resources"></a>

- [Full Pytest documentation](http://doc.pytest.org/en/latest/contents.html)
- [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)
- [Allure Framework](https://docs.qameta.io/allure/)

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
- TBD

### Tech Issues and Problem Solving:<br/>

<a id="tech_issues"></a>
- TBD


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
  <summary><b>Activate Virtual Environment</b></summary>

In a newly created virtualenv there will be a bin/activate shell script. For Windows systems, activation scripts are provided for CMD.exe and Powershell.

 1. Open Terminal
 2. Run: \path\to\env\Scripts\activate 
  
[Source](https://pypi.org/project/virtualenv/1.8.2/)
</details>

<details>
  <summary><b>Auto generate requirements.txt</b></summary>

<br/>Any application typically has a set of dependencies that are required for that application to work. The requirements file is a way to specify and install specific set of package dependencies at once.<br/>
Use pip’s freeze command to generate a requirements.txt file for your project:<br/>

```python
pip freeze > requirements.txt
```

If you save this in requirements.txt, you can follow this guide: [PyCharm - Manage dependencies using requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), or you can:<br/>
   
```python
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

<br/>Even if you haven't tracked the files so far, Git seems to be able to "know" about them even after you add them to .gitignore.<br/> 

**NOTE:**<br/>
 - First commit your current changes, or you will lose them.<br/> 
 - Then run the following commands from the top folder of your Git repository:<br/> 
    
```bash 
git rm -r --cached .
git add .
git commit -m "fixed untracked files"
```
</details>
