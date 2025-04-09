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
    const passwordField = document.querySelector("#password");
    const passwordField1 = document.querySelector("#password1");
    const showPasswordToggle = document.querySelector(".showPasswordToggle");
	const showConfirmPasswordToggle = document.querySelector(".showConfirmPasswordToggle");
	const toggleIcon = document.querySelector("#toggleIcon");
	const toggleIcon1 = document.querySelector("#toggleIcon1");

    if (showPasswordToggle){
        showPasswordToggle.addEventListener("click", function(){
			const isPassword = passwordField.type === "password";
			passwordField.type === isPassword ? "text" : "password";
			
            if (toggleIcon){
                toggleIcon.classList.toggle("fa-eye");
				toggleIcon.classList.toggle("fa-eye-slash");
            }
        });
    }
	
	if (showConfirmPasswordToggle){
        showConfirmPasswordToggle.addEventListener("click", function(){
			const isPassword1 = passwordField1.type === "password";
			passwordField1.type === isPassword1 ? "text" : "password";
			
            if (toggleIcon1){
                toggleIcon1.classList.toggle("fa-eye");
				toggleIcon1.classList.toggle("fa-eye-slash");
            }
        });
    }
});

