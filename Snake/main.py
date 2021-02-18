from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game NODERRR")
screen.tracer(0)

snake = Snake()
food = Food()
score= Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.NewPosition()
        snake.extend()
        score.score_up()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
     

    for part in snake.snake_parts[1:]:#The slice skip the cullision with the head cuz the head collides with himslef at begining
        if snake.head.distance(part) < 10:
            score.reset()
            snake.reset()
            



       

        






screen.exitonclick()