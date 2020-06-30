import QtQuick 2.13
import QtQuick.Controls 2.13

import easyAppGui.Style 1.0 as EaStyle
import easyAppGui.Elements 1.0 as EaElements
import easyAppGui.Components 1.0 as EaComponents

import Gui.Globals 1.0 as ExGlobals

Item {

    Column {
        anchors.centerIn: parent
        spacing: 0

        EaElements.Button {
            highlighted: true
            text: "Tutorial 1: Data fitting"
            onClicked: runTutorial1()
        }

        EaElements.Button {
            highlighted: true
            text: "Tutorial 2: App settings"
            onClicked: runTutorial2()
        }
    }

    EaElements.RemoteController {
        id: rc
    }

    function runTutorial1() {
        rc.wait(1000)
        rc.show()

        rc.mouseClick(ExGlobals.Variables.sampleTabButton)
        rc.mouseClick(ExGlobals.Variables.addNewSampleButton)
        rc.mouseClick(ExGlobals.Variables.amplitudeTextInput)
        rc.clearText(4)
        rc.typeText("2.10")
        rc.mouseClick(ExGlobals.Variables.periodTextInput)
        rc.clearText(2)
        rc.typeText("30")
        rc.keyClick(Qt.Key_Enter)

        rc.wait(2000)
        rc.mouseClick(ExGlobals.Variables.experimentTabButton)
        rc.mouseClick(ExGlobals.Variables.generateMeasuredDataButton)

        rc.wait(1000)
        rc.mouseClick(ExGlobals.Variables.analysisTabButton)
        rc.mouseClick(ExGlobals.Variables.xShiftTextInput)
        rc.clearText(4)
        rc.typeText("-0.30")
        rc.mouseClick(ExGlobals.Variables.yShiftTextInput)
        rc.clearText(2)
        rc.typeText("40")
        rc.keyClick(Qt.Key_Enter)
        rc.wait(1000)
        rc.mouseClick(ExGlobals.Variables.startFittingButton)

        rc.wait(1000)
        rc.hide()
    }

    function runTutorial2() {
        rc.wait(1000)
        rc.show()

        rc.mouseClick(ExGlobals.Variables.preferencesButton)
        rc.mouseClick(ExGlobals.Variables.themeSelector)

        const x_pos = undefined
        let y_pos = EaStyle.Colors.isDarkTheme ? EaStyle.Sizes.comboBoxHeight * 1.5 : undefined
        rc.mouseClick(ExGlobals.Variables.themeSelector, x_pos, y_pos)

        rc.wait(1000)
        rc.mouseClick(ExGlobals.Variables.themeSelector)
        y_pos = EaStyle.Colors.isDarkTheme ? EaStyle.Sizes.comboBoxHeight * 1.5 : undefined
        rc.mouseClick(ExGlobals.Variables.themeSelector, x_pos, y_pos)

        rc.wait(1000)
        rc.keyClick(Qt.Key_Escape)

        rc.wait(1000)
        rc.hide()
    }
}
