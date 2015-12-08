var xhr = new XMLHttpRequest();

function send() {
	
	xhr.open("POST", "/command", true);
	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
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
	var postParam = "command=repo";
	xhr.send(postParam)
}