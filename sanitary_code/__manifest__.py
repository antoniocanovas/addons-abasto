# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    Antonio Cánovas antonio.canovas@serincloud.com
##############################################################################

{
    "name": "Sanitary codes",
    "version": "14.0.1.0.0",
    "category": "Project",
    "author": "www.serincloud.com",
    "maintainer": "Antonio Cánovas",
    "website": "www.serincloud.com",
    "license": "AGPL-3",
    "depends": [
        'contacts',
        'product',
        'purchase',
    ],
    "data": [
        'security/ir.model.access.csv',
#        'views/sanitary_code_views.xml',
#        'views/product_template_views.xml',
#        'views/res_partner_views.xml',
    ],
    "installable": True,
}
