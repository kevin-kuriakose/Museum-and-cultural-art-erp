import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("SKU"), "fieldname": "sku", "fieldtype": "Data", "width": 120},
        {"label": _("Item"), "fieldname": "item_name", "fieldtype": "Data", "width": 200},
        {"label": _("Category"), "fieldname": "category", "fieldtype": "Data", "width": 150},
        {"label": _("Stock"), "fieldname": "stock_quantity", "fieldtype": "Int", "width": 80},
        {"label": _("Reorder Level"), "fieldname": "reorder_level", "fieldtype": "Int", "width": 110},
        {"label": _("Price (Rs)"), "fieldname": "unit_price", "fieldtype": "Currency", "width": 110},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 90},
        {"label": _("Alert"), "fieldname": "alert", "fieldtype": "Data", "width": 120},
    ]
    items = frappe.get_all("Shop Item",
        fields=["sku","item_name","category","stock_quantity",
                "reorder_level","unit_price","status"])
    data = []
    for item in items:
        alert = ""
        if flt(item.stock_quantity) <= flt(item.reorder_level):
            alert = "⚠️ Below Reorder"
        if flt(item.stock_quantity) == 0:
            alert = "❌ Out of Stock"
        data.append({**item, "alert": alert})
    data.sort(key=lambda x: (x["alert"] == "", flt(x.get("stock_quantity", 0))))
    return columns, data
