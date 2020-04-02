function submitform() {
  var xhr = new XMLHttpRequest();
  let form = document.forms[0];
  xhr.open("POST", form.action, true);
  var keimeno = document.getElementById("keimeno").value;
  xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
  console.log(keimeno)
  var jaa = {
    "keimeno": keimeno
  };
  xhr.onreadystatechange = () => {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      var resp = JSON.parse(xhr.responseText);
      var apotl = document.getElementById("apot");
      apotl.innerText = resp.predicted;
      apotl.className = "apotvisible"
    }
  }
  xhr.send(JSON.stringify(jaa));
}

function cleanLabel() {
  document.getElementById("apot").innerText = "";
}
