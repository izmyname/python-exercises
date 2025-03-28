def serve_dish(garnish = None):
    if garnish is None:
        print("default garnish: mint")

    else:
        print(f"custom garnish used: {garnish}")
              
serve_dish()