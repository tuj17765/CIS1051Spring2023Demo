

var closet = [];
//now have to make it so that it takes a closet as an argument
//so that these items are added specifically to that closet
function createItem(){

    let item = {
        img: document.querySelector("#image_input").files[0],
        type: document.querySelector("#addType").value,
        color: document.querySelector("#addColor").value,
        style: document.querySelector("#addStyle").value,
        season: document.querySelector("#addSeason").value,
        fit: document.querySelector("#addFit").value

    } //adds user input of type, color, style, season, fit to an item

    closet.push(item); //adds new item to closet
    document.querySelector("#form").reset();   //clears form entry for next ones
    document.querySelector("#showCloset").innerHTML = "";

    //displays the closet and the items inside - just for now, needs to be done w style sheet
    for (var i = 0; i < closet.length; i++) {
        var article = closet[i];
        var descriptors = "Item " + (i+1) + ": ";
        descriptors += "Type: " + article.type + ", ";
        descriptors += "Color: " + article.color + ", ";
        descriptors += "Style: " + article.style + ", ";
        descriptors += "Season: " + article.season + ", ";
        descriptors += "Fit: " + article.fit;

        var img = document.createElement("img");
        img.src = URL.createObjectURL(article.img); 
        img.style.height = "70px";
        img.style.width = "50px";
        document.querySelector("#showCloset").appendChild(img);
        document.querySelector("#showCloset").innerHTML += descriptors + "<br>";
    }
}

function createOutfit(){
    var outfit = [] //array of items
}

document.getElementById("btn").onclick = function(){createItem()};


  