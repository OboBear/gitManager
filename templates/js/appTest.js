var xhr = new XMLHttpRequest();
function send() {
	
	xhr.open("GET", "http://120.27.51.48:9999", true);
	
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//	xhr.setRequestHeader("Content-type", "text/html");
	
	xhr.onreadystatechange = function() {
		var XMLHttpReq = xhr;
		
		if (XMLHttpReq.readyState == 4) {
		alert(XMLHttpReq.status)
			if (XMLHttpReq.status == 200) {
				var text = XMLHttpReq.responseText;
				alert(text)
				console.log(text);
			}
		}
	};
	alert(123)
	xhr.send(null)
	
	
}