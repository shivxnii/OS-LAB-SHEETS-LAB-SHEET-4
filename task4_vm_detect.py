import subprocess

def detect_vm_windows():
    try:
        # Run systeminfo command on Windows
        output = subprocess.check_output("systeminfo", shell=True, text=True)

        # Keywords that indicate a VM
        vm_keywords = ["Virtual", "Hyper-V", "VMware", "VirtualBox", "Hypervisor"]

        # Check if any keyword appears in the systeminfo output
        if any(keyword in output for keyword in vm_keywords):
            print("Virtual Machine Detected on Windows")
        else:
            print("Running on Physical Machine (Not a VM)")

    except:
        print("Unable to detect virtualization")

detect_vm_windows()
