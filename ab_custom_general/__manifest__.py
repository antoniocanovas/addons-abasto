{
    'name': 'AB Custom General',
    'version': '14.0.1.0.0',
    'category': '',
    'description': u"""
    Personalizaciones varias AB
""",
    'author': 'Serincloud',
    'depends': [
        'account',
        'ab_custom_picking',
    ],
    'data': [
        'views/res_partner_views.xml',
        'views/pos_category_views.xml',
        'views/product_category_views.xml',
    ],
    'installable': True,
}
