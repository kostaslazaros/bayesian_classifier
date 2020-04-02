function submitform() {
  var xhr = new XMLHttpRequest();
  let form = document.forms[0];
  xhr.open('POST', form.action, true);
  var keimeno = document.getElementById('keimeno').value;
  xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
  console.log(keimeno);
  var jaa = {
    keimeno: keimeno
  };
  xhr.onreadystatechange = () => {
    if (xhr.readyState == XMLHttpRequest.DONE) {
      var resp = JSON.parse(xhr.responseText);
      var apotl = document.getElementById('apot');
      apotl.innerText = resp.predicted;
      apotl.className = 'apotvisible';
    }
  };
  xhr.send(JSON.stringify(jaa));
}

function cleanLabel() {
  document.getElementById('apot').innerText = '';
}

var getJSON = function(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.responseType = 'json';
  xhr.onload = function() {
    var status = xhr.status;
    if (status === 200) {
      callback(null, xhr.response);
    } else {
      callback(status, xhr.response);
    }
  };
  xhr.send();
};

getJSON('http://127.0.0.1:5000/categories', function(err, data) {
  if (err !== null) {
    document.getElementById('categories').innerText = '';
  } else {
    document.getElementById('categories').innerText =
      '(' + data.categories + ')';
  }
});
