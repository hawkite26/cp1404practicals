"""
Test file for silver_service_taxi.py
"""


from prac_08.silver_service_taxi import SilverServiceTaxi

test_ride = SilverServiceTaxi("Silver", 100, 4)
test_ride.drive(50)
print(test_ride, test_ride.get_fare())
test_ride.start_fare()
print(test_ride)
