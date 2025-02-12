<template>
  <section>
    <div class="pixi-container">
      <img
        src="../assets/card.jpg"
        alt="Card"
        class="fallback-image"
        :class="{ show: isTouchDevice }"
      />
      <canvas
        ref="pixiCanvas"
        class="desktop-canvas"
        :class="{ hide: isTouchDevice }"
      ></canvas>
    </div>
  </section>
  <section id="work">
    <br /><br /><br /><br />
    <h1>Work</h1>

    <h3 class="primary-color">Python Programmer</h3>
    <h4>
      บริษัท เอ็ม.ดี.ซอฟต์ จำกัด - M.D.Soft Co.,Ltd. (May 2024 - Feb 2025)
    </h4>
    <table>
      <tbody>
        <tr>
          <th scope="row">Project</th>
          <th scope="row">Detail</th>
          <th scope="row">Skills</th>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
          <td>...</td>
        </tr>
      </tbody>
    </table>

    <h3 class="primary-color">Backend Developer (Internship)</h3>
    <h4>
      บริษัท อมรินทร์ คอร์เปอเรชั่นส์ จำกัด (มหาชน) - Amarin (July 2023 - Oct
      2023)
    </h4>
    <table>
      <tbody>
        <tr>
          <th scope="row">Project</th>
          <th scope="row">Detail</th>
          <th scope="row">Skills</th>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
          <td>...</td>
        </tr>
      </tbody>
    </table>
    <br /><br /><br /><br />
    <h1>Personal project</h1>

    <table>
      <tbody>
        <tr>
          <th scope="row">Project</th>
          <th scope="row">Detail</th>
          <th scope="row">Skills</th>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a
            ><a
              href="https://www.google.com/"
              target="_blank"
              class="sprite github"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a
            ><a
              href="https://www.google.com/"
              target="_blank"
              class="sprite github"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a
            ><a
              href="https://www.google.com/"
              target="_blank"
              class="sprite github"
            ></a>
          </td>
          <td>...</td>
        </tr>
        <tr>
          <td>
            <img class="project-img" src="https://placehold.jp/250x150.png" />
          </td>
          <td>
            ...<a
              href="https://www.google.com/"
              target="_blank"
              class="sprite openinnewtab"
            ></a
            ><a
              href="https://www.google.com/"
              target="_blank"
              class="sprite github"
            ></a>
          </td>
          <td>...</td>
        </tr>
      </tbody>
    </table>
    <br /><br /><br /><br /><br />

    <hr />
    <h1>My skillset</h1>
    <h3 class="primary-color">Preferred languages and framework</h3>
    <table>
      <tbody>
        <tr>
          <th scope="row"></th>
          <th scope="row">Framework</th>
          <th scope="row">Usage</th>
        </tr>
        <tr>
          <td>
            <i class="sprite main-skill-icon skill-icon python"></i>python
          </td>
          <td>
            <i class="sprite skill-icon flask"></i> flask
            <i class="sprite skill-icon django"></i> django
            <i class="sprite skill-icon pandas"></i> pandas
            <i class="sprite skill-icon scikitlearn"></i> scikit-learn
            <i class="sprite skill-icon jupyternotebook"></i> jupyter notebook
            <i class="sprite skill-icon pygame"></i> pygame
          </td>
          <td>
            Backend, Data analysis, Data transformation, Data migration, Machine
            learning, Game development
          </td>
        </tr>
        <tr>
          <td><i class="sprite skill-icon javascript"></i> javascript</td>
          <td><i class="sprite skill-icon vue"></i> vue</td>
          <td>Frontend</td>
        </tr>
      </tbody>
    </table>
    <hr />
    <br /><br />
    <div class="skills-grid">
      <div class="skills-item">
        <h3 class="primary-color">Other Known Languages</h3>
        <table>
          <tbody>
            <tr>
              <th scope="row"></th>
              <th scope="row">Usage</th>
            </tr>
            <tr>
              <td><i class="sprite skill-icon go"></i> go</td>
              <td>Backend</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon r"></i> r</td>
              <td>Data analysis</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon linux"></i> bash</td>
              <td>Automation</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="skills-item">
        <h3 class="primary-color">Linux Distribution</h3>
        <table>
          <tbody>
            <tr>
              <th scope="row"></th>
              <th scope="row">Usage</th>
            </tr>
            <tr>
              <td><i class="sprite skill-icon ubuntu"></i> ubuntu</td>
              <td>Server, docker container, github action</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon fedora"></i> fedora</td>
              <td>Programming</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon linuxmint"></i> linux mint</td>
              <td>Daily Driver</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="skills-item">
        <h3 class="primary-color">Other Tools</h3>
        <table>
          <tbody>
            <tr>
              <th scope="row"></th>
              <th scope="row">Usage</th>
            </tr>
            <tr>
              <td>
                <i class="sprite skill-icon html"></i> html
                <i class="sprite skill-icon css"></i> css
              </td>
              <td>Frontend, create static website</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon docker"></i> docker</td>
              <td>Build, share and run web application</td>
            </tr>
            <tr>
              <td><i class="sprite skill-icon git"></i> git</td>
              <td>Version control, open-source and contribution</td>
            </tr>
            <tr>
              <td>
                <i class="sprite skill-icon aws"></i> aws (lightsail)<i
                  class="sprite skill-icon pythonanywhere"
                ></i>
                pythonanywhere
              </td>
              <td>Deploy web application</td>
            </tr>
            <tr>
              <td>
                <i class="sprite skill-icon postgres"></i> postgres
                <i class="sprite skill-icon mysql"></i> mysql
                <i class="sprite skill-icon sqlite"></i> sqlite
              </td>
              <td>Database</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="skills-item">
        <h3 class="primary-color">Software</h3>
        <table>
          <tbody>
            <tr>
              <th scope="row"></th>
              <th scope="row">Usage</th>
            </tr>
            <tr>
              <td>
                <i class="sprite skill-icon tableau"></i> tableau<i
                  class="sprite skill-icon powerbi"
                ></i>
                ms power bi
              </td>
              <td>Data Dashboard</td>
            </tr>
            <tr>
              <td>
                <i class="sprite skill-icon photoshop"></i> adobe photoshop
              </td>
              <td>Graphic editor</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <br /><br />
    <hr />
  </section>
  <section id="education">
    <br /><br /><br /><br />
    <h1 class="primary-color">Education</h1>
    <h4>
      Bachelor's in Data Science (<span class="primary-color">3.61 GPA</span>,
      Silpakorn Sanamchandra)
    </h4>
    <h4>Mostly self taught.</h4>

    <br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
  </section>
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
      isTouchDevice: false,
    };
  },
  methods: {
    checkTouchDevice() {
      // Check if device supports touch
      this.isTouchDevice =
        "ontouchstart" in window ||
        navigator.maxTouchPoints > 0 ||
        navigator.msMaxTouchPoints > 0;
    },
    async drawPixi() {
      // Don't initialize Pixi.js if it's a touch device
      if (this.isTouchDevice) {
        return;
      }

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

        window.addEventListener("mousemove", this.handleMouseMove);
        window.addEventListener("resize", this.handleResize);
      } catch (error) {
        console.error("Error initializing PixiJS:", error);
      }
    },
    resizeAndPositionSprite(container) {
      const windowRatio = window.innerWidth / window.innerHeight;
      const imageRatio = this.originalImageWidth / this.originalImageHeight;

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
      if (this.displacementFilter) {
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
    this.checkTouchDevice();
    this.drawPixi();
  },
  beforeUnmount() {
    if (this.app) {
      window.removeEventListener("mousemove", this.handleMouseMove);
      window.removeEventListener("resize", this.handleResize);
      this.app.destroy(true);
    }
  },
};
</script>

