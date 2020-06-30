# easyTemplateApp
Template for easyScience applications

[![CI Build][20]][21]

[![Release][30]][31]

[![Downloads][70]][71] [![Lines of code][81]]() [![Total lines][80]]() [![Files][82]]()

[![License][50]][51] [![License Scan][60]][61]

## Download easyTemplate
* Open **Terminal**
* Change the current working directory to the location where you want the **easyTemplateApp** directory
* Clone **easyTemplateApp** repo from GitHub using **git**
  ```
  git clone https://github.com/easyScience/easyTemplateApp
  ```
  
## Install easyTemplate dependencies
* Open **Terminal**
* Install [**Poetry**](https://python-poetry.org/docs/) (Python dependency manager)
  * osx / linux / bashonwindows
    ```
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    ```
  * windows powershell
    ```
    (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
    ```
* Go to **easyTemplateApp** directory
* Create virtual environment for **easyTemplate** and install its dependences using **poetry** (configuration file: **pyproject.toml**)
  ```
  poetry install --no-dev
  ```
  
## Launch easyTemplate application
* Open **Terminal**
* Go to **easyTemplateApp** directory
* Launch **easyTemplate** application using **poetry**
  ```
  poetry run easytemplate
  ```

## Update easyTemplate dependencies
* Open **Terminal**
* Go to **easyTemplateApp** directory
* Update **easyTemplate** using **poetry** (configuration file: **pyproject.toml**)
  ```
  poetry update --no-dev
  ```

## Delete easyTemplate
* ...
* Uninstall **Poetry**
   * osx / linux / bashonwindows
   ```
   curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | POETRY_UNINSTALL=1 python
   ```

<!---URLs--->
<!---https://naereen.github.io/badges/--->

<!---CI Build Status--->
[20]: https://github.com/easyScience/easyTemplateApp/workflows/macOS,%20Linux,%20Windows/badge.svg
[21]: https://github.com/easyScience/easyTemplateApp/actions

<!---Release--->
[30]: https://img.shields.io/github/release/easyScience/easyTemplateApp.svg
[31]: https://github.com/easyScience/easyTemplateApp/releases

<!---License--->
[50]: https://img.shields.io/github/license/easyScience/easyTemplateApp.svg?color=blue&label=license
[51]: https://github.com/easyScience/easyTemplateApp/blob/master/LICENSE

<!---LicenseScan--->
[60]: https://app.fossa.com/api/projects/git%2Bgithub.com%2FeasyScience%2FeasyTemplateApp.svg?type=shield
[61]: https://app.fossa.com/projects/git%2Bgithub.com%2FeasyScience%2FeasyTemplateApp?ref=badge_shield

<!---Downloads--->
[70]: https://img.shields.io/github/downloads/easyScience/easyTemplateApp/total.svg
[71]: https://github.com/easyScience/easyTemplateApp/releases

<!---Code statistics--->
[80]: https://tokei.rs/b1/github/easyScience/easyTemplateApp
[81]: https://tokei.rs/b1/github/easyScience/easyTemplateApp?category=code
[82]: https://tokei.rs/b1/github/easyScience/easyTemplateApp?category=files
