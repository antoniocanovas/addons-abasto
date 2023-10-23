# Copyright 2021 IC - Javier Muñoz Conesa
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
        'ab_custom_mrp',
        'mrp',
    ],
    "data": [
        'data/paper_format.xml',
        'views/label_production_view_pdf.xml',
        'views/report_simple_barcode.xml',
        'views/small_label_production_view.xml',
        'views/double_label_production_view.xml',


    ],
    "installable": True,
}
