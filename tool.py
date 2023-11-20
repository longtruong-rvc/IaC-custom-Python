import os
from pathlib import Path
import platform
import subprocess

"""
    Description: Create a tool that install applications to the webserver such as: aws-cli, java, ...
"""
def install_aws_cli(machine: str, work_dir: str) -> int:
    if not subprocess.run(["which", "aws"]).returncode:
        print("AWS-CLI has been installed on the Host machine")
        return 1

    # Create a temporary folder in the current working dir to store zip file
    aws_path = "aws_file"
    path = os.path.join(work_dir, aws_path)
    if not Path(path).exists():
        os.mkdir(path)
    os.chdir(path)

    # Download aws-cli binary
    # Use subprocess with wget instead of request module to fasten the download

    zip_file = f"awscli-exe-linux-{machine}.zip"
    zip_path = os.path.join(os.getcwd(), zip_file)

    if not os.path.isfile(zip_path):
        subprocess.run(
            ["wget", f"https://awscli.amazonaws.com/{zip_file}"],
            stderr=subprocess.STDOUT
        )
    # Extract aws-cli binary file
    subprocess.run(
            ["unzip", f"{zip_file}"],
            stdout=subprocess.STDOUT
    )
    # Check if aws-cli is installed successfully
    subprocess.run(["sudo", f"./aws/install"])
    print("Successfully install aws-cli on Host machine")
    return 0


if __name__ == "__main__":
    machine_arch = platform.machine()
    current_dir = os.getcwd()
    print(install_aws_cli(machine=machine_arch, work_dir=current_dir))