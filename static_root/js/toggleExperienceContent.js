let currentDivId = null;

function toggleExperienceContent(experienceId) {
  const divToOpen = document.getElementById(`js-${experienceId}`);
  const arrowDownToOpen = document.getElementById(
    `js-arrowDown-${experienceId}`
  );
  const arrowUpToOpen = document.getElementById(`js-arrowUp-${experienceId}`);

  // Si son iguales significa que se pide abrir el que esta visible
  if (currentDivId === experienceId) {
    divToOpen.classList.add("hidden");
    arrowDownToOpen.classList.remove("hidden");
    arrowUpToOpen.classList.add("hidden");
    currentDivId = null;
  } else {
    // Si hay alguno abierto lo cerramos
    if (currentDivId !== null) {
      const currentDivOpen = document.getElementById(`js-${currentDivId}`);
      const currentArrowUp = document.getElementById(
        `js-arrowUp-${currentDivId}`
      );
      const currentArrowDown = document.getElementById(
        `js-arrowDown-${currentDivId}`
      );
      currentDivOpen.classList.add("hidden");
      currentArrowUp.classList.add("hidden");
      currentArrowDown.classList.remove("hidden");
    }

    divToOpen.classList.toggle("hidden");
    arrowDownToOpen.classList.toggle("hidden");
    arrowUpToOpen.classList.toggle("hidden");
    currentDivId = experienceId;
  }
}