<style scoped>
.project-img {
  width: clamp(100px, 33vw, 250px);
  height: auto;
}
.pixi-container {
  width: 100vw;
  height: 100vh;
  position: relative;
  overflow: hidden;
  z-index: 2;
}

.fallback-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: none;
}

.fallback-image.show {
  display: block;
}

.desktop-canvas {
  position: absolute;
  top: 0;
  left: 0;
}
table {
  margin-left: auto;
  margin-right: auto;
  border-collapse: collapse;
  width: 80%;
}
th,
td {
  padding: 8px;
}
tr {
  border-bottom: 1px solid #ddd;
  transition: 0.2s;
}
.desktop-canvas.hide {
  display: none;
}
.skills-grid {
  display: grid;
  gap: 2rem;
  width: 100%;
}
.skill-icon {
  margin: 0 auto;
}
@media only screen and (max-width: 600px) {
  .skill-icon {
    zoom: 0.2;
    margin: 0 auto;
  }

  .skills-grid {
    grid-template-columns: 1fr;
  }
}

@media only screen and (min-width: 600px) {
  tr:hover {
    background-color: #2c3e50;
    transition: 0.2s;
  }
  .skill-icon {
    zoom: 0.4;
  }
  .main-skill-icon {
    zoom: 1.2;
  }

  .skills-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media only screen and (min-width: 1100px) {
  .skills-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
.skills-item {
  width: 100%;
}
.python {
  background: url("../assets/spritesheet.png") -768px -0px;
}
.flask {
  background: url("../assets/spritesheet.png") -896px -0px;
}
.django {
  background: url("../assets/spritesheet.png") -1024px -0px;
}
.pandas {
  background: url("../assets/spritesheet.png") -1152px -0px;
}
.scikitlearn {
  background: url("../assets/spritesheet.png") -0px -128px;
}
.jupyternotebook {
  background: url("../assets/spritesheet.png") -128px -128px;
}
.pygame {
  background: url("../assets/spritesheet.png") -256px -128px;
}
.html {
  background: url("../assets/spritesheet.png") -384px -128px;
}
.css {
  background: url("../assets/spritesheet.png") -512px -128px;
}
.javascript {
  background: url("../assets/spritesheet.png") -640px -128px;
}
.vue {
  background: url("../assets/spritesheet.png") -768px -128px;
}
.go {
  background: url("../assets/spritesheet.png") -896px -128px;
}
.r {
  background: url("../assets/spritesheet.png") -1024px -128px;
}
.linux {
  background: url("../assets/spritesheet.png") -1152px -128px;
}
.ubuntu {
  background: url("../assets/spritesheet.png") -0px -256px;
}
.linuxmint {
  background: url("../assets/spritesheet.png") -128px -256px;
}
.fedora {
  background: url("../assets/spritesheet.png") -256px -256px;
}
.docker {
  background: url("../assets/spritesheet.png") -384px -256px;
}
.git {
  background: url("../assets/spritesheet.png") -512px -256px;
}
.aws {
  background: url("../assets/spritesheet.png") -640px -256px;
}
.pythonanywhere {
  background: url("../assets/spritesheet.png") -768px -256px;
}
.postgres {
  background: url("../assets/spritesheet.png") -896px -256px;
}
.mysql {
  background: url("../assets/spritesheet.png") -1024px -256px;
}
.sqlite {
  background: url("../assets/spritesheet.png") -1152px -256px;
}
.tableau {
  background: url("../assets/spritesheet.png") -0px -384px;
}
.powerbi {
  background: url("../assets/spritesheet.png") -128px -384px;
}
.photoshop {
  background: url("../assets/spritesheet.png") -256px -384px;
}
</style>
