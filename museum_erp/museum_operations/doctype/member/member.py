import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate

class Member(Document):
    def validate(self):
        if self.expiry_date and getdate(self.expiry_date) < getdate(today()):
            if self.status == "Active":
                self.status = "Expired"

    def on_submit(self):
        # Create ERPNext Contact if not linked
        if not self.crm_contact and self.contact:
            self._create_contact()

    def _create_contact(self):
        try:
            contact = frappe.get_doc({
                "doctype": "Contact",
                "first_name": self.member_name,
                "status": "Open",
            })
            contact.insert(ignore_permissions=True)
            self.crm_contact = contact.name
            frappe.db.set_value("Member", self.name, "crm_contact", contact.name)
        except Exception as e:
            frappe.log_error(f"Member contact creation failed: {e}")
