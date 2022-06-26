# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'summary': 'Hospital Management System',
    'sequence': -100,
    'description': """Hospital management system""",
    'category': 'Hospital',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
