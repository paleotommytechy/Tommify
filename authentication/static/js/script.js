function toggleMode() {
    document.body.classList.toggle("dark-mode");
    let btn = document.querySelector(".toggle-mode");
    if (document.body.classList.contains("dark-mode")) {
        btn.innerHTML = "☀️";
    } else {
        btn.innerHTML = "🌙";
    }
}

// hide and show toggle
document.addEventListener("DOMContentLoaded", function(){
    const passwordField = document.querySelector(".password");
    const passwordField1 = document.querySelector(".password1");
    const showPasswordToggle = document.querySelector(".showPasswordToggle");
	const showConfirmPasswordToggle = document.querySelector(".showConfirmPasswordToggle");
	const toggleIcon = document.querySelector("#toggleIcon");
	const toggleIcon1 = document.querySelector("#toggleIcon1");

    if (showPasswordToggle){
        showPasswordToggle.addEventListener("click", function(){
			passwordField.type = passwordField.type === "password" ? "text" : "password";
			toggleIcon.classList.toggle("fa-eye");
			toggleIcon.classList.toggle("fa-eye-slash");
        });
    }
	
	if (showConfirmPasswordToggle){
        showConfirmPasswordToggle.addEventListener("click", function(){
			passwordField1.type = passwordField1.type === "password" ? "text" : "password";
			toggleIcon1.classList.toggle("fa-eye");
			toggleIcon1.classList.toggle("fa-eye-slash");
        });
    }
});

