#DELETE FROM ir_translation WHERE lang = 'bs_BA'

PATHS=custom/account-fiscal-rule,custom/report,custom/muk_web,custom/partner-contact,custom/web,custom/server-tools,custom/mis-builder,bosnia/l10n-bosnia
PATHS=$PATHS,custom/account-financial-tools

python2 odoo-bin --db_host=127.0.0.1 -r odoo -w test01 \
           --addons-path=addons,custom/contract,$PATHS \
           -d odoo10de -l bs_BA --load-language bs_BA \
           --without-demo=all \
           --dev=all

#https://www.odoo.com/forum/help-1/question/exception-bus-bus-unavailable-odoo-10-124387
#	   -c odoo.conf

#-u all 

#https://www.odoo.com/documentation/10.0/setup/deploy.html

