import frappe
from frappe.model.document import Document

class ArtifactLocation(Document):
    def on_submit(self):
        # Update artifact current location
        frappe.db.set_value("Artifact", self.artifact,
            "current_location", f"{self.location_type}: {self.room_gallery or ''}")
        frappe.db.commit()
