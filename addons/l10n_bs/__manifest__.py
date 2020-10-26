# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Author: Ernad Husremovic
# mail:   hernad(AT)bring.out.ba
{
    "name": "Bosna i Hercegovina - Accounting (FBiH 2020)",
    "description": """
Bosnian localisation.
======================

Author: Ernad Husremovic bring.out doo Sarajevo

Description:

Bosnian Chart of Accounts (FBiH ver.2020)

FBiH knjigovodstveni kontni plan za preduzeća za 2020.
Vrste konta
Porezne grupe prema poreznoj prijavi
Porezi PDV obrasca
Ostali porezi
Osnovne fiskalne pozicije


""",
    "version": "10.0",
    "author": "bring.out",
    'category': 'Localization',
    "website": "https://github.com/hernad/odoo",

    'depends': [
        'account',
    ],
    'data': [
        'data/l10n_bs_chart_data.xml',
        'data/account.account.type.csv',
        'data/account.account.template.csv',
        'data/account_chart_tag_data.xml',
        'data/account.tax.template.csv',
        'data/account_tax_fiscal_position_data.xml',
        'data/account_chart_template_data.yml',
    ],
    "active": False,
}
