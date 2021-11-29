{
    'name': 'Product taxed price',
    'version': '14.0.1.0.0',
    'category': '',
    'description': u"""
    Documentar el pvp con IVA en nuevo campo, y que actualice el precio del estándar.
    Al actualizar el precio en el estándar “list_price”, que se actualice el anterior.
""",
    'author': 'Serincloud',
    'depends': [
        'product',
        'base_automation',

    ],
    'data': [
        'data/action_server.xml',
        'views/model_views.xml',
    ],
    'installable': True,
}
