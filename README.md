# easySkeletonApp
Template for easyScience applications

[![CI Build][20]][21]

[![Release][30]][31]

[![Downloads][70]][71] [![Lines of code][81]]() [![Total lines][80]]() [![Files][82]]()

[![License][50]][51]

[![w3c][90]][91]

## Download easyTemplate
* Open **Terminal**
* Change the current working directory to the location where you want the **easySkeletonApp** directory
* Clone **easySkeletonApp** repo from GitHub using **git**
  ```
  git clone https://github.com/easyScience/easySkeletonApp
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
* Go to **easySkeletonApp** directory
* Create virtual environment for **easyTemplate** and install its dependences using **poetry** (configuration file: **pyproject.toml**)
  ```
  poetry install --no-dev
  ```
  
## Launch easyTemplate application
* Open **Terminal**
* Go to **easySkeletonApp** directory
* Launch **easyTemplate** application using **poetry**
  ```
  poetry run easyTemplate
  ```

## Update easyTemplate dependencies
* Open **Terminal**
* Go to **easySkeletonApp** directory
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

## Test easyTemplate
* Unit tests
  * ...
* GUI
   * Test video: https://easyscience.github.io/easySkeletonApp


<!---URLs--->
<!---https://naereen.github.io/badges/--->

<!---CI Build Status--->
[20]: https://github.com/easyScience/easySkeletonApp/workflows/macOS,%20Linux,%20Windows/badge.svg
[21]: https://github.com/easyScience/easySkeletonApp/actions

<!---Release--->
[30]: https://img.shields.io/github/release/easyScience/easySkeletonApp.svg
[31]: https://github.com/easyScience/easySkeletonApp/releases

<!---License--->
[50]: https://img.shields.io/github/license/easyScience/easySkeletonApp.svg
[51]: https://github.com/easyScience/easySkeletonApp/blob/master/LICENSE.md

<!---LicenseScan--->
[60]: https://app.fossa.com/api/projects/git%2Bgithub.com%2FeasyScience%2FeasySkeletonApp.svg?type=shield
[61]: https://app.fossa.com/projects/git%2Bgithub.com%2FeasyScience%2FeasySkeletonApp?ref=badge_shield

<!---Downloads--->
[70]: https://img.shields.io/github/downloads/easyScience/easySkeletonApp/total.svg
[71]: https://github.com/easyScience/easySkeletonApp/releases

<!---Code statistics--->
[80]: https://tokei.rs/b1/github/easyScience/easySkeletonApp
[81]: https://tokei.rs/b1/github/easyScience/easySkeletonApp?category=code
[82]: https://tokei.rs/b1/github/easyScience/easySkeletonApp?category=files

<!---W3C validation--->
[90]: https://img.shields.io/w3c-validation/default?targetUrl=https://easyscience.github.io/easySkeletonApp
[91]: https://easyscience.github.io/easySkeletonApp
