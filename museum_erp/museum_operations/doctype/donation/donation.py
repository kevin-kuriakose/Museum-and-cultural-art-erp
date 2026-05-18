import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Donation(Document):
    def on_submit(self):
        # Update donor cumulative giving
        if self.donor:
            total = frappe.db.sql("""
                SELECT SUM(amount) FROM `tabDonation`
                WHERE donor = %s AND docstatus = 1
            """, self.donor)[0][0] or 0
            frappe.db.set_value("Donor", self.donor,
                "cumulative_giving", flt(total))
            frappe.db.set_value("Donor", self.donor,
                "last_gift_date", self.donation_date)
        # Create Payment Entry
        if not self.payment_entry:
            self._create_payment_entry()

    def _create_payment_entry(self):
        try:
            company = frappe.defaults.get_user_default("Company")
            if not company:
                return
            pe = frappe.get_doc({
                "doctype": "Payment Entry",
                "payment_type": "Receive",
                "party_type": "Customer",
                "party": self.donor,
                "paid_amount": flt(self.amount),
                "received_amount": flt(self.amount),
                "company": company,
                "posting_date": self.donation_date,
                "reference_no": self.name,
                "reference_date": self.donation_date,
            })
            pe.insert(ignore_permissions=True)
            self.payment_entry = pe.name
            frappe.db.set_value("Donation", self.name,
                "payment_entry", pe.name)
        except Exception as e:
            frappe.log_error(f"Donation payment entry failed: {e}")
