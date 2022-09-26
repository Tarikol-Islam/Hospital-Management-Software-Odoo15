#-*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Contract',
    'category': 'Human Resources',
    'sequence': 39,
    'summary': '',
    'description': "",
    'installable': True,
    'depends': [
        'hr_contract',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_contract_view.xml',
        'views/templates.xml',
        'views/res_config_settings_views.xml'
    ],
    'demo': [
    ],

    'license': 'LGPL-3',
}
