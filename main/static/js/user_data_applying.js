$("#button").on("click", function(){
    $.ajax({
        type: "POST",
        url : "user_data_applying",
        data: {
            "name": $("#name").val(),
            "surname": $("#surname").val(),
            "numberPhone": $("#numberPhone").val(),
            "userEmail": $("#userEmail").val(),
            "country": $("#country").val(),
        },

        dataType:"text",

        // cache:false,
        success: function(data)
        {
            alert(data);
        },
    });
    return false;
});
