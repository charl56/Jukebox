<template>
    <v-row class="rowFractale">
        <div class="divFractale">
            <canvas id="my_canvas_tree" width="1000" height="800"></canvas>
        </div>
    </v-row>
</template>

<script>
export default {
    name: 'AppFractaleTree',
    created(){
    this.$root.$refs.FractaleTree = this;
    },
    mounted(){ // Lance la fonction au chargement de la page
        // this.drawTreeTime();
        // this.drawTree(400, 600, 120, 0, 10, "grey", "blue");
    },
    data () {
        return {
        myCanvas: '',
        ctx: ''
        }
    },
    methods:{
        async playThisSong(){
        },
        drawTree(startX, startY, len, angle, branchWidth, color1, color2) {
            var myCanvas = document.getElementById("my_canvas_tree");
            var ctx = myCanvas.getContext("2d");

            ctx.lineWidth = branchWidth;

            ctx.beginPath();
            ctx.save();

            ctx.strokeStyle = color1;
            ctx.fillStyle = color2;

            ctx.translate(startX, startY);
            ctx.rotate(angle * Math.PI/180);
            ctx.moveTo(0, 0);
            ctx.lineTo(0, -len);
            ctx.stroke();

            ctx.shadowBlur = 15;
            ctx.shadowColor = "rgba(0,0,0,0.8)";

            if(len < 15) {
                ctx.beginPath();
                ctx.arc(0, -len, 10, 0, Math.PI/2);
                ctx.fill();
                ctx.restore();
                return;
            }

            this.drawTree(0, -len, len*0.8, angle-15, branchWidth*0.8);
            this.drawTree(0, -len, len*0.8, angle+15, branchWidth*0.8);

            ctx.restore();
        },
        drawTreeTime(){
            // var angle = 0;
            // for(angle; angle < 180; angle++ ){
            //     this.drawTree(400, 600, 120, angle, 10, "grey", "blue");
            //     setTimeout(1000);

            // }  
            // for(angle; angle < 180; angle++ ){
            //     this.drawTree(400, 600, 120, -angle, 10, "grey", "blue");
            // }               

        }
    },
    computed: {

    }
}
</script>

<style>
.divFractale{
    background-color: white;;
    margin-left: auto;
    margin-right: auto;
    /* width: 100%;
    height: 10em; */
}
</style>