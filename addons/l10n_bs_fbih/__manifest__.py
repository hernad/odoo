# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Author: Ernad Husremovic
# mail:   hernad@bring.out.ba
{
    "name": "Bosna i Hercegovina / FBiH 2020",
    "description": """BiH, kontni plan FBiH

Author: Ernad Husremovic bring.out doo Sarajevo

Description:

Bosnian Chart of Accounts (FBiH ver.2020)


""",
    "version": "10.0.3",
    "author": "bring.out",
    'category': 'Localization',
    "website": "https://github.com/hernad/odoo",

    'depends': [
        'l10n_bs',
    ],
    'data': [
        'data/l10n_bs_fbih_chart_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_tag_data.xml',
        'data/account.tax.template.csv',
        'data/account_tax_fiscal_position_data.xml',
        'data/account_chart_template_data.yml',
        'data/account_updates_data.xml'
    ],
    "active": False,
}
