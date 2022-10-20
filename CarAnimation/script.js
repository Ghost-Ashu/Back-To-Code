var audio=document.createElement('audio');
audio.setAttribute('src','sound.mp3');
audio.loop=true;
var body=document.getElementsByTagName("body");
console.log(body);
audio.play();