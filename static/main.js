// document.getElementById('pickup-btn').addEventListener('click', function() {
//     var pickupForm = document.getElementById('pickup-form');
//     if (pickupForm.style.display === 'none' || pickupForm.style.display === '') {
//         pickupForm.style.display = 'block';
//     } else {
//         pickupForm.style.display = 'none';
//     }
// });


let requestBtn = document.getElementById("pickup-btn");
requestBtn.addEventListener('click', function(){
    let pickupForm = document.getElementById("pickup-form");
    if (pickupForm.style.display == "none"){
        pickupForm.style.display = 'block';
    }

    document.addEventListener("DOMContentLoaded", function() {
        // Smooth scroll for anchor links
        document.querySelectorAll('ul.linkediting a').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
});

    });
    document.addEventListener("DOMContentLoaded", function() {
        // Smooth scroll for anchor links
        document.querySelectorAll('ul.linkediting a').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();

                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    });