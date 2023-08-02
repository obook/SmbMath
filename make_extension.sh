#!/bin/sh
EXTENSION="smbmath.oxt"
rm -f $EXTENSION
cd src/
zip -r ../$EXTENSION *
