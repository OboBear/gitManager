var xhr = new XMLHttpRequest();

function send() {

	xhr.open("GET", "/show", true);
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
	xhr.send(null)
}