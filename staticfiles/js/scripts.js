document.addEventListener("DOMContentLoaded", function () {
  
    
    // Toggle comment input field
    document.querySelector('.comment-toggle-btn').addEventListener('click', function () {
        let commentSection = document.querySelector('.comment-section');
        commentSection.style.display = commentSection.style.display === "none" ? "block" : "none";
    });

    // Add comment functionality
    document.querySelector('.add-comment').addEventListener('click', function () {
        let commentInput = document.querySelector('.comment-input');
        let commentText = commentInput.value.trim();
        let commentList = document.querySelector('.comment-list');
        let commentCount = document.querySelector('.comment-count');
        let viewCommentsBtn = document.querySelector('.view-comments');

        if (commentText !== "") {
            let commentItem = document.createElement("li");
            commentItem.classList.add("comment-item");

            commentItem.innerHTML = `
                <div class="d-flex align-items-center">
                    <strong>Jane Doe</strong>
                    <span class="ms-auto">
                        <button class="btn btn-sm like-comment-btn"><i class="bi bi-hand-thumbs-up"></i> <span class="like-count">0</span></button> 
                        <button class="btn btn-sm reply-btn">Reply</button>
                    </span>
                </div>
                <p class="mt-1">${commentText}</p>
                <ul class="reply-list list-unstyled reply-section"></ul>
                <div class="reply-section mt-2" style="display: none;">
                    <div class="input-group">
                        <input type="text" class="form-control reply-input" placeholder="Write a reply...">
                        <button class="btn btn-secondary add-reply">Reply</button>
                    </div>
                </div>
            `;

            commentList.appendChild(commentItem);
            commentInput.value = "";

            // Update comment count
            commentCount.textContent = parseInt(commentCount.textContent) + 1;

            // Show "More Comments" button
            viewCommentsBtn.style.display = "block";
        }
    });

    // Event delegation for dynamically added like and reply buttons
    document.querySelector('.comment-list').addEventListener('click', function (event) {
        if (event.target.closest('.like-comment-btn')) {
            let likeBtn = event.target.closest('.like-comment-btn');
            let likeCount = likeBtn.querySelector('.like-count');
            let icon = likeBtn.querySelector('i');
            let count = parseInt(likeCount.textContent);

            if (icon.classList.contains('bi-hand-thumbs-up')) {
                icon.classList.replace('bi-hand-thumbs-up', 'bi-hand-thumbs-up-fill');
                likeBtn.classList.add('text-primary');
                likeCount.textContent = count + 1;
            } else {
                icon.classList.replace('bi-hand-thumbs-up-fill', 'bi-hand-thumbs-up');
                likeBtn.classList.remove('text-primary');
                likeCount.textContent = Math.max(0, count - 1);
            }
        }

        if (event.target.classList.contains('reply-btn')) {
            let replySection = event.target.closest('.comment-item').querySelector('.reply-section');
            replySection.style.display = replySection.style.display === "none" ? "block" : "none";
        }

        if (event.target.classList.contains('add-reply')) {
            let commentItem = event.target.closest('.comment-item');
            let replyInput = commentItem.querySelector('.reply-input');
            let replyText = replyInput.value.trim();
            let replyList = commentItem.querySelector('.reply-list');

            if (replyText !== "") {
                let replyItem = document.createElement("li");
                replyItem.classList.add("p-2", "bg-white", "mt-1", "rounded");
                replyItem.innerHTML = `
                    <div class="d-flex align-items-center">
                        <strong>Another User</strong>
                        <span class="ms-auto">
                            <button class="btn btn-sm like-comment-btn"><i class="bi bi-hand-thumbs-up"></i> <span class="like-count">0</span></button>
                        </span>
                    </div>
                    <p class="mt-1">${replyText}</p>
                `;

                replyList.appendChild(replyItem);
                replyInput.value = "";
            }
        }
    });

    // Toggle view comments
    document.querySelector('.view-comments').addEventListener('click', function () {
        let commentList = document.querySelector('.comment-list');
        if (commentList.style.display === "none") {
            commentList.style.display = "block";
            this.textContent = "Hide Comments";
        } else {
            commentList.style.display = "none";
            this.textContent = "More Comments";
        }
    });
});
  // Like button for the main post

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.like-btn').forEach(button => {
        button.addEventListener('click', function () {
            let likeCount = this.querySelector('.like-count');
            let count = parseInt(likeCount.textContent);
            let icon = this.querySelector('i');

            if (icon.classList.contains('bi-hand-thumbs-up')) {
                icon.classList.replace('bi-hand-thumbs-up', 'bi-hand-thumbs-up-fill');
                this.classList.add('text-primary');
                likeCount.textContent = count + 1;
            } else {
                icon.classList.replace('bi-hand-thumbs-up-fill', 'bi-hand-thumbs-up');
                this.classList.remove('text-primary');
                likeCount.textContent = Math.max(0, count - 1);
            }
        });
    });
});

//Follow system
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".follow-btn").forEach(button => {
        button.addEventListener("click", function() {
            let userId = this.getAttribute("data-user-id");
            let buttonElement = this;
            
            fetch(`/follow/${userId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": getCookie("csrftoken"),
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "followed") {
                    buttonElement.textContent = "Connected";
                    buttonElement.classList.remove("btn-primary");
                    buttonElement.classList.add("btn-success");
                } else {
                    buttonElement.textContent = "Connect +";
                    buttonElement.classList.remove("btn-success");
                    buttonElement.classList.add("btn-primary");
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});

// Function to get CSRF token for Django AJAX requests
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        let cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}