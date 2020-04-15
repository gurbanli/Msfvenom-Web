function getPayloadOptions() {
    let payload = document.getElementById('payloads').options.item(document.getElementById('payloads').options.selectedIndex).value;
    payload = payload.replace(/\//g, '');
    let http = new XMLHttpRequest();

    http.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            makeOptionTags(this.responseText);
        }
    };

    http.open("POST", "/get/" + payload, true);
    http.send();
}

function makeOptionTags(text) {
    let options_json = JSON.parse(text);
    let options = options_json['options'];
    let elements = document.getElementsByClassName('options');
    while (elements.length > 0) {
        elements[0].parentNode.removeChild(elements[0]);
    }
    for (let i = 0; i < options.length; i++) {
        let newHtml = '';
        newHtml += `<label for="options_${options[i]}">${options[i]}</label>\n`;
        newHtml += `<input class="form-control" name="options_${options[i]}" required type="text">`;
        let element = document.getElementById('payload-div');
        let newDiv = document.createElement('div');
        newDiv.className = "form-group options";
        newDiv.innerHTML = newHtml;
        element.parentNode.insertBefore(newDiv, element.nextSibling);
    }

}

window.onload = getPayloadOptions;
document.getElementById('payloads').onchange = getPayloadOptions;