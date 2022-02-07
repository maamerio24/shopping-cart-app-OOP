class Cart:
    def __init__(self, cart = []):
        self.cart = cart
    def add_item(self, add_item):
        if add_item not in self.cart:
            print(f'{add_item.title()} has been added to your cart.')
            return self.cart.append(add_item)
        else:
            print("This item is already in your cart!")
    def remove_item(self, remove_item):
        if remove_item in self.cart:
            self.cart.remove(remove_item)
            print(f'{remove_item.title()} has been removed from your cart.')
        else:
            print("This item is not in your cart!")
    def show(self):
        if len(self.cart) == 0:
            print("There is nothing in your cart.")
        else:
            print("Your shopping cart is:")
            for item in self.cart:
                print("- " + item.title())


def shopping_cart():
    cart = Cart()
    print("Welcome to your cart, lets go shopping!")
    done = False
    while not done:
        response = input(
        "Would you like to add an item (a), remove an item (r), see your cart (s), or leave (l)? ").lower()
        if response == 'a':
            addition = input("What item would you like to add to your cart? ")
            cart.add_item(addition)
        elif response == 'r':
            removal = input("what item would you like to remove from your cart? ")
            cart.remove_item(removal)
        elif response == 's':
            cart.show()
        elif response == 'l':
            print("Thanks for shopping!")
            break
        else:
            input("Please enter a valid command. " )

shopping_cart()


