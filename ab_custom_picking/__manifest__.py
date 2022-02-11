{
    'name': 'AB Custom Picking',
    'version': '14.0.1.0.0',
    'category': '',
    'description': u"""
    Documentar el pvp con IVA en nuevo campo, y que actualice el precio del estándar.
    Al actualizar el precio en el estándar “list_price”, que se actualice el anterior.
""",
    'author': 'Serincloud',
    'depends': [
        'purchase',
        'stock_picking_back2draft',
        'stock_delivery_note',
        'stock_picking_invoice_link',
        'stock_picking_purchase_order_link',
        'stock_picking_sale_order_link',
        'stock_picking_send_by_mail',
        'stock_picking_warn_message',
        #'purchase_stock_picking_invoice_link ',

    ],
    'data': [
        'data/action_server.xml',
        'views/model_views.xml',
    ],
    'installable': True,
}
