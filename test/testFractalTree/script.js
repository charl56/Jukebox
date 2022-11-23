////////////////////////////////////////////////
// Tree fractale
////////////////////////////////////////////////
var animate = true; //Turn this to true if your computer can handle it at the level of detail that you've set
var angle = 0; //You can change this manually, or use the slider in the output
var limit = 4; //Turn this up for less lag. A good number for smooth animation is 4
var scrub = 0.01; //Slider bar scrubbing detail
var animMult = 0.001; //Multiply animation speed
var sizeMult = 0.26; //Fractal size relative to screen. Larger multipliers will increase detail
var brLenRatio = 0.68; //Size of child branch relative to parent
var canvasSize = 300;

function setup() {
  // const canva = document.createElement("canvas");
  // canva.id = "myCanvas";
  // document.body.appendChild(canva);

  // const slider = document.createElement("input")
  // slider.type = "range"
  // <input type="range" min="1" max="100" value="50" class="slider" id="myRange">

  // createCanvas(canvasSize, canvasSize);
  slider = createSlider(0, 0, 0, 0);
  slider.style('visibility', 'hidden');
}

function draw() {
  stroke(1);
  strokeWeight(1);
  background("transparent");
  // background(117, 190, 218, 0.5);

  if (animate === true) {
    angle = slider.value() + millis() * animMult;
  } else {
    angle = slider.value();
  }

  translate(width / 2, height);
  branch(height * sizeMult);
}

function branch(length) {
  line(0, 0, 0, -length);
  translate(0, -length);

  push();
  rotate(angle);
  if (length > limit) {
    branch(length * brLenRatio);
  }
  pop();

  push();
  rotate(-angle);
  if (length > limit) {
    branch(length * brLenRatio);
  }
  pop();
}
////////////////////////////////////////////////
//  Random fractale
////////////////////////////////////////////////
document.addEventListener('DOMContentLoaded', () => {
  let canvas = document.getElementById('canvas'),
      ctx = canvas.getContext('2d'),
      t = 0,
      draw,
      julia;
  
  julia = function (d1, d2) {
      let a,
          b,
          an,
          bn,
          r,
          c,
          i,
          x,
          y,
          red = 0,
          green = 0,
          blue = 0,
          width = canvas.width,
          height = canvas.height,
          left = -1,
          right = 1,
          up = (((right - left) / width) * height) / 2,
          down = (((left - right) / width) * height) / 2,
          stepX = (right - left) / width,
          stepY = (up - down) / height,
          index = 0,
          imageData;
  
      ctx.clearRect(0, 0, width, height);
      ctx.transform(
          width / (right - left),
          0,
          0,
          -height / (up - down),
          (width * left) / (left - right),
          (height * down) / (down - up)
      );
  
      imageData = ctx.createImageData(width, height);
  
      for (y = down, r = 0; y < up; y += stepY, r++) {
          for (x = left, c = 0; x < right; x += stepX, c++) {
              a = x;
              b = y;
  
              for (i = 0; i <= 100; i++) {
                  an = a * a - b * b + d1;
                  bn = 1.5 * a * b + d2;
                  a = an;
                  b = bn;
  
                  if (a >= 2 || b >= 2) {
                      red = (12 * i + i) % 128;
                      green = (16 * i + i) % 0;
                      blue = (20 * i + i) % 196;
                      break;
                  }
              }
  
              if (a < 2 && b < 2) {
                  red = 128;
                  green = 0;
                  blue = 196;
              }
  
              imageData.data[index++] = red;
              imageData.data[index++] = green;
              imageData.data[index++] = blue;
              imageData.data[index++] = 255;
          }
      }
      ctx.putImageData(imageData, 0, 0);
  };
  
  draw = function () {
      t += 0.005;
      julia(Math.cos(t) * 0.8, Math.sin(t) * 0.8);
  };
  
  setInterval(draw, 24);
});
////////////////////////////////////////////////
//  
////////////////////////////////////////////////
