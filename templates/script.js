$(document).ready(function() {
    $("#send-button").click(function() {
        var message = $("#chat-input").val();
        sendMessage(message);
    });

    $("#chat-input").keypress(function(event) {
        if (event.which == 13) {
            var message = $("#chat-input").val();
            sendMessage(message);
        }
    });

    function sendMessage(message) {
        if (message.trim() !== "") {
            $("#chat-messages").append("<p class='user-message'>" + message + "</p>");
            $("#chat-input").val("");

            $.ajax({
                url: "/chat",
                type: "POST",
                data: { chat: message },
                success: function(response) {
                    $("#chat-messages").append("<p class='bot-message'>" + response + "</p>");
                },
                error: function(xhr, status, error) {
                    console.log("Error:", error);
                }
            });
        }
    }
});
