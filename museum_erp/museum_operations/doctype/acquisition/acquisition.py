import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

class Acquisition(Document):
    def validate(self):
        total = sum(flt(item.estimated_value) for item in self.items or [])
        if not self.total_value:
            self.total_value = total

    def on_submit(self):
        self.status = "Accessioned"
        for item in self.items or []:
            if item.artifact:
                frappe.db.set_value("Artifact", item.artifact,
                    "acquisition_date", self.acquisition_date)
        frappe.db.commit()
        # Create ERPNext Purchase Order for purchases
        if self.acquisition_type == "Purchase" and not self.purchase_order:
            self._create_purchase_order()

    def _create_purchase_order(self):
        try:
            company = frappe.defaults.get_user_default("Company")
            if not company:
                return
            po = frappe.get_doc({
                "doctype": "Purchase Order",
                "supplier": self.source_name,
                "company": company,
                "schedule_date": self.acquisition_date,
                "items": [{
                    "item_code": item.artifact or "Museum Acquisition",
                    "qty": 1,
                    "rate": flt(item.estimated_value),
                    "uom": "Nos",
                } for item in self.items if item.estimated_value],
            })
            po.insert(ignore_permissions=True)
            self.purchase_order = po.name
            frappe.db.set_value("Acquisition", self.name,
                "purchase_order", po.name)
            frappe.db.commit()
            print(f"  Created PO: {po.name}")
        except Exception as e:
            frappe.log_error(f"Acquisition PO creation failed: {e}")
