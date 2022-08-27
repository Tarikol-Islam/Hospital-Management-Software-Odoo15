# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Employee Management',
    'version': '1.0.0',
    'summary': 'Employee Management System',
    'sequence': -100,
    'description': """HR Employee""",
    'category': 'Human Resources',
    'depends': [
        'hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_type_view.xml',
        'views/hr_probation_period_settings_view.xml',
        'data/schedule.xml',

    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
