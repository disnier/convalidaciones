# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """
        Convalidaciones para un instituto marlon falcon""",

    'description': """
        Convalidaciones para un centros de estudios
    """,

    'author': "Disoft SA",
    'website': "http://www.disoftsa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
       # 'views/views.xml',
        'views/alumnos.xml',
        'views/modulos.xml',
        'views/ciclos.xml',
        'views/custums.xml',
        'views/convalidaciones.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
     'demo': [
       'demo/demo.xml',
    ],
}