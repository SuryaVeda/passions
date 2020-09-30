
var grey = document.getElementById("grey");
var sepia = document.getElementById("sepia");
var yellow = document.getElementById("yellow");
var white = document.getElementById("white");
var brown = document.getElementById("brown");
var black = document.getElementById("black");

grey.addEventListener('click', gcss);
sepia.addEventListener('click', scss);
yellow.addEventListener('click', ycss);
white.addEventListener('click', wcss);
brown.addEventListener('click', bcss);
black.addEventListener('click', blcss);


var elements = document.getElementsByClassName('page');
function gcss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.sepia || localStorage.yellow){
			localStorage.removeItem('sepia');
			localStorage.removeItem('yellow');
		}
		localStorage.setItem('grey', '#696969');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('grey');
		}
	}
	else {

	}
	
}
function scss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.grey || localStorage.yellow){
			localStorage.removeItem('grey');
			localStorage.removeItem('yellow');
		}
		localStorage.setItem('sepia', '#f2d5b8');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('sepia');
		}
	}
	else {

	}
	
}
function ycss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.sepia || localStorage.grey){
			localStorage.removeItem('sepia');
			localStorage.removeItem('grey');
		}
		localStorage.setItem('yellow', '#ffffc4');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('yellow');
		}
	}
	else {

	}
	
}
function wcss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.brown || localStorage.black){
			localStorage.removeItem('brown');
			localStorage.removeItem('black');
		}
		localStorage.setItem('white', 'white');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('white');
		}
	}
	else {

	}
	
}
function bcss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.black || localStorage.white){
			localStorage.removeItem('white');
			localStorage.removeItem('black');
		}
		localStorage.setItem('brown', '#471212');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('brown');
		}
	}
	else {

	}
	
}
function blcss() {
	if (typeof(Storage) !== "undefined") {
		if (localStorage.brown || localStorage.white){
			localStorage.removeItem('brown');
			localStorage.removeItem('white');
		}
		localStorage.setItem('black', 'black');
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('black');
		}
	}
	else {

	}
	
}

function getlocalstorage() {
	if (localStorage.grey) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('grey');
		}
	}
	if (localStorage.sepia) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('sepia');
		}
	}
	if (localStorage.yellow) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.backgroundColor = localStorage.getItem('yellow');
		}
	}
	if (localStorage.black) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('black');
		}
	}
	if (localStorage.white) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('white');
		}
	}
	if (localStorage.brown) {
		for(var i=0; i < elements.length; i++) {
		   elements[i].style.color = localStorage.getItem('brown');
		}
	}
}



    
function getlocalstorageAddPage() {
      var box = document.getElementById('box');
      var head = document.getElementById('id_para');
      var para = document.getElementById('id_heading');
      if (localStorage.grey) {
        box.style.backgroundColor = localStorage.getItem('grey');
        para.style.backgroundColor = localStorage.getItem('grey');
        para.style.borderColor = localStorage.getItem('grey');
        head.style.borderColor = localStorage.getItem('grey');
        head.style.backgroundColor = localStorage.getItem('grey');
        
      }
       if (localStorage.sepia) {
        box.style.backgroundColor = localStorage.getItem('sepia');
        para.style.backgroundColor = localStorage.getItem('sepia');
        para.style.borderColor = localStorage.getItem('sepia');
        head.style.borderColor = localStorage.getItem('sepia');
        head.style.backgroundColor = localStorage.getItem('sepia');
      }
       if (localStorage.yellow) {
        box.style.backgroundColor = localStorage.getItem('yellow');
        para.style.backgroundColor = localStorage.getItem('yellow');
        para.style.borderColor = localStorage.getItem('yellow');
        head.style.borderColor = localStorage.getItem('yellow');
        head.style.backgroundColor = localStorage.getItem('yellow');
      }
       if (localStorage.black) {
        box.style.color = localStorage.getItem('black');     
        para.style.color = localStorage.getItem('black');
        head.style.color = localStorage.getItem('black');

      }
       if (localStorage.brown) {
        para.style.color = localStorage.getItem('brown');
        head.style.color = localStorage.getItem('brown');
        box.style.color = localStorage.getItem('brown');
    }
       if (localStorage.white) {
        para.style.color = localStorage.getItem('white');
        head.style.color = localStorage.getItem('white');
        box.style.color = localStorage.getItem('white');   
    }
     }