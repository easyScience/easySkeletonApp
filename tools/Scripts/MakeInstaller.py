#!/usr/bin/env python3

import os, sys
import xml.dom.minidom
import dephell_licenses
import Functions


CONFIG = Functions.config()

def qtifwSetupFileName():
    file_name_base = CONFIG['ci']['qtifw']['setup']['file_name_base']
    file_name_suffix = CONFIG['ci']['qtifw']['setup']['file_name_suffix'][Functions.osName()]
    file_ext = CONFIG['ci']['qtifw']['setup']['file_ext'][Functions.osName()]
    return f'{file_name_base}{file_name_suffix}{file_ext}'

def qtifwSetupDownloadDest():
    return os.path.join(CONFIG['ci']['project']['subdirs']['download'], f'{qtifwSetupFileName()}')

def qtifwSetupDownloadUrl():
    base_url = CONFIG['ci']['qtifw']['setup']['base_url']
    qtifw_version = CONFIG['ci']['qtifw']['setup']['version']
    return f'{base_url}/{qtifw_version}/{qtifwSetupFileName()}'

def qtifwSetupExe():
    setup_name, _ = os.path.splitext(qtifwSetupFileName())
    d = {
        'macos': f'/Volumes/{setup_name}/{setup_name}.app/Contents/MacOS/{setup_name}',
        'ubuntu': qtifwSetupDownloadDest(),
        'windows': qtifwSetupDownloadDest()
    }
    return d[Functions.osName()]

def qtifwDirPath():
    home_dir = os.path.expanduser('~')
    qtifw_version = CONFIG['ci']['qtifw']['setup']['version']
    d = {
        'macos': f'{home_dir}/Qt/QtIFW-{qtifw_version}',
        'ubuntu': f'{home_dir}/Qt/QtIFW-{qtifw_version}',
        'windows': f'C:\\Qt\\QtIFW-{qtifw_version}'
    }
    return d[Functions.osName()]

def licenseFile():
    return CONFIG['ci']['project']['license_file']

def appName():
    return CONFIG['tool']['poetry']['name']

def setupName():
    return f"{appName()}{CONFIG['ci']['app']['setup']['file_name_suffix']}"

def distributionDir():
    return CONFIG['ci']['project']['subdirs']['distribution']

def scriptsDir():
    return CONFIG['ci']['project']['subdirs']['scripts']

def setupBuildDir():
    return os.path.join(CONFIG['ci']['project']['subdirs']['build'], setupName())

def configDirPath():
    return os.path.join(setupBuildDir(), CONFIG['ci']['app']['setup']['build']['config_dir'])

def configXmlPath():
    return os.path.join(configDirPath(), CONFIG['ci']['app']['setup']['build']['config_xml'])

def packagesDirPath():
    return os.path.join(setupBuildDir(), CONFIG['ci']['app']['setup']['build']['packages_dir'])

def repositoryDir():
    repository_dir_suffix = CONFIG['ci']['app']['setup']['repository_dir_suffix']
    repository_os_suffix = CONFIG['ci']['app']['setup']['repository_os_suffix'][Functions.osName()]
    return os.path.join(f'{appName()}{repository_dir_suffix}', repository_os_suffix)

def installationDir():
    var = CONFIG['ci']['app']['setup']['installation_dir'][Functions.osName()]
    return Functions.environmentVariable(var, var)

def installerConfigXml():
    try:
        message = f"create {CONFIG['ci']['app']['setup']['build']['config_xml']} content"
        app_version = CONFIG['ci']['app']['setup']['version']
        app_url = CONFIG['tool']['poetry']['homepage']
        target_dir = os.path.join(installationDir(), appName())
        maintenance_tool_suffix = CONFIG['ci']['app']['setup']['maintenance_tool_suffix']
        maintenance_tool_name = maintenance_tool_suffix #f'{appName()}{maintenance_tool_suffix}'
        config_control_script = CONFIG['ci']['scripts']['config_control']
        raw_xml = Functions.dict2xml({
            'Installer': {
                'Name': appName(),
                'Version': app_version,
                'Title': appName(),
                'Publisher': appName(),
                'ProductUrl': app_url,
                #'Logo': 'logo.png',
                #'WizardStyle': 'Classic', #'Aero',
                'StartMenuDir': appName(),
                'TargetDir': target_dir,
                'RemoteRepositories': {
                    'Repository': {
                        #'Url': f'http://localhost/{repositoryDir()}'
                        'Url': f'http://easyscience.apptimity.com/{repositoryDir()}'
                    }
                },
                'MaintenanceToolName': maintenance_tool_name,
                'AllowNonAsciiCharacters': 'true',
                'AllowSpaceInPath': 'true',
                'InstallActionColumnVisible': 'false',
                'ControlScript': config_control_script,
            }
        })
        pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml()
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)
        return pretty_xml

