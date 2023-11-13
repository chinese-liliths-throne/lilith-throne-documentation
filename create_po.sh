#!/bin/bash

cd ./docs
rm -r ./locale
./make.bat gettext
sphinx-intl update -p _build/gettext -l zh 