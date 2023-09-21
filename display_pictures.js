amout_pictures = 4

// add pictures by dragging them into Media/pictures and then run the
// pyton script to both rename the images and change amount_pictures
// in this file. please don't tuch the first line here :)

function displayPicture(name){
    return "<img id='photo'src='Media/pictures/" + name + ".jpeg'>"
}

for (var i = 1; i <= amout_pictures; i++){
    document.getElementById("photos").innerHTML += displayPicture("p" + 1)
}

