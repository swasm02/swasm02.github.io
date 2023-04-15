function fetch_data() {
    var file_location = "https://drive.google.com/uc?id=1tswwNfrNDx6_xIVpPLKJijKHcZTpeBu4&export=download";

    var json_data = fetch(file_location)
        .then((response) => response.json())
        .then((json) => {return json});
        
    console.log(json_data[0].date)

    document.getElement
}