// chat.js
document.addEventListener("DOMContentLoaded", function() {
    const chatIcon = document.getElementById("chatIcon");
    const messagingSection = document.querySelector(".messaging-section");
    
    chatIcon.addEventListener("click", function() {
        messagingSection.classList.toggle("show");
    });
});
