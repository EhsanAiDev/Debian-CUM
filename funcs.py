import subprocess
import re 

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
    governor_text.configure(text=f"Your Current Governor: {g}")


