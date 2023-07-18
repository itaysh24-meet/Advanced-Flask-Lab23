from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgWy3DLSoDNZxaoOiVo3G9I7-fXtRAztlpB8YtYejl&s"

user_bio = "Middle East Entrepreneurs of Tomorrow. Enabling the next generation of Israeli and Palestinian leaders."

posts = {
    "https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg": "The cohort of 2022!",
    "https://th-thumbnailer.cdn-si-edu.com/bZAar59Bdm95b057iESytYmmAjI=/1400x1050/filters:focal(594x274:595x275)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/95/db/95db799b-fddf-4fde-91f3-77024442b92d/egypt_kitty_social.jpg": "MEET graduation!",
    "https://cdn.theatlantic.com/thumbor/W544GIT4l3z8SG-FMUoaKpFLaxE=/0x131:2555x1568/1600x900/media/img/mt/2017/06/shutterstock_319985324/original.jpg": "#MEET_HACKATHON",
    "https://th-thumbnailer.cdn-si-edu.com/Nt501gmta9PWNEpTToe9zFIhPNE=/fit-in/1600x0/filters:focal(978x630:979x631)/https://tf-cmsv2-smithsonianmag-media.s3.amazonaws.com/filer/db/82/db8234fc-f167-4285-82bd-123d035e32ad/cats.jpg": "Class of 2024's Y1 closing event cohort"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html', userbio=user_bio, imagelink=image_link, Posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
