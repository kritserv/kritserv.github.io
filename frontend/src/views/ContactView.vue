<template>
  <div class="contact">
    <h1 class="primary-color">Contact</h1>

    <table>
      <tbody>
        <tr>
          <td>
            <i class="sprite github"></i>
          </td>
          <td>kritserv</td>
          <td>
            <a
              href="https://github.com/kritserv"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
        </tr>
        <tr>
          <td>
            <i class="sprite linkedin"></i>
          </td>
          <td>Krittipoom Phalachun</td>
          <td>
            <a
              href="https://www.linkedin.com/in/krittipoom2001"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
        </tr>
        <tr>
          <td>
            <i class="sprite email"></i>
          </td>
          <td>kritserv[at]gmail.com</td>
          <td></td>
        </tr>
        <tr>
          <td>
            <i class="sprite line"></i>
          </td>
          <td>qwermark111</td>
          <td></td>
        </tr>
        <tr>
          <td>
            <i class="sprite stackoverflow"></i>
          </td>
          <td>kritserv</td>
          <td>
            <a
              href="https://stackoverflow.com/users/21557915/kritserv"
              target="_blank"
              class="sprite openinnewtab"
            ></a>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.contact {
  margin-top: 65px;
  max-width: fit-content;
  margin-left: auto;
  margin-right: auto;
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
i {
  zoom: 0.3;
}
.linkedin {
  background: url("../assets/spritesheet.png") -384px -384px;
}
.email {
  background: url("../assets/spritesheet.png") -512px -384px;
}
.line {
  background: url("../assets/spritesheet.png") -640px -384px;
}
.stackoverflow {
  background: url("../assets/spritesheet.png") -768px -384px;
}
</style>
