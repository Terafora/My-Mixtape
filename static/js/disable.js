const addMixBtn = document.getElementsByClassName('addmixbtn')[0];
let counter = 0;

document.addEventListener('DOMContentLoaded', function() {

/**
* Disables add button on second press
* For preventing duplicate creations
*/
addMixBtn.addEventListener('click', function() {
    if(counter == 1){
        addMixBtn.disabled = true;
    } else {
        counter++;
    }
    });
});