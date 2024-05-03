function changeCol() {
	var img = document.getElementById("switchCol");
	if (img.src == "https://images.unsplash.com/photo-1530128118208-89f6ce02b37b") {
		img.src = "https://images.unsplash.com/photo-1489100517551-92a468b736f0";
		document.body.style.backgroundColor = "black";
		document.documentElement.style.backgroundColor = "black"
	} else {
		img.src = "https://images.unsplash.com/photo-1530128118208-89f6ce02b37b";
		document.body.style.backgroundColor = "#25282c";
		document.documentElement.style.backgroundColor = "#25282c"
	}
}
