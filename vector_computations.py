from vector import Vector
import math

print 'Addition'
print (Vector([8.218, -9.341]) + Vector([-1.129, 2.111])).round(3)
print

print 'Subtraction'
print (Vector([7.119, 8.215]) - Vector([-8.223, 0.878])).round(3)
print

print 'Scalar Multiplication'
print (Vector([1.671, -1.012, -0.318]) * 7.41).round(3)
print

print 'Magnitude'
print Vector([-0.221, 7.437]).magnitude()
print Vector([8.813, -1.331, -6.247]).magnitude()
print

print 'Direction'
print Vector([5.581, -2.136]).direction()
print Vector([1.996, 3.108, -4.554]).direction()
print

print 'Dot Product'
print Vector([7.887, 4.138]) * Vector([-8.802, 6.776])
print Vector([-5.955, -4.904, -1.874]) * Vector([-4.496, -8.755, 7.103])
print

print 'Angle'
print Vector([3.183, -7.627]).angle(Vector([-2.668, 5.319]))
print math.degrees(Vector([7.35, 0.221, 5.188]).angle(Vector([2.751, 8.259, 3.985])))
print

vectors = [
    [Vector([-7.579, -7.88]), Vector([22.737, 23.64])],
    [Vector([-2.029, 9.97, 4.172]), Vector([-9.231, -6.639, -7.245])],
    [Vector([-2.328, -7.284, -1.214]), Vector([-1.821, 1.072, -2.94])],
    [Vector([2.118, 4.827]), Vector([0, 0])]
]

print "Parallel"
for first, second in vectors:
    print first.parallel(second)
print

print "Orthogonal"
for first, second in vectors:
    print first.orthogonal(second)
print

print "Projection"
print "  - parallel"
print Vector([0.825, 2.036]).projection(Vector([3.039, 1.879])).round(3)
print "  - orthogonal"
v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print (v - b.projection(v)).round(3)
print "  - full composition"
v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print b.projection(v).round(3)
print (v - b.projection(v)).round(3)
