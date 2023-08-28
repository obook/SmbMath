echo on
set EXTENSION="smbmath_win64.oxt"
del /Q %EXTENSION%
cd /D src/
zip -r ../%EXTENSION% *
