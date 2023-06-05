# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "AB Custom MRP",
    "summary": "",
    "version": "14.0.1.0.0",
    "category": "Manufacturing",
    "author": "Serincloud",
    "website": "https://ingenieriacloud.com",
    "license": "AGPL-3",
    "depends": ["mrp_bom_group",
                "web_widget_numeric_step",
                ],
    "data": ["views/mrp_view.xml",
             "views/product_views.xml",
             "views/res_company_views.xml",
             "data/default_rules.xml",
#             "views/label_production_view_pdf.xml"
             ],
    "installable": True,
}
