document.addEventListener("DOMContentLoaded", function () {
    const continueButton = document.querySelector('.continue-button');
    const signUpButton = document.querySelector('.sign-button');

    continueButton.addEventListener('click', function () {
        alert("Continuing to the next step!");
        // You can redirect to another page if needed
        // window.location.href = "next-step.html";
    });

    signUpButton.addEventListener('click', function () {
        alert("Sign up form will open!");
        // You can redirect to the signup page
        // window.location.href = "signup.html";
    });
});
