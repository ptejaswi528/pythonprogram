def apply_discount(price,discount_percent):
    dis=price*discount_percent/100
    f=price-dis
    return f
def add_gst(price,gst_percent=18):
    gst=price*gst_percent/100
    total=price+gst
    return total
def generate_invoice(cart,discount_percent=0,gst_percent=18):
    total_price=0
    for i in cart.values():
        total_price+=int(i)
        dis1=apply_discount(total_price,discount_percent)
        gst1=add_gst(dis1,gst_percent)
    return total_price,dis1,gst1
cart={}