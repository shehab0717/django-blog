tagForm = document.getElementById('tag-form')

if(tagForm)
    tagForm.onsubmit = form_submit

$('.reply-btn').each(function () {
    var $this = $(this);
    $this.on("click", function () {
        showReplyForm($($this).data('comment-id'))
    });
});

$(".hide").hide()

function showReplyForm(commentId){
    $form = $(`#reply-form-${commentId}`)
    $form.show()
    commentInput = document.getElementById(`comment-id-${commentId}`)
    commentInput.value = commentId
}

    
function form_submit(event){
    form = event.target
    tagName = form[1].value
    csrf_token = form[0].value
    console.log(tagName)
    $.ajax({
        type: "POST",
        url: '/admin/tag/create',
        data: {
            name: tagName,
            csrfmiddlewaretoken: csrf_token
        },
        success: ()=> $('#tagFormModal').modal('toggle')
      });
    return false
}

