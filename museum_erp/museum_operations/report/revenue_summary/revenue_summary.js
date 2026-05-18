frappe.query_reports["Revenue Summary"] = {
    filters: [{fieldname:"year",label:"Year",fieldtype:"Data","default":frappe.datetime.get_today().substring(0,4)}]
};
