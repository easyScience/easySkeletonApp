import QtQuick 2.13
import QtQuick.Controls 2.13

import easyAppGui.Elements 1.0 as EaElements
import easyAppGui.Components 1.0 as EaComponents

import Gui.Globals 1.0 as ExGlobals

EaComponents.SideBarColumn {
    width: parent.width

    EaElements.GroupBox {
        title: qsTr("Calculator")
        collapsible: false

        EaElements.ComboBox {
            width: 200
            currentIndex: ExGlobals.Variables.proxy.calculatorInt
            model: ExGlobals.Variables.proxy.calculatorList
            Component.onCompleted: ExGlobals.Variables.proxy.calculatorInt = currentIndex
        }
    }

}
