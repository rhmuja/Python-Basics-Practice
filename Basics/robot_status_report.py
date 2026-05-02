#"Can you create a "Robot Status Report" that looks like this?

"""
Need to print-
==============================
      ROBOT SYSTEM CHECK
==============================
Battery: 	 100%
Joints: 	 OK
Sensor 1: 	 50 + 50 (Print the sum)
Sensor 2: 	 200 - 120 (Print the result)
------------------------------
Status: 	 ALL SYSTEMS GO
==============================
"""

#Solution is

#print_border_and_Text
print("=" * 25, sep="")
print("   ROBOT SYSTEM CHECK ")
print("=" * 25, sep="")

#print_items
print("Battery: \t", "100%")
print("Joints: \t", "Ok")
print("Sensor 1: \t", 50+50)
print("Sensor 2: \t", 200-120)

#print_one_line
print("-" * 25)

#print_status
print("Status: ", "ALL SYSTEM GO")

#print_end_border
print("=" * 25)
