# -*- coding: utf-8 -*-
{
    'name': 'elearning_teacher',
    'description': 'Módulo que agrega Profesores',
    'author': 'Comunidad Odoo Misiones',
    'depends': ['base','website_slides'],
    'application': True,
    'data': ['views/slideChannel_view.xml',
            'security/security.xml',
            'security/ir.model.access.csv']
}
