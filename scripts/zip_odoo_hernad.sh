#!/usr/bin/env bash

ODOO=odoo-16-hernad

rm -rf $ODOO
mkdir -p $ODOO/

~/odoonix/python311 setup.py install --home odoo-tmp

cp -av addons/* odoo-tmp/lib/python/odoo-16.0-py3.11.egg/odoo/addons/

echo === create $ODOO dir ======
mv odoo-tmp/lib/python/odoo-16.0-py3.11.egg/odoo/ $ODOO/


cp -r CONTRIBUTING.md  debian  doc  requirements.txt  \
   SECURITY.md  setup.cfg COPYRIGHT LICENSE  odoo.egg-info  README.md setup  setup.py $ODOO/

rm $ODOO.zip


echo $(date) > $ODOO/date.txt

echo ==== create zip $ODOO.zip ==========================

zip -r $ODOO.zip --exclude="./.git/*/*"  \
   --exclude="*/__pycache__/*" \
   --exclude="./__pycache__/*" \
   --exclude="*/*/__pycache__/*"  $ODOO


echo uklanjam $ODOO

rm -rf $ODOO