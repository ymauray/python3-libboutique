import argh

from libboutique.services.snap.snap_service import SnapService

# SNAPS 

class SnapProgressPublisher:
    def publish(client, object):
        print(f"client: {client}")
        print(f"object: {object}")

snap_service = SnapService(progress_publisher=SnapProgressPublisher)

def snap_command_list(_):
    packages = snap_service.list_installed_packages()
    #for package in packages:
    #    print(package)
    print(packages[0])

def snap_command_info(package_name):
    packages = snap_service.retrieve_package_information_by_name(package_name)
    for package in packages:
        print(package)

def snap_command_install(package_name):
    snap_service.install_package(package_name)

def snap_command_remove(package_name):
    snap_service.remove_package(package_name)

snap_commands = {
    "list": snap_command_list,
    "info": snap_command_info,
    "install": snap_command_install,
    "remove": snap_command_remove
}

@argh.arg("command", choices=["list", "info", "install", "remove"])
def snap(command, package_name = None):
    snap_command = snap_commands.get(command)
    snap_command(package_name)

