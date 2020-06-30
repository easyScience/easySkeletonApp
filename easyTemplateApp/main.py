import os, sys
from PySide2.QtCore import QUrl
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWidgets import QApplication

import easyAppGui
from easyTemplateApp.Logic.PyQmlProxy import PyQmlProxy


def main():
    # Define paths
    current_path = os.path.dirname(os.path.abspath(__file__))
    # current_path = os.path.dirname(sys.argv[0])
    main_qml_path = QUrl.fromLocalFile(os.path.join(current_path, "Gui", "main.qml"))
    gui_path = str(QUrl.fromLocalFile(os.path.join(current_path)).toString())
    easyAppGui_path = easyAppGui.__path__[0]
    #print("current_path", current_path)
    #print("main_qml_path", main_qml_path)
    #print("gui_path", gui_path)
    #print("easyAppGui_path", easyAppGui_path)

    # Create a proxy object between python logic and QML GUI
    py_qml_proxy_obj = PyQmlProxy()

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName(py_qml_proxy_obj.appName)

    # Create qml application engine
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("_screenshotPath", os.path.join(current_path, "..", "dist", "screenshot.png"))
    engine.rootContext().setContextProperty("_pyQmlProxyObj", py_qml_proxy_obj)
    engine.addImportPath(easyAppGui_path)
    engine.addImportPath(gui_path)
    engine.load(main_qml_path)

    # Event loop
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
