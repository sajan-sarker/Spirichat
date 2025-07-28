function sendMessage() {
  const inputField = document.getElementById("chat-input");
  const message = inputField.value.trim();
  if (!message) return;

  const chatBody = document.getElementById("chat-body");

  // Add user's message with avatar
  const userMessage = document.createElement("div");
  userMessage.className = "message user";
  userMessage.innerHTML = `
    <div class="user-avatar"></div>
    <div class="bubble">${message}</div>
    <span class="timestamp">${getCurrentTime()}</span>
  `;
  chatBody.appendChild(userMessage);
  inputField.value = "";

  chatBody.scrollTop = chatBody.scrollHeight;

  // Send to backend
  fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message }),
  })
    .then((res) => res.json())
    .then((data) => {
      const botMessage = document.createElement("div");
      botMessage.className = "message bot";
      botMessage.innerHTML = `
        <div class="bot-avatar"></div>
        <div class="bubble">${data.response.replace(/\n/g, "<br>")}</div>
        <span class="timestamp">${getCurrentTime()}</span>
      `;
      chatBody.appendChild(botMessage);
      chatBody.scrollTop = chatBody.scrollHeight;
    })
    .catch((err) => {
      const errorMessage = document.createElement("div");
      errorMessage.className = "message bot";
      errorMessage.innerHTML = `
        <div class="bot-avatar"></div>
        <div class="bubble">Something went wrong. Please try again.</div>
        <span class="timestamp">${getCurrentTime()}</span>
      `;
      chatBody.appendChild(errorMessage);
      chatBody.scrollTop = chatBody.scrollHeight;
    });
}

function getCurrentTime() {
  const now = new Date();
  return now.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

// Trigger sendMessage() when Enter is pressed
document.getElementById("chat-input").addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    e.preventDefault(); // Prevent newline (if textarea) or form submission
    sendMessage();
  }
});
