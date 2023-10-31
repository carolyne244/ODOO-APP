// Mock data for initial messages
const initialMessages = [
    { text: "Hello!", sender: "client", timestamp: new Date() },
    { text: "Hi there!", sender: "server", timestamp: new Date() }
];

// Function to display messages
function displayMessages(messages) {
    const messagesDiv = document.querySelector('.messages');
    messagesDiv.innerHTML = '';

    messages.forEach(message => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', message.sender);
        messageDiv.innerHTML = `
            <p class="message-text">${message.text}</p>
            <p class="message-time">${message.timestamp.toLocaleTimeString()}</p>
        `;
        messagesDiv.appendChild(messageDiv);
    });
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messageText = messageInput.value.trim();
    
    if (messageText !== '') {
        const newMessage = {
            text: messageText,
            sender: 'client',
            timestamp: new Date()
        };

        initialMessages.push(newMessage);
        displayMessages(initialMessages);

        messageInput.value = ''; 
    }
}

const sendButton = document.getElementById('sendButton');
sendButton.addEventListener('click', sendMessage);

displayMessages(initialMessages);
