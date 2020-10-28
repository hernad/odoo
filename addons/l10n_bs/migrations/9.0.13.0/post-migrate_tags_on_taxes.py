# -*- coding: utf-8 -*-

import odoo


#def migrate_tags_on_taxes(cr, registry):
#    ''' This is a utiliy function to help migrate the tags of taxes when the localization has been modified on stable version. If
#    called accordingly in a post_init_hooked function, it will reset the tags set on taxes as per their equivalent template.
#
#    Note: This unusual decision has been made in order to help the improvement of VAT reports on version 9.0, to have them more flexible
#    and working out of the box when people are creating/using new taxes.

def migrate(cr, version):
    registry = odoo.registry(cr.dbname)
    from odoo.addons.account.models.chart_template import migrate_tags_on_taxes
    migrate_tags_on_taxes(cr, registry)
