import os.path
import urllib.request

print('''+--------------------------------------+
|          arcdps_updater 0.1          |
+--------------------------------------+
|   Coded in Python3 by Atrox Obitus   |
+--------------------------------------+
|    Compiled with "auto-py-to-exe"    |
+--------------------------------------+\n''')

if os.path.isfile('Gw2-64.exe'):
    print('Gw2-64.exe found!\n')
else:
    print('Gw2-64.exe not found!\n')
    print('Please copy this program in your "Guild Wars 2" folder and start it again!\n')
    input('Press a key to close this program!')
    exit()

print('Downloading arcdps.ini ...')
urllib.request.urlretrieve('https://www.deltaconnected.com/arcdps/x64/arcdps.ini', 'addons\\arcdps\\arcdps.ini')
print('Downloading d3d9.dll ...')
urllib.request.urlretrieve('https://www.deltaconnected.com/arcdps/x64/d3d9.dll', 'bin64\d3d9.dll')
print('Downloading d3d9_arcdps_buildtemplates.dll ...')
urllib.request.urlretrieve('https://www.deltaconnected.com/arcdps/x64/buildtemplates/d3d9_arcdps_buildtemplates.dll', 'bin64\d3d9_arcdps_buildtemplates.dll')
print('Downloading d3d9_arcdps_extras.dll ...')
urllib.request.urlretrieve('https://www.deltaconnected.com/arcdps/x64/extras/d3d9_arcdps_extras.dll', 'bin64\d3d9_arcdps_extras.dll')
print('\nARCDPS UPDATED!\n')
input('Press a key to close the program!')
exit()
