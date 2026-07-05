# -*- coding: utf-8 -*-
{
    'name': "Odoo Accounting Filters",
    'summary': """Odoo Accounting Filters.""",
    'description': """Odoo Accounting Filters.""",
    'category': 'Accounting',
    'author': 'Mitchel Admin',
    'company': 'Mitchel Admin',
    'maintainer': 'erpmitchellodoo@gmail.com',
    'version': '17.0.1.1.1',
    'price':'00.00',
    'currency':'USD',
    'depends': ['account_accountant','account_reports'],
    'data': [
       'views/account_report_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_accounting_filters/static/src/xml/filters.xml',
        ],

    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,

}
