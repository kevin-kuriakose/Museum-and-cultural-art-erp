frappe.ui.form.on("Acquisition", {
    refresh(frm) {
        if (frm.doc.docstatus === 1 && frm.doc.purchase_order) {
            frm.add_custom_button(__("View Purchase Order"), () => {
                frappe.set_route("Form", "Purchase Order", frm.doc.purchase_order);
            });
        }
    },
    acquisition_type(frm) {
        if (frm.doc.acquisition_type === "Gift" || frm.doc.acquisition_type === "Bequest") {
            frappe.msgprint(__("For gifts/bequests, no Purchase Order will be created in ERPNext."), "Info");
        }
    }
});
