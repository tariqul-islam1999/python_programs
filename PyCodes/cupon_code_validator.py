"""

Cupon Code Validator
--------------------
Checks whether the cupon code is valid or invalid

"""
class CouponCodeValidator:
    def is_valid_coupon(self, coupon):
        if not coupon:
            return False
        
        wrong_inputs = " +-*/_=<>,.!#:;'?{}[]()\\|`~"
        wrong_inputs_list = list(wrong_inputs)
        for char in wrong_inputs_list:
            if char in coupon:
                return False
        is_valid = coupon.startswith("C") and coupon[-1].isdigit()
        return is_valid

validator = CouponCodeValidator()
coupon_code = input("Enter coupon code: ")
result = validator.is_valid_coupon(coupon_code)
print(f"Coupon {coupon_code} is {'valid' if result else 'invalid'}")