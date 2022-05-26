$.ajax({
    type: "GET",
    url : "user_data_applying",
    data: {
        'name': $("#name").val(),
    }

    dataType:"text",

    cache:false,
    success: function(data)
    {
        if (data == 'ok')
            {}
        else if (data == 'no')
            {}
    }
})
