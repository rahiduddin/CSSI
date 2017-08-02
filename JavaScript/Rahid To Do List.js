function Task1Complete(silentshane) {
  var bulletstyle = document.getElementById(silentshane).style.textDecoration;

  if (bulletstyle == 'line-through') {
    document.getElementById(silentshane).style.textDecoration = 'none';
  } else {
    document.getElementById(silentshane).style.textDecoration = 'line-through';
  }
}

function clearlist() {
  names = document.getElementByClassName("line-through");
  for (i = 0; i < names, length; i++) {
    names[i].style.textDecoration = "none";
  }
}

function addnew() {
  var addme = prompt("Add New");
  addListItem(addme);
}

function addListItem(text) {
  list = document.querySelector('ol');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
