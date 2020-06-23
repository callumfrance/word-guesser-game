console.log(document.cookie);
initialThemeSet();

function initialThemeSet() {
    var themeCookieResult = getCookie("toggleTheme");
    var themeSwitch = document.getElementById("themeSwitch");
    
    console.log(themeCookieResult);

    if (themeCookieResult == "true") {
        document.getElementById('formalTheme').disabled = true;
        document.getElementById('popTheme').disabled = false;
        themeSwitch.checked = true;
    } else {
        document.getElementById('popTheme').disabled = true;
        document.getElementById('formalTheme').disabled = false;
        themeSwitch.checked = false;
    }
}

function toggleThemeCheckBox() {
    var themeCookieResult = getCookie("toggleTheme");
    var themeSwitch = document.getElementById("themeSwitch");

    if (themeSwitch.checked == true) {
        document.getElementById('formalTheme').disabled = true;
        document.getElementById('popTheme').disabled = false;
    } else {
        document.getElementById('popTheme').disabled = true;
        document.getElementById('formalTheme').disabled = false;
    }

    setCookie("toggleTheme", themeSwitch.checked, 365);
}

function setCookieInner(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    console.log("setCookieInner " + cname + cvalue + exdays + " " + document.cookie);
}

function setCookie(cname, cvalue, exdays) {
    setCookieInner(cname, '', -1);
    setCookieInner(cname, cvalue, exdays);
}

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}
