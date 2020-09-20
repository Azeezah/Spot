// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// No Node.js APIs are available in this process because
// `nodeIntegration` is turned off. Use `preload.js` to
// selectively enable features needed in the rendering
// process.

var dog = document.getElementById('dog');
var imgs = document.querySelectorAll('#dog > img');

const start = Date.now();  // timestamp in ms
const ms_to_cross_screen = 10000;
const fps = 60;
const ms_per_frame = 1000/fps;
const footsteps_per_sec = 15;

var interval = setInterval(() => {
  let ms_elapsed = (Date.now() - start);
  let x_coord = screen.width * ms_elapsed / ms_to_cross_screen;
  dog.style.left = x_coord + 'px';

  for (let img of imgs) { img.style.visibility = "hidden"; }
  let i = Math.floor((footsteps_per_sec * ms_elapsed / 1000) % imgs.length);
  imgs[i].style.visibility = "visible";

  if (ms_elapsed > ms_to_cross_screen) {
    clearInterval(interval);
  }
}, ms_per_frame);
