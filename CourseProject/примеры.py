class Vector:
    def __init__(self, components):
        self.components = components

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __str__(self):
        return str(self.components)

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
        result = [x + y for x, y in zip(self, other)]
        return Vector(result)

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
        result = [x - y for x, y in zip(self, other)]
        return Vector(result)

    def __mul__(self, scalar):
        result = [x * scalar for x in self]
        return Vector(result)

    def dot_product(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")
        result = sum(x * y for x, y in zip(self, other))
        return result


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])


#
# /*
# ** Проекция vector V1 on vector V2  and return the len vector V1;
# ** return (sqrt(pow(v->x, 2) + pow(v->y, 2) + pow(v->z, 2)));
# */
#
# double		ft_vector_projection_on_ray(t_vector *v1, t_vector *v2)
# {
# 	return (ft_vector_scalar(v1, v2) / ft_vector_modul(v2));
# }