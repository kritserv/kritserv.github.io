function changeColAndImg() {
	var img = document.getElementById("switchCol");
	var footer = document.querySelector(".footer");
	var dialoglinks = document.getElementsByClassName("dLink");

	if (img.src == "https://images.unsplash.com/photo-1485075792961-9ea033ad04fc") {
		img.src = "https://images.unsplash.com/photo-1584381443170-bfbc4463966a";
		document.body.style.backgroundColor = "black";
		document.documentElement.style.backgroundColor = "black";
		footer.style.backgroundColor = "#00a1ff";
		for (var i = 0; i < dialoglinks.length; i++) {
			dialoglinks[i].style.color = "#00a1ff";
		}
	} else {
		img.src = "https://images.unsplash.com/photo-1485075792961-9ea033ad04fc";
		document.body.style.backgroundColor = "#25282c";
		document.documentElement.style.backgroundColor = "#25282c";
		footer.style.backgroundColor = "#111";
		for (var i = 0; i < dialoglinks.length; i++) {
			dialoglinks[i].style.color = "gold";
		}
	}
}
