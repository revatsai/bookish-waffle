// go to top button
var mybutton = document.getElementById("goTopBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 450 || document.documentElement.scrollTop > 450) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}
// go to top button end

function editinfo() {
    document.getElementById('UserName').removeAttribute("disabled");
    document.getElementById('gender').removeAttribute("disabled");
    document.getElementById('birthday').removeAttribute("disabled");
    document.getElementById('height').removeAttribute("disabled");
    document.getElementById('weight').removeAttribute("disabled");
    document.getElementById('submit').removeAttribute("disabled");
    document.getElementById('photo').removeAttribute("disabled");
}

function saveinfo() {
    document.getElementById('UserName').setAttribute("disabled");
    document.getElementById('gender').setAttribute("disabled");
    document.getElementById('birthday').setAttribute("disabled");
    document.getElementById('height').setAttribute("disabled");
    document.getElementById('weight').setAttribute("disabled");
    document.getElementById('submit').setAttribute("disabled");
    document.getElementById('photo').setAttribute("disabled");
}


/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function () {
  var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("navbar").style.top = "0";
  } else {
    document.getElementById("navbar").style.top = "-50px";
  }
  prevScrollpos = currentScrollPos;
};
