echo@off
mkdir -p Z:\logs\
robocopy D:\ Z:\ /mir /R:2 /W:3 /LOG+:"Z:\logs\database_cloning.log" /TEE /NDL
pause
