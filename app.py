from flask import Flask, render_template, request, url_for
import os
import random
from os import path

app = Flask(__name__)

#how many image puzzles are available to choose from
num_images = 6
#how many parts the images are divided into on each side (puzzles must be square and have at least one part)
parts_per_side = 2

#determines which image is shown to the user
image_num = random.randint(0,num_images-1)

num_parts = parts_per_side ** 2

@app.route("/", methods=["GET", "POST"])
def main():
    global image_num
    global num_images
    global parts_per_side
    global num_parts
    #indicates that user requested a new image
    if request.method == "POST" and request.form and request.form["new"] == "New Puzzle":
        print("New puzzle requested")
        #fetch a new image randomly
        image_num = random.randint(0,num_images-1)
    #randomize the order that the parts will appear in the grid
    image_parts = [*range(0,num_parts)]
    random.shuffle(image_parts)
    
    return render_template("puzzle.html", image_num = image_num, parts_per_side = parts_per_side, image_parts = image_parts)

@app.before_first_request
def add_images():
    #allows loading the static images
    global num_images
    global num_parts
    for img in range(0, num_images):
        for part in range(0, num_parts):
            file = path.join("images",str(img),str(part)+".jpg")
            print("loaded file:",file)
            url_for("static", filename=file)

if __name__ == "__main__":
	app.run(host="localhost", port=8080, debug=False)
