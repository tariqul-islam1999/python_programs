# Class to validate product code
class ProductCodeValidator:
    def is_valid_code(self, code):
        is_valid = code.startswith("P") and len(code) == 5  # Boolean: True if valid
        return is_valid

# Create validator instance
validator = ProductCodeValidator()

# Get user input
product_code = input("Enter product code: ")

# Check and display result
result = validator.is_valid_code(product_code)
print(f"Code {product_code} is {'valid' if result else 'invalid'}")