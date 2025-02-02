
class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")

        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        self.cart = cart

    def add(self, product, prodcut_qty):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]["qty"] = prodcut_qty
            
        else:
            self.cart[product_id] = {"price": str(product.price), "qty": prodcut_qty}

        self.session.modified = True