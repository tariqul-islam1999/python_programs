# Class to validate coupon code
class CouponCodeValidator:
    def is_valid_coupon(self, coupon):
        is_valid = coupon.startswith("C") and coupon[-1].isdigit()  # Boolean: True if valid
        return is_valid

# Create validator instance
validator = CouponCodeValidator()

# Get user input
coupon_code = input("Enter coupon code: ")

# Check and display result
result = validator.is_valid_coupon(coupon_code)
print(f"Coupon {coupon_code} is {'valid' if result else 'invalid'}")