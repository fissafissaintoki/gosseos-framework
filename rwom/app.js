(function () {
  "use strict";
  const worlds = { RASCHELWALD: "world-raschelwald", OPERATORDECK: "world-operator" };

  function activateWorld(target) {
    if (!Object.hasOwn(worlds, target)) return;
    Object.entries(worlds).forEach(([name, id]) => {
      document.getElementById(id).setAttribute("visible", name === target);
    });
    document.getElementById("world-label").setAttribute("value", `AKTIVE WELT: ${target}`);
    localStorage.setItem("kyron.rwom.world", target);
  }

  AFRAME.registerComponent("world-switch", {
    schema: { target: { type: "string" } },
    init() { this.el.addEventListener("click", () => activateWorld(this.data.target)); }
  });

  window.addEventListener("DOMContentLoaded", async () => {
    const scene = document.getElementById("rwom-scene");
    const launch = document.getElementById("launch");
    const button = document.getElementById("enter-vr");
    const state = document.getElementById("xr-state");
    activateWorld(localStorage.getItem("kyron.rwom.world") || "RASCHELWALD");

    if (!navigator.xr || !(await navigator.xr.isSessionSupported("immersive-vr"))) {
      button.textContent = "IM META QUEST BROWSER ÖFFNEN";
      state.textContent = "Immersive WebXR-Unterstützung fehlt.";
      return;
    }

    button.disabled = false;
    button.textContent = "RWOM IN DER BRILLE STARTEN";
    state.textContent = "Quest/WebXR erkannt.";
    button.addEventListener("click", async () => {
      button.disabled = true;
      try { await scene.enterVR(); }
      catch (error) { state.textContent = `Start blockiert: ${error.message}`; button.disabled = false; }
    });
    scene.addEventListener("enter-vr", () => { launch.hidden = true; });
    scene.addEventListener("exit-vr", () => { launch.hidden = false; button.disabled = false; });
  }, { once: true });
})();
