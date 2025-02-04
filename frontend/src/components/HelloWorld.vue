<template>
  <div class="pixi-container">
    <canvas ref="pixiCanvas"></canvas>
  </div>
</template>

<script>
import * as PIXI from "pixi.js";

export default {
  name: "HelloWorld",
  data() {
    return {
      app: null,
      sprite: null,
      depthMap: null,
      displacementFilter: null,
      originalImageWidth: 0,
      originalImageHeight: 0,
      isMobile: false,
    };
  },
  methods: {
    detectDevice() {
      // Simple mobile detection
      this.isMobile =
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
          navigator.userAgent
        );
    },

    async drawPixi() {
      this.detectDevice();

      try {
        this.app = new PIXI.Application();
        await this.app.init({
          width: window.innerWidth,
          height: window.innerHeight,
          antialias: true,
          transparent: true,
          view: this.$refs.pixiCanvas,
        });

        const [imageModule, depthModule] = await Promise.all([
          import("../assets/card.jpg"),
          import("../assets/card_depth.png"),
        ]);

        const texture = await PIXI.Assets.load(imageModule.default);
        this.sprite = new PIXI.Sprite(texture);

        this.originalImageWidth = texture.width;
        this.originalImageHeight = texture.height;

        this.scaleSprite();
        this.app.stage.addChild(this.sprite);

        const depthTexture = await PIXI.Assets.load(depthModule.default);
        this.depthMap = new PIXI.Sprite(depthTexture);
        this.depthMap.width = window.innerWidth;
        this.depthMap.height = window.innerHeight;

        this.displacementFilter = new PIXI.DisplacementFilter(this.depthMap);
        this.displacementFilter.scale.x = 0;
        this.displacementFilter.scale.y = 0;

        this.app.stage.filters = [this.displacementFilter];

        // Only add mouse move listener on desktop
        if (!this.isMobile) {
          window.addEventListener("mousemove", this.handleMouseMove);
        }

        window.addEventListener("resize", this.handleResize);
      } catch (error) {
        console.error("Error initializing PixiJS:", error);
      }
    },

    scaleSprite() {
      const windowRatio = window.innerWidth / window.innerHeight;
      const imageRatio = this.originalImageWidth / this.originalImageHeight;

      if (windowRatio > imageRatio) {
        this.sprite.width = window.innerWidth;
        this.sprite.height = window.innerWidth / imageRatio;
      } else {
        this.sprite.height = window.innerHeight;
        this.sprite.width = window.innerHeight * imageRatio;
      }

      this.sprite.x = (window.innerWidth - this.sprite.width) / 2;
      this.sprite.y = (window.innerHeight - this.sprite.height) / 2;
    },

    handleMouseMove(e) {
      if (this.displacementFilter && !this.isMobile) {
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;

        this.displacementFilter.scale.x = (centerX - e.clientX) / 20;
        this.displacementFilter.scale.y = (centerY - e.clientY) / 20;
      }
    },

    handleResize() {
      if (this.app && this.sprite) {
        this.app.screen.width = window.innerWidth;
        this.app.screen.height = window.innerHeight;

        this.scaleSprite();

        if (this.depthMap) {
          this.depthMap.width = window.innerWidth;
          this.depthMap.height = window.innerHeight;
        }

        this.app.render();
      }
    },
  },
  mounted() {
    this.drawPixi();
  },
  beforeUnmount() {
    if (this.app) {
      window.removeEventListener("resize", this.handleResize);
      if (!this.isMobile) {
        window.removeEventListener("mousemove", this.handleMouseMove);
      }
      this.app.destroy(true);
    }
  },
};
</script>

<style scoped>
.pixi-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
}

canvas {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
