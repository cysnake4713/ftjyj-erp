# -*- coding: utf-8 -*-
{
    'name': 'Odoosoft Vote Module',
    'version': '0.2',
    'category': 'odoosoft',
    'complexity': "easy",
    'description': """
Odoosoft Vote Module""",
    'author': 'Matt Cai',
    'website': 'http://odoosoft.com',
    'depends': ['base'],
    'data': [
        'views/config_view.xml',
        'views/register_record_view.xml',
        'views/vote_record_view.xml',

        'views/menu.xml',

    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'demo': [],
    'application': True
}
