// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.

var dog = document.getElementById('dog');

const start = Date.now();  // timestamp in ms
const ms_to_cross_screen = 5000;
const fps = 60;
const ms_per_frame = 1000/fps;
var interval;

interval = setInterval(() => {
  let x = screen.width * (Date.now() - start) / ms_to_cross_screen;
  dog.style.left = x + 'px';

  if (x > screen.width) {
    clearInterval(interval);
  }
}, ms_per_frame);
