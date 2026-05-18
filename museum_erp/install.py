import frappe

def after_install():
    frappe.db.commit()
    print("✅ MuseumEdge ERP installed")
