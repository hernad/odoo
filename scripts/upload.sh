#!/usr/bin/env bash

ssh root@download.svc.bring.out.ba mv /data/download/odoo-16-hernad.zip /data/download/odoo-16-hernad-old.zip 

scp odoo-16-hernad.zip root@download.svc.bring.out.ba:/data/download/

ssh root@download.svc.bring.out.ba ls -lh /data/download/

