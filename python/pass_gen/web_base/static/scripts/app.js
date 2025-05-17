document.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll("nav a");
  const content = document.getElementById("app-content");

  function setActiveRoute(route) {
    links.forEach(link => {
      if (link.dataset.route === route) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });
  }

  function loadRoute(route) {
    setActiveRoute(route);
    fetch(`/${route === "home" ? "" : route}`)
      .then(res => res.text())
      .then(html => {
        content.innerHTML = html;

        if (route === "generator") {
          setupGeneratorForm();
        }
      });
  }

  function setupGeneratorForm() {
    const form = document.getElementById("password-form");
    const output = document.getElementById("password-output");
    const copyBtn = document.getElementById("copy-btn");

    copyBtn.disabled = true;

    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const length = parseInt(form.length.value);
      const use_upper = form.use_upper.checked;
      const use_lower = form.use_lower.checked;
      const use_digits = form.use_digits.checked;
      const use_symbols = form.use_symbols.checked;

      if (!use_upper && !use_lower && !use_digits && !use_symbols) {
        alert("Select at least one character type!");
        return;
      }
      if (length < 1) {
        alert("Length must be a positive number!");
        return;
      }

      const response = await fetch("/api/generate_password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ length, use_upper, use_lower, use_digits, use_symbols }),
      });
      const data = await response.json();

      if (data.error) {
        alert(data.error);
        output.textContent = "";
        copyBtn.disabled = true;
      } else {
        output.textContent = data.password;
        copyBtn.disabled = false;
      }
    });

    copyBtn.addEventListener("click", () => {
      if (output.textContent) {
        navigator.clipboard.writeText(output.textContent);
        alert("Password copied to clipboard!");
      }
    });
  }

  // Initial load
  loadRoute("home");

  // SPA style nav
  links.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const route = link.dataset.route;
      loadRoute(route);
    });
  });
});
