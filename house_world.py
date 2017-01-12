import cs1graphics as cg

paper = cg.Canvas()
paper.setBackgroundColor('forestGreen')
paper.setWidth(800)
paper.setHeight(600)
paper.setTitle('My World')

sun = cg.Circle(50, cg.Point(100, 100))
sun.setFillColor('yellow')

paper.add(sun)

sunray_endpoints = {
    "SW": ((65, 135), (30, 170)),
    "SE": ((135, 135), (170, 170)),
    "NE": ((135, 65), (170, 30)),
    "NW": ((65, 65), (30, 30)),

}

sunrays = []
#index = 0

for direction, points, in sunray_endpoints.items():


    sunrays.append(cg.Path(cg.Point(*points[0]), cg.Point(*points[1])))

    # if we wanted to name the instances of sunrays in the sunrays list
    # obj_name = sunray + direction
    # obj_init = obj_name+ " = sunrays[index]"

    # index += 1
    # exec(obj_init)

# if we wanted to name the instances of sunrays in the sunrays list

for ray in sunrays:
    ray.setBorderColor('gold')
    ray.setBorderWidth(6)
    paper.add(ray)
