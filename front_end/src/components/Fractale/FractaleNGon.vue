<template>
    <v-row class="rowFractale">
        <div class="divFractale">
            <canvas id="canvas" width="300" height="300"></canvas>
        </div>
    </v-row>
</template>

<script>

export default {
    name: 'AppFractaleNgon',
    mounted() {    // Au chargement de la page
        const box = document.createElement("canvas");
        box.id = "canvas";
        document.body.appendChild(box);

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
            },
            data : function () {
                return {
                }
    },
    methods:{       // Modifier le code contre le plagiat ? c'est un projet perso

        }

}
</script>