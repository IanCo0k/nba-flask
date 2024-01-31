document.getElementById('playerSelect').addEventListener('input', function() {
    var inputVal = this.value.toLowerCase();
    var options = this.options;
    for (var i = 0; i < options.length; i++) {
        var optionVal = options[i].text.toLowerCase();
        if (optionVal.includes(inputVal)) {
            options[i].style.display = "";
        } else {
            options[i].style.display = "none";
        }
    }
});