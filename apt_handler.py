import argh

from libboutique.services.packagekit.packagekit_service import PackageKitService

def progress_publisher(client, object):
    print("hello, callback !")

apt_service = PackageKitService(progress_publisher=progress_publisher)

def apt_command_list():
    packages = apt_service.list_installed_packages()
    #for package in packages:
    #    print(package)
    print(packages[0])

def apt_command_info():
    pass

apt_commands = {
    "list": apt_command_list,
    "info": apt_command_info
}

@argh.arg("command", choices=["list", "info"])
def apt(command):
    apt_command = apt_commands.get(command)
    apt_command()