def appPackageXml():
    try:
        message = f"create app package content"
        description = CONFIG['tool']['poetry']['description']
        version = CONFIG['tool']['poetry']['version']
        release_date = "2020-01-01" #datetime.datetime.strptime(config['release']['date'], "%d %b %Y").strftime("%Y-%m-%d")
        package_install_script = CONFIG['ci']['scripts']['package_install']
        license_id = CONFIG['tool']['poetry']['license'].replace('-only', '')
        license_name = dephell_licenses.licenses.get_by_id(license_id).name
        raw_xml = Functions.dict2xml({
            'Package': {
                'DisplayName': appName(),
                'Description': description,
                'Version': version,
                'ReleaseDate': release_date,
                'Default': 'true',
                'Essential': 'true',
                'ForcedInstallation': 'true',
                #'RequiresAdminRights': 'true',
                'Licenses': {
                    'License': {
                        '@name': license_name,
                        '@file': licenseFile()
                    }
                },
                'Script': package_install_script,
            }
        })
        pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml()
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)
        return pretty_xml

def docsPackageXml():
    try:
        message = f"create docs package content"
        name = CONFIG['ci']['app']['setup']['build']['docs_package_name']
        description = CONFIG['ci']['app']['setup']['build']['docs_package_description']
        version = CONFIG['ci']['app']['setup']['build']['docs_package_version']
        release_date = "2020-01-01" #datetime.datetime.strptime(config['release']['date'], "%d %b %Y").strftime("%Y-%m-%d")
        raw_xml = Functions.dict2xml({
            'Package': {
                'DisplayName': name,
                'Description': description,
                'Version': version,
                'ReleaseDate': release_date,
                'Default': 'true',
            }
        })
        pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml()
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)
        return pretty_xml

def downloadQtInstallerFramework():
    Functions.createDir(CONFIG['ci']['project']['subdirs']['download'])
    Functions.downloadFile(
        url=qtifwSetupDownloadUrl(),
        destination=qtifwSetupDownloadDest()
    )

def osDependentPreparation():
    message = f'prepare for os {Functions.osName()}'
    if Functions.osName() == 'macos':
        Functions.attachDmg(qtifwSetupDownloadDest())
    elif Functions.osName() == 'ubuntu':
        Functions.run('sudo', 'apt-get', 'install', '-qq', 'libxkbcommon-x11-0')
        Functions.setEnvironmentVariable('QT_QPA_PLATFORM', 'minimal')
        Functions.addReadPermission(qtifwSetupExe())
    else:
        Functions.printNeutralMessage(f'No preparation needed for os {Functions.osName()}')

