LITTER_PER_GALLON = 3.785411784
KMS_PER_MILE = 1.609344


def liters_100km_to_miles_gallon(liters):
    kms_per_liter = 100/liters
    kms_per_gallon = kms_per_liter*LITTER_PER_GALLON
    miles_per_gallon = kms_per_gallon/KMS_PER_MILE
    return miles_per_gallon


def miles_gallon_to_liters_100km(miles):
    gallons_per_100miles = 100/miles
    gallons_per_100kms = gallons_per_100miles/KMS_PER_MILE
    liters_per_100kms = gallons_per_100kms*LITTER_PER_GALLON
    return liters_per_100kms


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
