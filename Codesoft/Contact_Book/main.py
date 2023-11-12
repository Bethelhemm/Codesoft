import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def update_contact(self, contact, name, phone_number, email, address):
        contact.name = name
        contact.phone_number = phone_number
        contact.email = email
        contact.address = address

    def search_contacts(self, search_term):
        search_results = []
        for contact in self.contacts:
            if (
                search_term.lower() in contact.name.lower() or
                search_term in contact.phone_number
            ):
                search_results.append(contact)
        return search_results

    def get_contact_list(self):
        return self.contacts

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    contact = Contact(name, phone_number, email, address)
    contact_manager.add_contact(contact)

    messagebox.showinfo("Success", "Contact added successfully.")
    clear_fields()

def search_contact():
    search_term = search_entry.get()
    search_results = contact_manager.search_contacts(search_term)

    contact_list.delete(0, tk.END)
    for contact in search_results:
        contact_list.insert(tk.END, f"{contact.name}, {contact.phone_number}")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contact_manager.get_contact_list()[selected_index[0]]
        contact_manager.delete_contact(selected_contact)
        contact_list.delete(selected_index)
        messagebox.showinfo("Success", "Contact deleted successfully.")

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contact_manager.get_contact_list()[selected_index[0]]
        update_window = tk.Toplevel(root)

        name_label = tk.Label(update_window, text="Name:")
        name_label.grid(row=0, column=0)
        name_entry = tk.Entry(update_window)
        name_entry.grid(row=0, column=1)
        name_entry.insert(tk.END, selected_contact.name)

        phone_label = tk.Label(update_window, text="Phone Number:")
        phone_label.grid(row=1, column=0)
        phone_entry = tk.Entry(update_window)
        phone_entry.grid(row=1, column=1)
        phone_entry.insert(tk.END, selected_contact.phone_number)

        email_label = tk.Label(update_window, text="Email:")
        email_label.grid(row=2, column=0)
        email_entry = tk.Entry(update_window)
        email_entry.grid(row=2, column=1)
        email_entry.insert(tk.END, selected_contact.email)

        address_label = tk.Label(update_window, text="Address:")
        address_label.grid(row=3, column=0)
        address_entry = tk.Entry(update_window)
        address_entry.grid(row=3, column=1)
        address_entry.insert(tk.END, selected_contact.address)

        update_button = tk.Button(update_window, text="Update", command=lambda: update_selected_contact(selected_contact))
        update_button.grid(row=4, column=0, columnspan=2)

def update_selected_contact(contact):
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    contact_manager.update_contact(contact, name, phone_number, email, address)
    messagebox.showinfo("Success", "Contact updated successfully.")
    update_window.destroy()
    refresh_contact_list()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contact_manager.get_contact_list():
        contact_list.insert(tk.END, f"{contact.name}, {contact.phone_number}")

contact_manager = ContactManager()

root = tk.Tk()
root.title("Contact Manager")

# Add Contact Frame
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

name_label = tk.Label(add_frame, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(add_frame, text="Phone Number:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(add_frame)
phone_entry.grid(row=1, column=1)
email_label = tk.Label(add_frame, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=2, column=1)

address_label = tk.Label(add_frame, text="Address:")
address_label.grid(row=3, column=0)
address_entry = tk.Entry(add_frame)
address_entry.grid(row=3, column=1)

add_button = tk.Button(add_frame, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2)

# Contact List Frame
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

search_label = tk.Label(list_frame, text="Search:")
search_label.grid(row=0, column=0)
search_entry = tk.Entry(list_frame)
search_entry.grid(row=0, column=1)

search_button = tk.Button(list_frame, text="Search", command=search_contact)
search_button.grid(row=0, column=2)

contact_list = tk.Listbox(list_frame, width=50)
contact_list.grid(row=1, column=0, columnspan=3, pady=10)

delete_button = tk.Button(list_frame, text="Delete Contact", command=delete_contact)
delete_button.grid(row=2, column=0)

update_button = tk.Button(list_frame, text="Update Contact", command=update_contact)
update_button.grid(row=2, column=1)

refresh_contact_list()

root.mainloop()