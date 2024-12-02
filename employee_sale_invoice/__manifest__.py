# -*- coding: utf-8 -*-

{
    'name': "Employee Sale Invoice",
    'author': "THECH ERP",
    'category': 'Human Resources',
    'summary': """Display the number of quotations and sales order quickly on the Employee""",
    'description': """""",
    'version': '18.0.1.0.0',
    'depends': [
        'hr',
        'sale_management',
        'account',
        'sale',
        'contacts'
    ],
    'data': [
        'views/account_move.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
