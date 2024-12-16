// Canvas setup
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const WIDTH = 450;
const HEIGHT = 600;
const CENTER = { x: WIDTH / 2, y: HEIGHT / 2 };
const RADIUS = 150;

canvas.width = WIDTH;
canvas.height = HEIGHT;

// Ball class
class Ball {
    constructor(x, y, radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = { 
            r: Math.random() * 255, 
            g: Math.random() * 255, 
            b: Math.random() * 255 
        };
        this.vx = Math.random() * 2 - 1;
        this.vy = Math.random() * 2 - 1;
        this.gravity = 0.5;
        this.colorChnage = {
            r: 1,
            g: 1,
            b: 1
        };
    }

    draw(ctx) {
        if(this.color.r >= 255 || this.color.r <= 0) {
            this.colorChnage.r *= -1;
        }
        if(this.color.g >= 255 || this.color.g <= 0) {
            this.colorChnage.g *= -1;
        }
        if(this.color.b >= 255 || this.color.b <= 0) {
            this.colorChnage.b *= -1;
        }

        this.color.r += this.colorChnage.r;
        this.color.g += this.colorChnage.g;
        this.color.b += this.colorChnage.b;

        ctx.fillStyle = `rgb(${this.color.r}, ${this.color.g}, ${this.color.b})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.strokeStyle = "white";
        ctx.stroke();
        ctx.closePath();
    }

    move() {
        this.vy += this.gravity;
        this.x += this.vx;
        this.y += this.vy;

        // Bounce if hitting the circular boundary
        const dx = this.x - CENTER.x;
        const dy = this.y - CENTER.y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance + this.radius > RADIUS) {
            const magnitude = Math.sqrt(dx * dx + dy * dy);
            const nx = dx / magnitude;
            const ny = dy / magnitude;

            const dotProduct = this.vx * nx + this.vy * ny;
            this.vx -= 2.02 * dotProduct * nx;
            this.vy -= 2.02 * dotProduct * ny;

            // Slightly move the ball back inside the circle
            const overlap = distance + this.radius - RADIUS;
            this.x -= nx * overlap;
            this.y -= ny * overlap;

            this.radius += 1; // Increase radius on collision
        }
    }
}

// Ball array
const balls = [];

// Draw circle boundary
function drawBoundary() {
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(CENTER.x, CENTER.y, RADIUS, 0, Math.PI * 2);
    ctx.stroke();
    ctx.closePath();
}

// Add a new ball
function addBall() {
    const x = CENTER.x + Math.random() * 200 - 100;
    const y = CENTER.y - 100;
    balls.push(new Ball(x, y, 10));
}

// Animation loop
function animate() {

    const homeScreen = document.getElementById("homeScreen")
    const gameCanvas = document.getElementById("gameCanvas")
    homeScreen.style.display = "none";
    gameCanvas.style.display = "inline";


    drawBoundary();
    balls.forEach((ball) => {
        ball.move();
        ball.draw(ctx);
    });
    requestAnimationFrame(animate);
}

// Event listener for adding a ball on click
canvas.addEventListener('click', () => {
    addBall();
});

// Start animation
document.getElementById('startButton').addEventListener('click', function() {
    const homeScreen = document.getElementById("homeScreen");
    const gameCanvas = document.getElementById("gameCanvas");
    homeScreen.style.display = "none";
    gameCanvas.style.display = "inline";
    animate(); // Start the animation when button is clicked
});