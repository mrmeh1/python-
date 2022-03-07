import subprocess

c = subprocess.run(["netsh","wlan","show","profiles"],capture_output=True,errors="ignore").stdout

c = c.encode("utf-8").decode("utf-8").strip().split("\n")

profiles,wifis = [],[]
for line in c:
    if "All The Profiles" in line:
        profiles.append(line.strip().split(":")[1].strip())

if len(profiles)       