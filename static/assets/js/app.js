const title_elem = document.querySelector(".article-title"),
description_elem = document.querySelector(".article-description");

var search = window.location.search.substr(1);

if (search) { 
    var api = "https://en.wikipedia.org/w/api.php?format=json&action=query&origin=*&prop=extracts&exintro&explaintext&redirects=1&titles=" + search;

    fetch(api)
        .then(response => response.json())
        .then(response => {
            response = response.query.pages;
            var pageid = Object.keys(response)[0];
            var extract = response[pageid].extract;
            title_elem.innerHTML = search; 
            description_elem.innerHTML = extract

        })

}