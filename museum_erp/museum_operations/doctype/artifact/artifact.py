import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt

class Artifact(Document):
    def validate(self):
        if flt(self.insurance_value) < 0:
            frappe.throw(_("Insurance value cannot be negative"))
        if self.condition == "Critical":
            frappe.msgprint(
                _("⚠️ Artifact condition is CRITICAL — please raise a Conservation Record"),
                alert=True, indicator="red")

    def on_update(self):
        # Sync condition to ERPNext Item if linked
        if self.linked_item:
            frappe.db.set_value("Item", self.linked_item,
                "description", f"{self.title} | Condition: {self.condition}")
