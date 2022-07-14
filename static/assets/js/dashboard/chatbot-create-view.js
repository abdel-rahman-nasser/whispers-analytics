const btn = document.querySelector(".add-new-topic");
let topics_rows_counter = 1;

btn.addEventListener("click", () => {
	const clone = $(".original-topics-row").clone();
	clone.removeClass("original-topics-row");
	clone.find(".btn-danger").show();
	
	let new_row_value = +topics_rows_counter + 1;

	clone.attr('id', 'accordionTopic' + new_row_value);
	clone.find('[data-target^="#topic"]')
		.attr('data-target', '#topic' + new_row_value)

	clone.find('[id^="topic"]')
		.attr('id', 'topic' + new_row_value)
		.attr('data-parent', '#accordionTopic' + new_row_value);

	clone.find('.card-header section .title').text('Topic #' + new_row_value);
	clone.find('[name^="topic_"]').each(function () {
		const el = $(this);
		const name = el.attr("name");
		const newName = name.replace(/\d+/, () => {
			return new_row_value;
		});
		el.val('')
		el.attr("name", newName);
	});
	topics_rows_counter = new_row_value;
	$('[name="number_of_rows"]').val(topics_rows_counter);
	// clone.css('margin-top', '20px');
	$(".single-topic-row:last").after(clone);
});

$("body").delegate(".remove-topic", "click", function () {
	$(this).parents(".single-topic-row").remove();
});
