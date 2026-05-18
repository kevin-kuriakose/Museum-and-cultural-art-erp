import frappe
from frappe.model.document import Document
from frappe.utils import flt

class Exhibition(Document):
    def validate(self):
        if self.end_date and self.start_date:
            if self.end_date < self.start_date:
                frappe.throw("End date cannot be before start date")

    def on_submit(self):
        self.status = "Open"
        if not self.project:
            self._create_project()

    def _create_project(self):
        try:
            proj = frappe.get_doc({
                "doctype": "Project",
                "project_name": f"Exhibition: {self.title}",
                "status": "Open",
                "expected_start_date": self.start_date,
                "expected_end_date": self.end_date,
                "estimated_costing": flt(self.budget),
            })
            proj.insert(ignore_permissions=True)
            self.project = proj.name
            frappe.db.set_value("Exhibition", self.name, "project", proj.name)
        except Exception as e:
            frappe.log_error(f"Exhibition project creation failed: {e}")
