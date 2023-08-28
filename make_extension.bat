echo on
set EXTENSION="smbmath.oxt"
del /Q %EXTENSION%
cd /D src/
zip -r ../%EXTENSION% *
cd ..
