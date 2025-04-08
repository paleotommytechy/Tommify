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

    if (showPasswordToggle){
        showPasswordToggle.addEventListener("click", function(){
            if (passwordField.type === "password"){
                showPasswordToggle.textContent = "HIDE";
                passwordField.type = "text";
                passwordField1.type = "text";
            }else{
                showPasswordToggle.textContent = "SHOW";
                passwordField.type = "password";
                passwordField1.type = "password";
            }
        });
    }else{
        console.error("Element with class 'showPasswordToggle' not found");
    }
});

