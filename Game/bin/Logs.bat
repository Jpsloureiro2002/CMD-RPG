cd ..
for /f %%I in ('wmic os get localdatetime ^|find "20"') do set dt=%%I
REM
set dt=%dt:~4,2%-%dt:~6,2%-%dt:~0,4%
TITLE LOGS%dt%
python logs.py
pause
