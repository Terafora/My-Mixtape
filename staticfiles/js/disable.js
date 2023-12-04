document.addEventListener('DOMContentLoaded', function() {
    /**
     * Disables add button add mixtape with a 2-second delay
     */
    const addMixBtn = document.getElementById('addmixbtn');
    console.log(addMixBtn);
    
    addMixBtn.addEventListener('click', function() {
        setTimeout(function() {
            addMixBtn.disabled = true;
        }, 5000); // 2000 milliseconds = 2 seconds
    });
});
