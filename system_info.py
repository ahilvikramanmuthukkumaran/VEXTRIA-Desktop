
import platform
import subprocess
import json


def get_sys_info():
    result = subprocess.run(
        [
            "powershell",
            "-NoProfile",
            "-Command",
            "Get-CimInstance Win32_ComputerSystem | "
            "Select-Object Manufacturer, Model, TotalPhysicalMemory | "
            "ConvertTo-Json -Compress"
        ],
        capture_output=True,
        text=True,
        check=True,
        timeout=10
    )

    computer = json.loads(result.stdout)

    return {
        "OS": platform.system(),
        "OS Version": platform.platform(),
        "Processor": platform.processor(),
        "Manufacturer": computer.get("Manufacturer", "Unknown"),
        "Model": computer.get("Model", "Unknown"),
        "RAM (GB)": round(
            computer["TotalPhysicalMemory"] / (1024 ** 3), 2
        ),
    }