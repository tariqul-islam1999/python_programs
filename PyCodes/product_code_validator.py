"""

Product Code Validator
-----------------------
Checks whether a product code is start with P & total length of code is 5.

"""
class ProductCodeValidator:
    def is_valid_code(self, code):
        is_valid = code.startswith("P") and len(code) == 5 
        return is_valid

validator = ProductCodeValidator()
product_code = input("Enter product code: ")
result = validator.is_valid_code(product_code)
print(f"Code {product_code} is {'valid' if result else 'invalid'}")