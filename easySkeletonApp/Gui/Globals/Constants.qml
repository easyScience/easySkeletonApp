pragma Singleton

import QtQuick 2.13

QtObject {
    readonly property string appVersion: "0.5.0" // TODO: Get from phython logic
    readonly property string appName: _pyQmlProxyObj.appName
}
