import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Ticket(Document):
    def validate(self):
        self.total_price = (flt(self.unit_price) * flt(self.quantity or 1)) - flt(self.discount_applied)

    def on_submit(self):
        if not self.sales_invoice:
            self._create_sales_invoice()

    def _create_sales_invoice(self):
        try:
            company = frappe.defaults.get_user_default("Company")
            if not company:
                return
            si = frappe.get_doc({
                "doctype": "Sales Invoice",
                "customer": self.visitor_name or "Museum Walk-in",
                "company": company,
                "posting_date": self.visit_date,
                "items": [{
                    "item_name": f"Ticket: {self.ticket_type}",
                    "qty": flt(self.quantity or 1),
                    "rate": flt(self.unit_price),
                    "uom": "Nos",
                }]
            })
            si.insert(ignore_permissions=True)
            self.sales_invoice = si.name
            frappe.db.set_value("Ticket", self.name, "sales_invoice", si.name)
        except Exception as e:
            frappe.log_error(f"Ticket invoice creation failed: {e}")
