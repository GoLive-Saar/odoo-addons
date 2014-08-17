{
    'name': 'eCommerce German additions',
    'category': 'Website',
    'summary': 'German additions for eCommerce (B2C)',
    'version': '0.1',
    'description': """
German additions for eCommerce (B2C)
==========================

This addon installed necessary additions in accordance with statutory requirements in Germany.

Overview
--------
 - adds terms page
 - adds revocation page
 - adds delivery page
 - adds privacy page
 - adds imprint page
 - adds an easy built-in address snippet to content blocks
 - adds "incl. VAT, plus shipping costs" to every price
 - adds terms and revocation popup on payment site; both are taken from terms and revocation page on the frontend
 
Todo
----
 - add VAT-percentage to every "incl. VAT"
 - translate all into german
 - create a email template which inherits all statutory required informations
 - ...

Contact for questions
---------------------
copado MEDIA UG - Unterdorfstr. 29 - 77948 Friesenheim - Germany - Phone: +49 7821 32725 20 - info@copado.de - http:www.copado.de
        """,
    'author': 'copado MEDIA UG, Mathias Neef',
    'depends': ['website_sale'],
    'data': [
        'views/wsga_views.xml',
        'views/wsga_templates.xml',
        'views/wsga_snippets.xml',
        'data/data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}