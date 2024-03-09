#!/usr/bin/env bash

rm odoo-16-hernad.zip


echo $(date) > odoo-16-hernad/date.txt

zip -r odoo-16-hernad.zip --exclude="./.git/*/*"  \
   --exclude="*/__pycache__/*" \
   --exclude="./__pycache__/*" \
   --exclude="*/*/__pycache__/*"  odoo-16-hernad

echo uklanjam odoo-16-hernad

rm -rf odoo-16-hernad