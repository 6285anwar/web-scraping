const searchInput = document.querySelector(".search-input");

searchInput.addEventListener("keyup", function(e){
    if (e.keyCode === 13){
        var value = searchInput.value;
        if (value)
        $(document).on('click', '.alink', function () {
            var url = $("#Url").attr("data-url") + value;
        }); 

    }

})