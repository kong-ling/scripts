from infi.devicemanager import DeviceManager
dm = DeviceManager()
print(dm)
dm.root.rescan()
disks = dm.disk_drives
names = [disk.friendly_name for disk in disks]

for name in names:
    print(name)
