import subprocess 

data = str(subprocess.check_output("Get-PnpDevice -Class AudioEndpoint && Bluetooth | Select-Object Name, Status"))

print(data);