import frappe
from frappe.model.document import Document

class Loan(Document):
    def on_submit(self):
        self.status = "Active"
        for item in self.artifacts or []:
            if item.artifact:
                frappe.db.set_value("Artifact", item.artifact, "status", "On Loan")
        frappe.db.commit()

    def on_cancel(self):
        self.status = "Returned"
        for item in self.artifacts or []:
            if item.artifact:
                frappe.db.set_value("Artifact", item.artifact, "status", "Active")
        frappe.db.commit()
