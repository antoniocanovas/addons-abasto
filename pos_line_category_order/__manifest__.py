# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

{
    "name": "POS line category order",
    "summary": "sort receipt lines by category.",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/pos",
    "category": "Point of Sale",
    "maintainers": ["pedroguirao"],
    "version": "14.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["pos_restaurant","skit_pos_restaurant",],
    "data": [
        "views/assets.xml",
             ],
    "qweb": [
        "static/src/xml/multiprint.xml",
             ],
}
