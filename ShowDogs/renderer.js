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
const footsteps_to_cross_screen = 1;

const gait = ['dog.png', 'dog2.png'];
dog.src = gait[1];

var interval;

interval = setInterval(() => {
  let fractionTimeElapsed = (Date.now() - start) / ms_to_cross_screen;
  let stepsElapsed = Math.floor(footsteps_to_cross_screen * fractionTimeElapsed);

  let gait_cycle_index = Math.floor((fractionTimeElapsed - stepsElapsed / footsteps_to_cross_screen) * gait.length);

  dog.style.left = screen.width * fractionTimeElapsed + 'px';

  render_gait(gait_cycle_index);

  if (fractionTimeElapsed > 1) {
    clearInterval(interval);
    console.log('cleared interval');
  }
}, ms_per_frame);
