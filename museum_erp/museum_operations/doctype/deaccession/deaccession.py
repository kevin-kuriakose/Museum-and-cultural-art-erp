import frappe
from frappe import _
from frappe.model.document import Document

class Deaccession(Document):
    def on_submit(self):
        self.status = "Completed"
        frappe.db.set_value("Artifact", self.artifact, "status", "Deaccessioned")
        frappe.db.commit()
