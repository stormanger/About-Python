import math
#import decimal
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Can not normalize the zero vector."
    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = "Only defined in two three dims."

    def __init__(self, coordinates):
        #Please input a python List.
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            #print(self.coordinates)
            self.dimension = len(coordinates)
            #print(self.dimension)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    #vector plus
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)     ##****返回的是重新初始化的向量

    #vector minus
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    #times scalar
    def times_scalar(self, scalar):
        new_coordinates = [x*scalar for x in self.coordinates]
        return Vector(new_coordinates)

    #vector magnitude 大小
    def magnitude(self):
        n = 0
        for i in self.coordinates:
            n += i ** 2
        return decimal.Decimal(math.sqrt(n))
        #coordinates_squared = [x**2 for x in self.coordinates]
        #return math.sqrt(sum(coordinates_squared))

    #unit vector 单元化向量
    def normalized(self):
        try:
            return self.times_scalar(Decimal('1.0')/self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    #dot product of vector
    def dot(self, v):
        x = [x*y for x,y in zip(self.coordinates, v.coordinates)]
        return sum(x)

    #radians and angle of vector
    def angle_with(self, v , degrees=False):
        try:
            unit1 = self.normalized()
            unit2 = v.normalized()
            angle_in_radians = math.acos(unit1.dot(unit2))

            if degrees:
                degrees_per_radian = 180. / math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Can not compute an angle with the zero verctor')
            else:
                raise e

    #zero vector test
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    #Parallel
    def is_parallel_to(self, v):
        if self.is_zero() or v.is_zero():
            return True
        elif self.angle_with(v) == 0 or self.angle_with(v) == math.pi:
            return True
        else:
            return False

    #orthogonal
    def is_orthogonal(self, v, tolerance=1e-10):
        res = self.dot(v)
        return res < tolerance

    #proj sub b of v 投影
    def component_parallel_to(self, basis):
        try:
            unit_b = basis.normalized()
            weight = self.dot(unit_b)
            return unit_b.times_scalar(weight)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    #v perp
    def component_orthogonal_to(self, basis):
        try:
            projb = self.component_parallel_to(basis)
            return self.minus(projb)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
            else:
                raise e

    #vector cross products
    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [y_1*z_2 - y_2*z_1,
                               -(x_1*z_2 - x_2*z_1),
                               x_1*y_2 - x_2*y_1]
            return Vector(new_coordinates)
        except Exception as e:
            msg = str(e)
            if msg == 'need more than 2 values to unpack':
                self_embedded_in_r3 = Vector(self.coordinates + ('0',))
                v_embedded_in_r3 = Vector(v.coordinates + ('0',))
                return self_embedded_in_r3.cross(v_embedded_in_r3)
            elif (msg == 'too many values to unpack' or
                msg == 'need more than 1 values to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    #area of paralleogram
    def area_parallelogram(self, v):
        return self.cross(v).magnitude()

    #area of triangle
    def area_triangle(self, v):
        return self.area_parallelogram(v) /Decimal('2.0')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates



#v1 = Vector([8.462, 7.893, -8.187])
#v2 = Vector([6.984, -5.975, 4.778])
#v1 = Vector([8.462, 7.893, 0])
#v2 = Vector([6.984, -5.975, 0])
#print(v1.cross(v2))
#print(v1.is_orthogonal(v2))

#v3 = Vector([-8.987, -9.838, 5.031])
#v4 = Vector([-4.268, -1.861, -8.866])
#print(v3.area_parallelogram(v4))
#print(v3.is_orthogonal(v4))

#v5 = Vector([1.5, 9.547, 3.691])
#v6 = Vector([-6.007, 0.124, 5.772])
#print(v5.area_triangle(v6))
#print(v5.is_orthogonal(v6))

#v7 = Vector([0, 0, 0])
#v8 = Vector([0, 0, 0])
#print(v7.is_parallel_to(v8))
#print(v7.is_orthogonal(v8))

#v9 = Vector([0, 0, 0])
#print(v9.is_zero())