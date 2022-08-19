var today = new Date();
var todayDate = today.getDate() + '/'+ (today.getMonth() + 1) + '/' + today.getFullYear();
var todayTime = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

var date = todayDate + ' ' + todayTime;

var msg = "Current URL: " + document.location.protocol + "//" + document.location.hostname;
console.log("[DEBUG] " + date + " " + msg);
