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
      // Detect mobile via touch capability and screen size
      this.isMobile =
        ("maxTouchPoints" in navigator && navigator.maxTouchPoints > 0) ||
        window.innerWidth <= 768;
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

        const container = new PIXI.Container();
        container.addChild(this.sprite);
        this.app.stage.addChild(container);

        this.resizeAndPositionSprite(container);

        const depthTexture = await PIXI.Assets.load(depthModule.default);
        this.depthMap = new PIXI.Sprite(depthTexture);

        this.resizeDepthMap();

        this.displacementFilter = new PIXI.DisplacementFilter(this.depthMap);
        this.displacementFilter.scale.x = 0;
        this.displacementFilter.scale.y = 0;

        container.filters = [this.displacementFilter];
        this.app.stage.addChild(this.depthMap);

        if (!this.isMobile) {
          window.addEventListener("mousemove", this.handleMouseMove);
        }
        window.addEventListener("resize", this.handleResize);
      } catch (error) {
        console.error("Error initializing PixiJS:", error);
      }
    },
    resizeAndPositionSprite(container) {
      const windowRatio = window.innerWidth / window.innerHeight;
      const imageRatio = this.originalImageWidth / this.originalImageHeight;

      // Ensure full coverage while maintaining aspect ratio
      if (windowRatio > imageRatio) {
        container.scale.set(window.innerWidth / this.originalImageWidth);
      } else {
        container.scale.set(window.innerHeight / this.originalImageHeight);
      }

      container.x = (window.innerWidth - container.width) / 2;
      container.y = (window.innerHeight - container.height) / 2;
    },
    resizeDepthMap() {
      const container = this.sprite.parent;
      this.depthMap.width = this.originalImageWidth * container.scale.x;
      this.depthMap.height = this.originalImageHeight * container.scale.y;

      this.depthMap.x = container.x;
      this.depthMap.y = container.y;
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

        this.resizeAndPositionSprite(this.sprite.parent);
        this.resizeDepthMap();

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
