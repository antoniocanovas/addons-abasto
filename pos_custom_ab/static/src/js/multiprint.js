odoo.define('pos_custom_ab.multiprint', function (require) {
"use strict";

var multi = require('pos_line_category_order.multiprint');
var core = require('web.core');
var models = require('point_of_sale.models');
var Printer = require('point_of_sale.Printer').Printer;
var QWeb = core.qweb;

var _super_order = models.Order.prototype;
models.Order = models.Order.extend({

    computeChanges: function(categories){
        var order = _super_order.computeChanges.call(this,categories)
        var json        = this.export_as_JSON();
        if (json.ms_info['changed']) {
          order['waiter'] = json.ms_info['changed']['user']['name'];
        }else if(json.ms_info['created']){
          order['waiter'] = json.ms_info['created']['user']['name'];
        }else {
           order['waiter'] = "";
        }
        return order
    },

});

});
