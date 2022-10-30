# -*- coding: utf-8 -*-

{
    'name': "Configuration Manager",
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Configuration Manager in Settings',
    'description': """
        Used to define all API Keys/Passwords/Paths.
    """,
    'author': "Ajay",
    'website': "https://www.youngman.co.in/",
    'sequence': -100,

    'depends': ['base'],

    'data': [
        'views/views.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
