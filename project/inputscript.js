
var closet = [];
/*
var closetList = []; //display closet list on right hand side, also each name should be a link

function createCloset(){
    var closet = [];

    closetList.push(closet);
}

function editCloset(closetToEdit){ //now takes a closet as an argument so that these items are added specifically to that closet 
    document.getElementById("addItemBtn").onclick = function(){createItem()};

}*/

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
    document.querySelector("#addItemForm").reset();   //clears form entry for next ones
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

document.getElementById("newClosetBtn").onclick = function(){createCloset()};
document.getElementById("editClosetBtn").onclick = function(){editCloset()};


  