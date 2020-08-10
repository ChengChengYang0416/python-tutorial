# import built-in module sys
import sys as system
print(system.platform)
print("------------------------")
print(system.maxsize)
print("------------------------")
print(system.path)
print("------------------------")

# added path of self-created module to python
system.path.append("../modules")

# import self-created geometry module
import geometry
print(geometry.distance(1, 1, 5, 5))
print(geometry.slope(1, 1, 5, 5))

# import self-created circle module
import circle
print(circle.cal_area(3))
print(circle.cal_perimeter(3))