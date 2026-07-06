# Task 4 - Using Map(): Apply GST to List of Prices

prices=[100,250,400,1200,50]
prices_with_gst= list(map(lambda price:price + (0.18*price),prices))
print(f"Orginal Prices: {prices}")
print(f"Prices After GST : {prices_with_gst}")