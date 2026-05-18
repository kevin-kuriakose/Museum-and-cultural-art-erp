import frappe
from frappe.model.document import Document
from frappe.utils import flt

class ShopSale(Document):
    def validate(self):
        subtotal = sum(flt(i.unit_price) * flt(i.qty) for i in self.items or [])
        for item in self.items or []:
            item.line_total = flt(item.unit_price) * flt(item.qty) - flt(item.discount)
        self.subtotal = subtotal
        self.total = subtotal - flt(self.discount) + flt(self.tax)

    def on_submit(self):
        self.status = "Completed"
        self._update_stock()
        if not self.sales_invoice:
            self._create_invoice()

    def _update_stock(self):
        for item in self.items or []:
            if item.item:
                stock = frappe.db.get_value("Shop Item", item.item, "stock_quantity") or 0
                frappe.db.set_value("Shop Item", item.item,
                    "stock_quantity", max(0, flt(stock) - flt(item.qty)))

    def _create_invoice(self):
        try:
            company = frappe.defaults.get_user_default("Company")
            if not company:
                return
            si = frappe.get_doc({
                "doctype": "Sales Invoice",
                "customer": "Museum Shop Walk-in",
                "company": company,
                "posting_date": self.sale_date,
                "items": [{
                    "item_name": item.item or "Shop Item",
                    "qty": flt(item.qty),
                    "rate": flt(item.unit_price),
                    "uom": "Nos",
                } for item in self.items if item.qty],
            })
            si.insert(ignore_permissions=True)
            self.sales_invoice = si.name
            frappe.db.set_value("Shop Sale", self.name, "sales_invoice", si.name)
        except Exception as e:
            frappe.log_error(f"Shop sale invoice failed: {e}")
