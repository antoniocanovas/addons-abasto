# Copyright 2021 IC - Javier Muñoz Conesa, Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports Abasto",
    "summary": "Reports Abasto",
    "version": "14.0.0.0.0",
    "category": "Reports",
    "author": "SerinCloud",
    "website": "https://www.ingeniriacloud.com",
    "license": "AGPL-3",
    "depends": [
        'pos_restaurant',
        'ab_custom_mrp',
        'mrp',
    ],
    "data": [
        'views/pos_custom_templates.xml',
        'views/label_production_view_pdf.xml',
        'views/report_simple_barcode.xml',
        'views/small_label_production_view.xml',
        'views/double_label_production_view.xml',
        'data/paper_format.xml',
    ],
    "qweb": [
            "static/src/xml/multiprint.xml",
        ],
    "installable": True,
}