def installQtInstallerFramework():
    if os.path.exists(qtifwDirPath()):
        Functions.printNeutralMessage(f'QtInstallerFramework was already installed to {qtifwDirPath()}')
        return
    try:
        message = f'install QtInstallerFramework to {qtifwDirPath()}'
        silent_script = os.path.join(scriptsDir(), CONFIG['ci']['scripts']['silent_install'])
        Functions.installSilently(
            installer=qtifwSetupExe(),
            silent_script=silent_script
        )
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def createInstallerSourceDir():
    try:
        message = f'create installer source directory {setupBuildDir()}'
        # base
        Functions.createDir(setupBuildDir())
        # config
        config_control_script_path = os.path.join(scriptsDir(), CONFIG['ci']['scripts']['config_control'])
        Functions.createDir(configDirPath())
        Functions.createFile(path=configXmlPath(), content=installerConfigXml())
        Functions.copyFile(source=config_control_script_path, destination=configDirPath())
        # package: app
        app_subdir_path =  os.path.join(packagesDirPath(), CONFIG['ci']['app']['setup']['build']['app_package_subdir'])
        app_data_subsubdir_path =  os.path.join(app_subdir_path, CONFIG['ci']['app']['setup']['build']['data_subsubdir'])
        app_meta_subsubdir_path =  os.path.join(app_subdir_path, CONFIG['ci']['app']['setup']['build']['meta_subsubdir'])
        app_package_xml_path = os.path.join(app_meta_subsubdir_path, CONFIG['ci']['app']['setup']['build']['package_xml'])
        package_install_script_src = os.path.join(scriptsDir(), CONFIG['ci']['scripts']['package_install'])
        freezed_app_src = os.path.join(distributionDir(), f"{appName()}{CONFIG['ci']['pyinstaller']['dir_suffix'][Functions.osName()]}")
        Functions.createDir(packagesDirPath())
        Functions.createDir(app_subdir_path)
        Functions.createDir(app_data_subsubdir_path)
        Functions.createDir(app_meta_subsubdir_path)
        Functions.createFile(path=app_package_xml_path, content=appPackageXml())
        Functions.copyFile(source=package_install_script_src, destination=app_meta_subsubdir_path)
        Functions.copyFile(source=licenseFile(), destination=app_meta_subsubdir_path)
        Functions.moveDir(source=freezed_app_src, destination=app_data_subsubdir_path)
        # package: docs
        docs_subdir_path = os.path.join(packagesDirPath(), CONFIG['ci']['app']['setup']['build']['docs_package_subdir'])
        docs_data_subsubdir_path = os.path.join(docs_subdir_path, CONFIG['ci']['app']['setup']['build']['data_subsubdir'])
        docs_meta_subsubdir_path = os.path.join(docs_subdir_path, CONFIG['ci']['app']['setup']['build']['meta_subsubdir'])
        docs_package_xml_path = os.path.join(docs_meta_subsubdir_path, CONFIG['ci']['app']['setup']['build']['package_xml'])
        docs_dir_src = CONFIG['ci']['project']['subdirs']['docs']
        Functions.createDir(docs_subdir_path)
        Functions.createDir(docs_data_subsubdir_path)
        Functions.createDir(docs_meta_subsubdir_path)
        Functions.createFile(path=docs_package_xml_path, content=docsPackageXml())
        Functions.copyDir(source=docs_dir_src, destination=os.path.join(docs_data_subsubdir_path, 'Documentation'))
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def createOnlineRepository():
    try:
        message = 'create online repository'
        qtifw_bin_dir_path = os.path.join(qtifwDirPath(), 'bin')
        qtifw_repogen_path = os.path.join(qtifw_bin_dir_path, 'repogen')
        repository_os_suffix = f"{appName()}{CONFIG['ci']['app']['setup']['repository_os_suffix']}"
        repository_dir_path = os.path.join(CONFIG['ci']['project']['subdirs']['distribution'], repositoryDir())
        Functions.run(
            qtifw_repogen_path,
            '--update-new-components',
            '-p', packagesDirPath(),
            repository_dir_path
        )
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

def createInstaller():
    try:
        message = 'create installer'
        qtifw_bin_dir_path = os.path.join(qtifwDirPath(), 'bin')
        qtifw_binarycreator_path = os.path.join(qtifw_bin_dir_path, 'binarycreator')
        qtifw_installerbase_path = os.path.join(qtifw_bin_dir_path, 'installerbase')
        setup_exe_path = os.path.join(distributionDir(), setupName())
        Functions.run(
            qtifw_binarycreator_path,
            '--verbose',
            #'--online-only',
            #'--offline-only',
            '-c', configXmlPath(),
            '-p', packagesDirPath(),
            '-t', qtifw_installerbase_path,
            setup_exe_path
        )
    except Exception as exception:
        Functions.printFailMessage(message, exception)
        sys.exit()
    else:
        Functions.printSuccessMessage(message)

if __name__ == "__main__":
    downloadQtInstallerFramework()
    osDependentPreparation()
    installQtInstallerFramework()
    createInstallerSourceDir()
    createOnlineRepository()
    createInstaller()
