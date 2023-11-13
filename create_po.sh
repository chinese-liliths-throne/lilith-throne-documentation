#!/bin/bash

cd ./docs
./make.bat gettext
sphinx-intl update -p _build/gettext -l zh 