{
    'name': 'Deutschland - Accounting IKR',
    'version': '1.0',
    'author': 'copado MEDIA',
	'website': 'http://www.copado.de',
    'category': 'Localization/Account Charts',
    'description': """
Dieses Modul beinhaltet den deutschen Kontenrahmen IKR (Industriekontenrahmen) angelehnt an den Schulkontenrahmen der IHK.
==========================================================================================================================
	* Letzte Überarbeitung IKR: 08/2014


English:
German accounting chart and localization (Industry Chart Temlate (IKR)) relating to the school-chart-template of the IHK (Industry and Trade Chamber).
	* Last change IKR: 08/2014

    """,
    'depends': [
		'base',
		'account',
		'base_iban',
		'base_vat',
		'account_chart'
	],
    'demo': [],
    'data': [
        'account_tax_ikr.xml',
        'account_chart_schema_ikr.xml',
        'account_chart_ikr.xml', 					
        'account_chart_template_ikr.xml',			
        'account_tax_fiscal_position_ikr.xml',		
        'chart_ikr_wizard.xml',
    ],
    'installable': True,
    'images': ['images/config_chart_l10n_de.jpeg','images/l10n_de_chart.jpeg'],
}

