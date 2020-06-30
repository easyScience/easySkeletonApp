import QtQuick 2.13
import QtQuick.Controls 2.13

import easyAppGui.Globals 1.0 as EaGlobals
import easyAppGui.Elements 1.0 as EaElements
import easyAppGui.Components 1.0 as EaComponents

import Gui.Globals 1.0 as ExGlobals

EaComponents.SideBarColumn {
    width: parent.width

    EaElements.GroupBox {
        title: qsTr("Group 1")
        collapsible: false

        EaElements.SideBarButton {
            fontIcon: "plus-circle"
            text: "Button 1"
        }
    }

    EaElements.GroupBox {
        title: qsTr("Group 2")
        collapsed: false

        Grid {
            columns: 1
            columnSpacing: 20
            rowSpacing: 10
            verticalItemAlignment: Grid.AlignVCenter

            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
            EaElements.Label { text: "Parameter: 100" }
        }
    }

    EaElements.GroupBox {
        title: qsTr("Group 3")
        collapsed: false

        EaElements.SideBarButton {
            fontIcon: "plus-circle"
            text: "Button 2"
        }
    }

}

