# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'palette traching',
    'summary': '',
    'description': """""",
    'author': 'company',
    'website': '',
    'category': 'Test',
    'version': '1.1',
    'depends' : [ 'base', 'sale', 'sale_management', 'stock', 'sale_stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/Palette_tracking.xml',
    ],
    'demo': [
        'demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
