import os 
import re 
import subprocess

def get_current_governor():
    result = subprocess.run("cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor",
                            text=True,
                            shell=True,
                            capture_output=True).stdout
    
    return result.split("\n")[0]

def get_governors():
    result = subprocess.run("cpupower frequency-info",
                            shell=True,
                            capture_output=True,
                            text=True).stdout
    match = re.search(pattern=r"available cpufreq governors:\s*(.+)" , string=result)

    if match:
        governors = match.group(1).split()
        return governors
    else:
        return None
    

def set_governor(g,governor_text):
    service_text = f"""
[Unit]
Description=Set CPU governor

[Service]
Type=oneshot
ExecStart=/usr/bin/cpupower frequency-set -g {g}

[Install]
WantedBy=multi-user.target
"""
    
    with open('/tmp/cpupower.service', 'w') as temp_file:
        temp_file.write(service_text)
    os.system(f"pkexec cpupower frequency-set -g {g}")
    os.system(f"pkexec mv /tmp/cpupower.service /etc/systemd/system/cpupower.service")
    os.system(f"pkexec systemctl enable cpupower.service")
    governor_text.configure(text=f"Your Current Governor: {g}")

        


