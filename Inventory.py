import tkinter as tk
from tkinter import messagebox

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Inventory Management System")
        self.root.geometry("600x400")
        
        # Initialize the inventory as an empty list (data will not persist)
        self.inventory = []

        # Create the GUI components
        self.create_widgets()

    def create_widgets(self):
        # Product Name
        self.name_label = tk.Label(self.root, text="Product Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.product_name = tk.Entry(self.root)
        self.product_name.grid(row=0, column=1, padx=10, pady=5)

        # Product Price
        self.price_label = tk.Label(self.root, text="Price")
        self.price_label.grid(row=1, column=0, padx=10, pady=5)
        self.product_price = tk.Entry(self.root)
        self.product_price.grid(row=1, column=1, padx=10, pady=5)

        # Product Quantity
        self.quantity_label = tk.Label(self.root, text="Quantity")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=5)
        self.product_quantity = tk.Entry(self.root)
        self.product_quantity.grid(row=2, column=1, padx=10, pady=5)

        # Supplier Name
        self.supplier_label = tk.Label(self.root, text="Supplier")
        self.supplier_label.grid(row=3, column=0, padx=10, pady=5)
        self.product_supplier = tk.Entry(self.root)
        self.product_supplier.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=4, column=0, padx=10, pady=5)

        self.update_button = tk.Button(self.root, text="Update Product", command=self.update_product)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=4, column=2, padx=10, pady=5)

        self.search_button = tk.Button(self.root, text="Search Product", command=self.search_product)
        self.search_button.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        # Listbox to display products
        self.product_listbox = tk.Listbox(self.root, width=50, height=10)
        self.product_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        # Load current inventory data into listbox
        self.refresh_inventory()

    def add_product(self):
        # Get product details from user input
        name = self.product_name.get()
        price = self.product_price.get()
        quantity = self.product_quantity.get()
        supplier = self.product_supplier.get()

        if name and price and quantity and supplier:
            # Add the new product to the inventory
            product = {
                "name": name,
                "price": float(price),
                "quantity": int(quantity),
                "supplier": supplier
            }

            self.inventory.append(product)
            self.refresh_inventory()

            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    def update_product(self):
        # Get selected product name from listbox
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            product_name = selected_product.split(" | ")[0]

            # Get new product details
            new_price = self.product_price.get()
            new_quantity = self.product_quantity.get()

            if new_price and new_quantity:
                for product in self.inventory:
                    if product["name"] == product_name:
                        product["price"] = float(new_price)
                        product["quantity"] = int(new_quantity)

                self.refresh_inventory()

                messagebox.showinfo("Success", f"Product '{product_name}' updated successfully!")
            else:
                messagebox.showwarning("Input Error", "Price and quantity are required to update.")
        else:
            messagebox.showwarning("Selection Error", "Please select a product to update.")

    def delete_product(self):
        # Get selected product name from listbox
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            product_name = selected_product.split(" | ")[0]

            self.inventory = [product for product in self.inventory if product["name"] != product_name]
            self.refresh_inventory()

            messagebox.showinfo("Success", f"Product '{product_name}' deleted successfully!")
        else:
            messagebox.showwarning("Selection Error", "Please select a product to delete.")

    def search_product(self):
        search_term = self.product_name.get().lower()
        self.product_listbox.delete(0, tk.END)

        for product in self.inventory:
            if search_term in product["name"].lower():
                self.product_listbox.insert(tk.END, f"{product['name']} | ${product['price']} | {product['quantity']} pcs | {product['supplier']}")

    def refresh_inventory(self):
        # Clear the listbox and populate it with current inventory
        self.product_listbox.delete(0, tk.END)
        for product in self.inventory:
            self.product_listbox.insert(tk.END, f"{product['name']} | ${product['price']} | {product['quantity']} pcs | {product['supplier']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
