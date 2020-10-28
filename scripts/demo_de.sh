#DELETE FROM ir_translation WHERE lang = 'bs_BA'

python2 odoo-bin --db_host=127.0.0.1 -r odoo -w test01 --addons-path=addons,custom/contract -d odoo10de -l bs_BA --load-language bs_BA \
           --without-demo=all 
