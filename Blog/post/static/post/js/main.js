tagForm = document.getElementById('tag-form')

tagForm.onsubmit = form_submit


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

