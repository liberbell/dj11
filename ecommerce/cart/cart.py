
class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("session_key")

        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}

        self.cart = cart

    def add(self, product, prodcut_qty):
        product_id = product.id
        