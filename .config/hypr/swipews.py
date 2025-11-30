import subprocess

# Obtener el valor del monitor actual
result = subprocess.run(['hyprctl', 'activeworkspace'], stdout=subprocess.PIPE, text=True)
# Filtrar
monitor_id = None
for line in result.stdout.splitlines():
	if "monitorID" in line:
		monitor_id = line.split()[-1]
		break
# Hacer el efecto toggle entre monitores
if monitor_id == '1':
	subprocess.run(['hyprctl', 'dispatch', 'movecurrentworkspacetomonitor', '0'])
elif monitor_id == '0':
	subprocess.run(['hyprctl', 'dispatch', 'movecurrentworkspacetomonitor', '1'])