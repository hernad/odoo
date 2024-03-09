#!/usr/bin/env bash

rm -rf odoo-16-hernad
mkdir -p odoo-16-hernad/

~/odoonix/python311 setup.py install --home odoo-tmp

cp -av addons/* odoo-tmp/lib/python/odoo-16.0-py3.11.egg/odoo/addons/

mv odoo-tmp/lib/python/odoo-16.0-py3.11.egg/odoo/ odoo-16-hernad/


cp -r CONTRIBUTING.md  debian  doc  requirements.txt  \
   SECURITY.md  setup.cfg COPYRIGHT LICENSE  odoo.egg-info  README.md setup  setup.py odoo-16-hernad/




