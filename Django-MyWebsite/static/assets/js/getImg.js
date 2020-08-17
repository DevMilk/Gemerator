
var img = $("img")[0];
console.log("aa");

$.ajax({
	 

	type: "GET", 
	dataType: 'jsonp',
	url: "https://gemerrator.ey.r.appspot.com/generate?callback=json",  
	success: function(data){
		console.log("funcc");
		let obj = JSON.parse(data);
		console.log(obj.Images);
		console.log("gumo");
		//img.src = "data:image/png;base64,"+obj.Images; 
	}
});
 