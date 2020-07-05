import os, sys
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

import easyAppGui
from easyTemplateApp.Logic.PyQmlProxy import PyQmlProxy


def testMode():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            return True
    return False

def screenshotsDir():
    if len(sys.argv) > 2:
        return sys.argv[2]
    return None

def main():
    # Define paths
    current_path = os.path.dirname(sys.argv[0])
    package_path = os.path.join(current_path, "easyTemplateApp")
    main_qml_path = QUrl.fromLocalFile(os.path.join(package_path, "Gui", "main.qml"))
    gui_path = str(QUrl.fromLocalFile(package_path).toString())
    easyAppGui_path = easyAppGui.__path__[0]

    # Create a proxy object between python logic and QML GUI
    py_qml_proxy_obj = PyQmlProxy()

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName(py_qml_proxy_obj.appName)

    # Create qml application engine
    engine = QQmlApplicationEngine()
    #engine.rootContext().setContextProperty("_screenshotPath", os.path.join(current_path, "..", "dist", "screenshot.png"))
    engine.rootContext().setContextProperty("_pyQmlProxyObj", py_qml_proxy_obj)
    engine.rootContext().setContextProperty("_testMode", testMode())
    engine.rootContext().setContextProperty("_screenshotsDir", screenshotsDir())
    engine.addImportPath(easyAppGui_path)
    engine.addImportPath(gui_path)
    engine.load(main_qml_path)

    # Event loop
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
