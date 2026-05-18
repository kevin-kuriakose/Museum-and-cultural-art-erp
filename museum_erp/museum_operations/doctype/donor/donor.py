import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Donor(Document):
    def on_update(self):
        # Update cumulative giving from Donations
        total = frappe.db.sql("""
            SELECT SUM(amount) FROM `tabDonation`
            WHERE donor = %s AND docstatus = 1
        """, self.name)[0][0] or 0
        frappe.db.set_value("Donor", self.name, "cumulative_giving", flt(total))

    def _update_giving_level(self, total):
        level = "Friend"
        if flt(total) >= 1000000:
            level = "Major Donor"
        elif flt(total) >= 500000:
            level = "Benefactor"
        elif flt(total) >= 100000:
            level = "Patron"
        elif flt(total) >= 25000:
            level = "Supporter"
        frappe.db.set_value("Donor", self.name, "giving_level", level)
