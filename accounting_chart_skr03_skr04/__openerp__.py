# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2013 OpenERP s.a. (<http://openerp.com>).
#    Copyright (C) 2014 copado MEDIA UG (<http://www.copado.de>).
#    Author Mathias Neef <mn[at]copado.de>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Deutschland - better accounting for 7.0',
    'version': '1.0',
    'author': 'copado.de',
    'website': 'http://www.copado.de',
    'category': 'Localization/Account Charts',
    'description': """
Aktuallisierte Version des SKR03 und SKR04 aus der l10n_de.
===========================================================

Actualized german accounting charts SKR03 and SKR04.
    """,
    'depends': ['base', 'account', 'base_iban', 'base_vat', 'account_chart'],
    'demo': [ ],
    'data': [
        'account_tax_skr03.xml',
        'account_types_skr03.xml',
        'account_chart_skr03.xml',
        'account_chart_template_skr03.xml',
        'account_tax_fiscal_position_skr03.xml',
        'account_tax_skr04.xml',
        'account_types_skr04.xml',
        'account_chart_skr04.xml',
        'account_chart_template_skr04.xml',
        'account_tax_fiscal_position_skr04.xml',
        'skr_de_wizard.xml',
    ],
    'installable': True,
    'images': [],
}

