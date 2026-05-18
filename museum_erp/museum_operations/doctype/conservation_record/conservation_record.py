import frappe
from frappe.model.document import Document
from frappe.utils import flt

class ConservationRecord(Document):
    def on_update(self):
        if self.condition_rating == "Critical" and self.priority != "Urgent":
            self.priority = "Urgent"
        if self.status == "Completed" and self.artifact:
            frappe.db.set_value("Artifact", self.artifact,
                "condition", self.condition_rating)
            frappe.db.commit()
        # Auto-create ERPNext Project if not linked
        if not self.project and self.artifact:
            self._create_project()

    def _create_project(self):
        try:
            proj = frappe.get_doc({
                "doctype": "Project",
                "project_name": f"Conservation: {self.artifact}",
                "status": "Open",
                "expected_start_date": self.examination_date,
                "museum_exhibition_ref": None,
            })
            proj.insert(ignore_permissions=True)
            self.project = proj.name
            frappe.db.set_value("Conservation Record", self.name,
                "project", proj.name)
        except Exception as e:
            frappe.log_error(f"Conservation project creation failed: {e}")
