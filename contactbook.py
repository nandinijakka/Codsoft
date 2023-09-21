import tkinter as tk
from tkinter import messagebox

# Dictionary to store contacts
contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning('Error', 'Name and Phone are required fields.')

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def search_contact():
    search_name = search_entry.get()
    if search_name in contacts:
        clear_entries()
        name_entry.insert(0, search_name)
        phone_entry.insert(0, contacts[search_name]['Phone'])
        email_entry.insert(0, contacts[search_name]['Email'])
        address_entry.insert(0, contacts[search_name]['Address'])
    else:
        messagebox.showwarning('Contact not found', 'Contact not found in the list.')

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        clear_entries()
        update_contact_list()
    else:
        messagebox.showwarning('Contact not found', 'Contact not found in the list.')

# Create the main application window
root = tk.Tk()
root.title("Contact Management System")

# Create labels and entry fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

search_label = tk.Label(root, text="Search Name:")
search_label.grid(row=5, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1, padx=10, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Listbox to display contacts
contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=0, column=2, rowspan=8, padx=10, pady=5)
update_contact_list()

root.mainloop()
