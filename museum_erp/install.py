import frappe

def after_install():
    create_custom_fields()
    frappe.db.commit()
    print("✅ MuseumEdge ERP installed")

def create_custom_fields():
    # Link ERPNext Item to Artifact for gift shop
    if not frappe.db.exists("Custom Field", "Item-museum_artifact_ref"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Item",
            "fieldname": "museum_artifact_ref",
            "fieldtype": "Link",
            "options": "Artifact",
            "label": "Museum Artifact Reference",
            "insert_after": "item_name",
            "module": "Museum Operations",
        }).insert(ignore_permissions=True)

    # Link ERPNext Project to Exhibition
    if not frappe.db.exists("Custom Field", "Project-museum_exhibition_ref"):
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Project",
            "fieldname": "museum_exhibition_ref",
            "fieldtype": "Link",
            "options": "Exhibition",
            "label": "Museum Exhibition Reference",
            "insert_after": "project_name",
            "module": "Museum Operations",
        }).insert(ignore_permissions=True)

    frappe.db.commit()
