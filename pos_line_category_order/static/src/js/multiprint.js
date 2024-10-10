odoo.define('pos_line_category_order.multiprint', function (require) {
"use strict";

var models = require('point_of_sale.models');
var core = require('web.core');
var Printer = require('point_of_sale.Printer').Printer;
var multi = require('pos_restaurant.multiprint');

var QWeb = core.qweb;


var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
    build_line_resume: function(){
        var resume = {};
        this.orderlines.each(function(line){
            if (line.mp_skip) {
                return;
            }
            var qty  = Number(line.get_quantity());
            var note = line.get_note();
            var product_id = line.get_product().id;
            var product_name = line.get_full_product_name();
            var p_key = product_id + " - " + product_name;
            var product_resume = p_key in resume ? resume[p_key] : {
                pid: product_id,
                product_name_wrapped: line.generate_wrapped_product_name(),
                qties: {},
            };
            if (note in product_resume['qties']) product_resume['qties'][note] += qty;
            else product_resume['qties'][note] = qty;
            resume[p_key] = product_resume;

        });
        return resume;
    },
    computeChanges: function(categories){
        var current_res = this.build_line_resume();
        var old_res     = this.saved_resume || {};
        var json        = this.export_as_JSON();
        var add = [];
        var rem = [];
        var p_key, note;

        for (p_key in current_res) {

            for (note in current_res[p_key]['qties']) {
                var curr = current_res[p_key];
                var old  = old_res[p_key] || {};
                var pid = curr.pid;
                var found = p_key in old_res && note in old_res[p_key]['qties'];
                 if (this.pos.db.get_product_by_id(pid)){
                      var categ_parts = this.pos.db.get_product_by_id(pid).categ_id['1'].split("/");
                      var final_categ = categ_parts[categ_parts.length - 1].replace(/\s/g,'');
                    }

                if (!found) {
                    add.push({
                        'id':       pid,
                        'name':     this.pos.db.get_product_by_id(pid).display_name,
                        'categ':    final_categ || false,
                        'name_wrapped': curr.product_name_wrapped,
                        'note':     note,
                        'qty':      curr['qties'][note],
                    });
                } else if (old['qties'][note] < curr['qties'][note]) {
                    add.push({
                        'id':       pid,
                        'name':     this.pos.db.get_product_by_id(pid).display_name,
                        'categ':    final_categ || false,
                        'name_wrapped': curr.product_name_wrapped,
                        'note':     note,
                        'qty':      curr['qties'][note] - old['qties'][note],
                    });
                } else if (old['qties'][note] > curr['qties'][note]) {
                    rem.push({
                        'id':       pid,
                        'name':     this.pos.db.get_product_by_id(pid).display_name,
                        'categ':    final_categ || false,
                        'name_wrapped': curr.product_name_wrapped,
                        'note':     note,
                        'qty':      old['qties'][note] - curr['qties'][note],
                    });
                }
            }
        }

        for (p_key in old_res) {
            for (note in old_res[p_key]['qties']) {
                var found = p_key in current_res && note in current_res[p_key]['qties'];
                if (!found) {
                     if (this.pos.db.get_product_by_id(pid)){
                      var categ_parts = this.pos.db.get_product_by_id(pid).categ_id['1'].split("/");
                      var final_categ = categ_parts[categ_parts.length - 1].replace(/\s/g,'');
                    }
                    var old = old_res[p_key];
                    var pid = old.pid;
                    rem.push({
                        'id':       pid,
                        'name':     this.pos.db.get_product_by_id(pid).display_name,
                        'categ':    final_categ || false,
                        'name_wrapped': old.product_name_wrapped,
                        'note':     note,
                        'qty':      old['qties'][note],
                    });
                }
            }
        }

        if(categories && categories.length > 0){
            // filter the added and removed orders to only contains
            // products that belong to one of the  supplied as a parameter

            var self = this;

            var _add = [];
            var _rem = [];

            for(var i = 0; i < add.length; i++){
                if(self.pos.db.is_product_in_category(categories,add[i].id)){
                    _add.push(add[i]);
                }
            }
            add = _add.sort(function(a,b){
                if(a.categ < b.categ) { return -1; }
                if(a.categ > b.categ) { return 1; }
                return 0;
            });
            for(var i = 0; i < rem.length; i++){
                if(self.pos.db.is_product_in_category(categories,rem[i].id)){
                    _rem.push(rem[i]);
                }
            }
            rem = _rem.sort(function(a,b){
                if(a.categ < b.categ) { return -1; }
                if(a.categ > b.categ) { return 1; }
                return 0;
            });
        }

        var d = new Date();
        var hours   = '' + d.getHours();
            hours   = hours.length < 2 ? ('0' + hours) : hours;
        var minutes = '' + d.getMinutes();
            minutes = minutes.length < 2 ? ('0' + minutes) : minutes;

        var j_waiter = ""
         if (json.ms_info['changed']) {
          j_waiter = json.ms_info['changed']['user']['name'];
        }else if(json.ms_info['created']){
          j_waiter = json.ms_info['created']['user']['name'];
        }

        return {
            'new': add,
            'cancelled': rem,
            'waiter': j_waiter,
            'table': json.table || false,
            'floor': json.floor || false,
            'name': json.name  || 'unknown order',
            'time': {
                'hours':   hours,
                'minutes': minutes,
            },
        };

    },
    printChanges: async function(){
        var printers = this.pos.printers;
        let isPrintSuccessful = true;
        for(var i = 0; i < printers.length; i++){
            var changes = this.computeChanges(printers[i].config.product_categories_ids);
            if ( changes['new'].length > 0 || changes['cancelled'].length > 0){
                var receipt = QWeb.render('OrderChangeReceipt',{changes:changes, widget:this});
                const result = await printers[i].print_receipt(receipt);
                if (!result.successful) {
                    isPrintSuccessful = false;
                }
            }
        }
        return isPrintSuccessful;
    },

});


});
