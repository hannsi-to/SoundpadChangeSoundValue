import pymem
import pymem.process

pm = pymem.Pymem("Soundpad.exe")
module = pymem.process.module_from_name(pm.process_handle, "Soundpad.exe")

base = module.lpBaseOfDll
address = base + 0xA27254

running = True

while running:
    value = pm.read_float(address)
    print("Current sound value:", value)

    new_value = input("New sound value (or 'exit'): ")

    if new_value.lower() == "exit":
        running = False
        continue

    try:
        new_float = float(new_value)
        pm.write_float(address, new_float)
        print("Written:", new_float)
    except ValueError:
        print("Invalid number!")