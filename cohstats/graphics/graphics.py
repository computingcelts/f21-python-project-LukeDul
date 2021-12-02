import turtle

# initializes turtle graphics coordinates
new_x_position = 720 / -2
new_y_position = 675 / -2
print('Window height:' + str(new_x_position))
print('Window width:' + str(new_y_position))
turtle.tracer(0, 0)


# draws a text on the screen
def draw_text(the_text, x, y):
    turtle.penup()
    turtle.goto(new_x_position + x, new_y_position + y)
    turtle.pendown()
    turtle.write(the_text, True, align="left", font=("Arial", 20, "normal"))


# draws a bar on the screen
def draw_bar(x, y, height, width, color):
    turtle.pencolor(color)
    turtle.pensize(0)
    turtle.penup()
    turtle.setposition(new_x_position + x, new_y_position + y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


def draw_bars(x, y, color, width=10, gap=5,  total_bars=1):
    i = 0
    while i < total_bars :
        draw_bar(x + (i*(width + gap)), 50, 400, width, color)
        i += 1


def render() :
    turtle.update()  # Render image
    turtle.exitonclick()  # Wait for user's mouse click
#
# def draw_bar(x, y, height, width, color):
# You have to implement the following 4 functions
def plot_top_k_service_types(data, metadata, k):
    draw_text('Displays graph: plot_top_k_service_types', 10, 650)
    unsorted_list = []
    # print('unsorted', unsorted_list)

    for key, value in data[metadata].items():
        unsorted_list.append(value)

    sorted_list = sorted(unsorted_list, reverse=True)
    # print('sorted', sorted_list)

    final_list = []
    index = 0
    for i in sorted_list:
        if index < k:
            final_list.append(i)
        index += 1
    print(final_list)
    bars = 0
    index_2 = 0
    distance = 20
    while bars < k:
        draw_bar(distance, 550, final_list[index_2], 5, 'green')
        index_2 += 1
        bars += 1
        distance += 20


# def plot_bottom_k_service_types(data, metadata, k):
#     draw_text('Displays graph: plot_bottom_k_service_types', 10, 500)
#
#
# def plot_service_by_day(data, day):
#     # draw_text('Displays graph: plot_service_by_day', 10, 480)
#
#
# def plot_service_by_hour(data, hour):
#     # draw_text('Displays graph: plot_service_by_hour', 10, 460)

