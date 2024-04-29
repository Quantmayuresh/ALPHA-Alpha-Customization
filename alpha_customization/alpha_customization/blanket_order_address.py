import frappe
from frappe.contacts.doctype.address.address import get_address_display


@frappe.whitelist()
def get_address_for_blanket_order(party_type , party):
    parent = frappe.db.sql("""
                SELECT b.parent 
                FROM `tabAddress` a
                LEFT JOIN `tabDynamic Link` b ON a.name = b.parent
                WHERE b.parenttype = 'Address' AND b.link_doctype = %s AND b.link_name = %s AND a.disabled = 0
                LIMIT 1
            """,(party_type ,party),as_dict="True")

    if parent :
        address = parent[0]['parent']
        address_doc = frappe.get_doc("Address", address).as_dict()
        address_display = get_address_display(address_doc)

        return  address,address_display

    else :
        return frappe.msgprint('This Party Do Not Have any Address Linked')
    


@frappe.whitelist()
def get_display_address_for_blanket_order(address_id):

    add_doc = frappe.get_doc("Address", address_id).as_dict()
    add_display = get_address_display(add_doc)

    return add_display


@frappe.whitelist()
def ItemWeight(item_code):
    item_weight = frappe.get_value('Production UOM Definition',{'parent': item_code ,'uom':'Kg'}, "value_per_unit")
    return item_weight if item_weight else 0

@frappe.whitelist()
def get_name_of_party(party):
    if party:
        party_name = frappe.get_value('Supplier', party,'supplier_name')
        if not party_name:
            party_name = frappe.get_value('Customer', party,'customer_name')
        
        return party_name
    else:
        return None

        
