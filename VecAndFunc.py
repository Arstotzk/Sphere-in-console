class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Leng(self):
        return (self.y ** 2 + self.x ** 2) ** 0.5

    def Plus(self, vec):
        return vec2(self.x + vec.x, self.y + vec.y)

    def Minus(self, vec):
        return vec2(self.x - vec.x, self.y - vec.y)

    def Division(self, vec):
        return vec2(self.x / vec.x, self.y / vec.y)


class vec3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def Norm(self):
        le = vec3.Leng(self)
        vecL = vec3(le, le, le)
        vecL = vec3.Division(self, vecL)
        return vecL

    def Leng(self):
        return (self.y ** 2 + self.x ** 2 + self.z ** 2) ** 0.5

    def Plus(self, vec):
        return vec3(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def Minus(self, vec):
        return vec3(self.x - vec.x, self.y - vec.y, self.z - vec.z)

    def Division(self, vec):
        return vec3(self.x / vec.x, self.y / vec.y, self.z / vec.z)

    def Multiplication(self, vec):
        return vec3(self.x * vec.x, self.y * vec.y, self.z * vec.z)

    def Dot(self, vec):
        s = float(self.x * vec.x + self.y * vec.y + self.z * vec.z)
        return s


class vecFunc:

    def rotateX(self, angle):
        b = self
        b.z = self.z * math.cos(angle) - self.y * math.sin(angle)
        b.y = self.z * math.sin(angle) + self.y * math.cos(angle)
        b.x = self.x
        return b
    def rotateY(self, angle):
        b = self
        b.x = self.x * math.cos(angle) - self.z * math.sin(angle)
        b.z = self.x * math.sin(angle) + self.z * math.cos(angle)
        b.y = self.y
        return b
    def rotateZ(self, angle):
        b = self
        b.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        b.y = self.x * math.sin(angle) + self.y * math.cos(angle)
        b.z = self.z
        return b

    def sph(ro, rd, ce, ra):
        oc = vec3.Minus(ro, ce)
        b = float(vec3.Dot(oc, rd))
        c = vec3.Dot(oc, oc) - ra * ra
        h = b * b - c
        if (h < 0.0):
            return vec2(-1, -1)
        h = h ** 0.5
        return vec2(-b - h, -b + h)