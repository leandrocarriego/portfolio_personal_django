document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");

    if (form) {
        form.querySelectorAll("label").forEach(label => {
            label.classList.add("block", "text-zinc-200", "font-bold", "mb-2");
        });

        form.querySelectorAll("input, textarea").forEach(input => {
            input.classList.add("bg-zinc-900", "appearance-none", "border-b-2", "border-gray-400", "text-zinc-200", "leading-tight", "focus:outline-none", "focus:bg-zinc-800", "focus:border-[#26a699]", "focus:rounded", "border-gray-300", "block", "w-full",  "shadow-sm", "p-2", "mb-6");
        });
    }
});