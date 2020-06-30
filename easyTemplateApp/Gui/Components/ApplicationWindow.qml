import QtQuick 2.13
import QtQuick.Controls 2.13

import easyAppGui.Style 1.0 as EaStyle
import easyAppGui.Globals 1.0 as EaGlobals
import easyAppGui.Elements 1.0 as EaElements
import easyAppGui.Components 1.0 as EaComponents

import Gui.Globals 1.0 as ExGlobals
import Gui.Pages.Home 1.0 as ExHomePage
import Gui.Pages.Project 1.0 as ExProjectPage
import Gui.Pages.Sample 1.0 as ExSamplePage
import Gui.Pages.Experiment 1.0 as ExExperimentPage
import Gui.Pages.Analysis 1.0 as ExAnalysisPage
import Gui.Pages.Summary 1.0 as ExSummaryPage

EaComponents.ApplicationWindow {

    ///////////////////
    // APPLICATION BAR
    ///////////////////

    // Left group of application bar tool buttons
    appBarLeftButtons: [
        EaElements.ToolButton {
            fontIcon: "\uf0c7"
            ToolTip.text: qsTr("Save current state of the project")
        },
        EaElements.ToolButton {
            fontIcon: "\uf2ea"
            ToolTip.text: qsTr("Undo")
        },
        EaElements.ToolButton {
            fontIcon: "\uf2f9"
            ToolTip.text: qsTr("Redo")
        }
    ]

    // Right group of application bar tool buttons
    appBarRightButtons: [
        EaElements.ToolButton {
            id: preferencesButton
            fontIcon: "\uf013"
            ToolTip.text: qsTr("Application preferences")
            onClicked: EaGlobals.Variables.showAppPreferencesDialog = true
            Component.onCompleted: ExGlobals.Variables.preferencesButton = preferencesButton
        },
        EaElements.ToolButton {
            fontIcon: "\uf059"
            ToolTip.text: qsTr("Get online help")
        },
        EaElements.ToolButton {
            fontIcon: "\uf188"
            ToolTip.text: qsTr("Report a bug or issue")
        }
    ]

    // Central group of application bar tab buttons (workflow tabs)
    // Tab buttons for the pages described below
    appBarCentralTabs: [
        // Home tab
        EaElements.TabButton {
            id: homeTabButton
            enabled: EaGlobals.Variables.homePageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "home"
            text: qsTr("Home")
            ToolTip.text: qsTr("Home page")
            Component.onCompleted: ExGlobals.Variables.homeTabButton = homeTabButton
        },
        // Project tab
        EaElements.TabButton {
            id: projectTabButton
            enabled: EaGlobals.Variables.projectPageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "archive"
            text: qsTr("Project")
            ToolTip.text: qsTr("Project description page")
            Component.onCompleted: ExGlobals.Variables.projectTabButton = projectTabButton
        },
        // Sample tab
        EaElements.TabButton {
            id: sampleTabButton
            enabled: EaGlobals.Variables.samplePageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "gem"
            text: qsTr("Sample")
            ToolTip.text: qsTr("Sample model description page")
            Component.onCompleted: ExGlobals.Variables.sampleTabButton = sampleTabButton
        },
        // Experiment tab
        EaElements.TabButton {
            id: experimentTabButton
            enabled: EaGlobals.Variables.experimentPageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "microscope"
            text: qsTr("Experiment")
            ToolTip.text: qsTr("Experimental settings and data page")
            Component.onCompleted: ExGlobals.Variables.experimentTabButton = experimentTabButton
        },
        // Analysis tab
        EaElements.TabButton {
            id: analysisTabButton
            enabled: EaGlobals.Variables.analysisPageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "calculator"
            text: qsTr("Analysis")
            ToolTip.text: qsTr("Simulation and fitting page")
            Component.onCompleted: ExGlobals.Variables.analysisTabButton = analysisTabButton
        },
        // Summary tab
        EaElements.TabButton {
            id: summaryTabButton
            enabled: EaGlobals.Variables.summaryPageEnabled
            implicitHeight: EaStyle.Sizes.appBarHeight
            fontIcon: "clipboard-list"
            text: qsTr("Summary")
            ToolTip.text: qsTr("Summary of the work done")
            Component.onCompleted: ExGlobals.Variables.summaryTabButton = summaryTabButton
        }
    ]

    /////////////////////////
    // MAIN CONTENT + SIDEBAR
    /////////////////////////

    // Pages for the tab buttons described above
    contentArea: [
        // Home page
        ExHomePage.MainContent {},
        // Project page
        EaComponents.ContentPage {
            mainContent: EaComponents.MainContent {
                tabs: [
                    EaElements.TabButton {
                        text: qsTr("Description")
                    },
                    EaElements.TabButton {
                        text: qsTr("project.cif")
                    }
                ]

                items: [
                    ExProjectPage.MainContentDescription {},
                    ExProjectPage.MainContentCifEdit {}
                ]
            }

            sideBar: EaComponents.SideBar {
                basicControls: ExProjectPage.SideBarBasic {}
                advancedControls: ExProjectPage.SideBarAdvanced {}
            }
        },
        // Sample page
        EaComponents.ContentPage {
            mainContent: EaComponents.MainContent {
                tabs: [
                    EaElements.TabButton {
                        text: qsTr("Structure view")
                    },
                    EaElements.TabButton {
                        text: qsTr("samples.cif")
                    }
                ]

                items: [
                    ExSamplePage.MainContentStructureView {},
                    ExSamplePage.MainContentCifEdit {}
                ]
            }

            sideBar: EaComponents.SideBar {
                basicControls: ExSamplePage.SideBarBasic {}
                advancedControls: ExSamplePage.SideBarAdvanced {}
            }
        },
        // Experiment page
        EaComponents.ContentPage {
            mainContent: EaComponents.MainContent {
                tabs: [
                    EaElements.TabButton {
                        text: qsTr("Plot view")
                    },
                    EaElements.TabButton {
                        text: qsTr("Table view")
                    },
                    EaElements.TabButton {
                        text: qsTr("experiments.cif")
                    }
                ]

                items: [
                    ExExperimentPage.MainContentPlotView {},
                    ExExperimentPage.MainContentTableView {},
                    ExExperimentPage.MainContentCifEdit {}
                ]
            }

            sideBar: EaComponents.SideBar {
                basicControls: ExExperimentPage.SideBarBasic { id: experimentSideBarBasic }
                advancedControls: ExExperimentPage.SideBarAdvanced {}
            }
        },
        // Analysis page
        EaComponents.ContentPage {
            mainContent: EaComponents.MainContent {
                tabs: [
                    EaElements.TabButton {
                        text: qsTr("Fitting")
                    },
                    EaElements.TabButton {
                        text: qsTr("calculations.cif")
                    }
                ]

                items: [
                    ExAnalysisPage.MainContentFitting {},
                    ExAnalysisPage.MainContentCifEdit {}
                ]
            }

            sideBar: EaComponents.SideBar {
                basicControls: ExAnalysisPage.SideBarBasic {}
                advancedControls: ExAnalysisPage.SideBarAdvanced {}
            }
        },
        // Summary page
        EaComponents.ContentPage {
            mainContent: EaComponents.MainContent {
                tabs: [
                    EaElements.TabButton {
                        text: qsTr("Report")
                    }
                ]

                items: [
                    ExSummaryPage.MainContentReport {}
                ]
            }

            sideBar: EaComponents.SideBar {
                basicControls: ExSummaryPage.SideBarBasic {}
                advancedControls: ExSummaryPage.SideBarAdvanced {}
            }
        }
    ]

    /////////////
    // STATUS BAR
    /////////////

    statusBar: EaElements.StatusBar {
        text: "Status bar"
    }

    /*
    Item {
        id: item
        anchors.fill: parent
    }

    Timer {
        id: quit
        interval: 5000
        onTriggered: {
            print("* closing app")
            Qt.quit()
        }
    }

    Timer {
        id: saveScreenshot
        interval: 5000
        onTriggered: {
            print("* saving screenshot")
            print("* screenshot path:", _screenshotPath)
            analysisTabButton.grabToImage(function(result) { result.saveToFile(_screenshotPath) })
            quit.start()
        }
    }

    Component.onCompleted: {
        print("* windows size:", window.width, "x", window.height)
        saveScreenshot.start()
    }
    */
}
