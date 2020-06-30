pragma Singleton

import QtQuick 2.13

QtObject {
    property var proxy: _pyQmlProxyObj

    property var homeTabButton
    property var projectTabButton
    property var sampleTabButton
    property var experimentTabButton
    property var analysisTabButton
    property var summaryTabButton

    property var preferencesButton

    property var addNewSampleButton
    property var generateMeasuredDataButton
    property var startFittingButton

    property var amplitudeTextInput
    property var periodTextInput
    property var xShiftTextInput
    property var yShiftTextInput

    property var themeSelector
}
