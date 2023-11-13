#!/bin/bash

cd ./docs
rm -r ./locale
sphinx-build -M gettext . _build
sphinx-intl update -p _build/gettext -l zh 