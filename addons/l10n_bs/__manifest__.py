# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Author: Ernad Husremovic
# mail:   hernad@bring.out.ba
{
    "name": "Bosna i Hercegovina",
    "description": """
Bosnian localisation.
======================

Author: Ernad Husremovic bring.out doo Sarajevo

Description:

Bosnian accounting


""",
    "version": "10.0.3",
    "author": "bring.out",
    'category': 'Localization',
    "website": "https://github.com/hernad/odoo",

    'depends': [
        'account',
    ],
    'data': [
        'data/account_account_tags_data.xml',
        'data/account_account_types_data.xml',
        'data/bs_menu_data.xml',
        'data/res.country.state.csv',
    ],
    "active": False,
}
