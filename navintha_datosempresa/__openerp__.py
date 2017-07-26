# -*- coding: utf-8 -*-
{
    'name': "Navintha - perfil de compañia",

    'summary': """
        Datos de la compañia""",

    'description': """
        Modulo para guardar los datos de la compañia
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'views/navintha_profile_view.xml',
        'views/navintha_actions.xml',
    ],
    'installable':True,
    'auto_install':False,
}

