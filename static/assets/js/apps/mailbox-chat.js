let chat_bot_id = null;

$(".delete-bot-btn").on("click", function (event) {
	event.stopPropagation();
	var botID = $(this).attr("data-bot-id");
	var parentEl = $(this).parents(".person");

	$.ajax({
		type: "POST",
		enctype: "multipart/form-data",
		url: "/chat_bot/delete-bot/",
		data: {
			bot_id: botID,
		},
		success: (res) => {
			console.log(res);
			parentEl.remove();
		},
	});
});

$(".user-list-box .person").on("click", function (event) {
	if ($(this).hasClass(".active")) {
		return false;
	} else {
		// reset chat box
		$(".chat").html(`<div class="bubble you">Hey there, I'm a chatbot created for you.</div><div class="bubble you">send me anything you want to talk about.</div>`);
		var botID = $(this).attr("data-bot-id");
		chat_bot_id = botID;

		// console.log(botID)
		// try {
		// 	// activate the chatbot from the backend
		// 	$.ajax({
		// 		type: "POST",
		// 		enctype: "multipart/form-data",
		// 		url: "/chat_bot/activate-bot/",
		// 		data: {
		// 			bot_id: botID,
		// 		},
		// 		success: (res) => {
		// 			console.log(res);
		// 		},
		// 	});

		// } catch (error) {

		// }

		var personName = $(this).find(".user-name").text();
		var personImage = $(this).find("img").attr("src");
		var hideTheNonSelectedContent = $(this)
			.parents(".chat-system")
			.find(".chat-box .chat-not-selected")
			.hide();
		var showChatInnerContent = $(this)
			.parents(".chat-system")
			.find(".chat-box .chat-box-inner")
			.show();

		if (window.innerWidth <= 767) {
			$(".chat-box .current-chat-user-name .name").html(
				personName.split(" ")[0]
			);
		} else if (window.innerWidth > 767) {
			$(".chat-box .current-chat-user-name .name").html(personName);
		}
		$(".chat-box .current-chat-user-name img").attr("src", personImage);
		$(".chat").removeClass("active-chat");
		$(".user-list-box .person").removeClass("active");
		$(".chat-box .chat-box-inner").css("height", "100%");
		$(".chat-box .overlay-phone-call").css("display", "block");
		$(".chat-box .overlay-video-call").css("display", "block");
		$(this).addClass("active");
		$(".chat").addClass("active-chat");
	}
	if ($(this).parents(".user-list-box").hasClass("user-list-box-show")) {
		$(this).parents(".user-list-box").removeClass("user-list-box-show");
	}
	$(".chat-meta-user").addClass("chat-active");
	$(".chat-box").css("height", "calc(100vh - 158px)");
	$(".chat-footer").addClass("chat-active");

	new PerfectScrollbar(".chat-conversation-box", {
		suppressScrollX: true,
	});

	const getScrollContainer = document.querySelector(".chat-conversation-box");
	getScrollContainer.scrollTop = 0;
});

// const ps = new PerfectScrollbar(".people", {
// 	suppressScrollX: true,
// });

$(".mail-write-box").on("keydown", function (event) {
	if (event.key === "Enter") {
		var chatInput = $(this);
		var botID = $(this).attr("data-bot-id");
		var chatMessageValue = chatInput.val();
		if (chatMessageValue === "") {
			return;
		}
		renderMessage(chatInput, chatMessageValue);

		// send message to server
		$.ajax({
			type: "POST",
			enctype: "multipart/form-data",
			url: "/chat_bot/get-bot-response/",
			data: {
				msg: chatMessageValue,
				bot_id: chat_bot_id,
			},
			success: (res) => {
				renderMessage(chatInput, res.response, "you");
			},
		});
	}
});

function renderMessage(parent, chatMessageValue, chatMessageType = "me") {
	console.log(chatMessageValue, chatMessageType);
	$messageHtml =
		'<div class="bubble ' +
		chatMessageType +
		'">' +
		chatMessageValue +
		"</div>";
	var appendMessage = parent
		.parents(".chat-system")
		.find(".active-chat")
		.append($messageHtml);
	const getScrollContainer = document.querySelector(".chat-conversation-box");
	getScrollContainer.scrollTop = getScrollContainer.scrollHeight;
	$(".mail-write-box").val("");
}

$(".hamburger, .chat-system .chat-box .chat-not-selected p").on(
	"click",
	function (event) {
		$(this)
			.parents(".chat-system")
			.find(".user-list-box")
			.toggleClass("user-list-box-show");
	}
);
