import frappe
from frappe.model.document import Document
from frappe.utils import flt, add_years

class MembershipRenewal(Document):
    def on_submit(self):
        if self.member and self.new_expiry_date:
            frappe.db.set_value("Member", self.member, {
                "expiry_date": self.new_expiry_date,
                "membership_tier": self.renewed_tier,
                "status": "Active",
            })
            frappe.db.commit()
