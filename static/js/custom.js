document.addEventListener('DOMContentLoaded', function() {
    const swalMessage = document.getElementById('swal-message');
    if (swalMessage) {
        const context = swalMessage.getAttribute('data-context');
        const message = swalMessage.getAttribute('data-message');

        Swal.fire({
            title: 'Success!',
            text: message,
            icon: 'success',
            confirmButtonText: 'OK'
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const swalMessage = document.getElementById('swal-message');
    if (swalMessage) {
        const context = swalMessage.getAttribute('data-context');
        const message = swalMessage.getAttribute('data-message');

        if (context === 'contact') {
            Swal.fire({
                icon: 'success',
                title: 'Success!',
                text: message,
                confirmButtonText: 'OK'
            });
        }
    }
});


    document.addEventListener('DOMContentLoaded', function () {
        const toggleBtn = document.getElementById('toggle-comments');
        const moreComments = document.getElementById('more-comments');

        if (toggleBtn) {
            toggleBtn.addEventListener('click', function (e) {
                e.preventDefault();
                if (moreComments.style.display === "none") {
                    moreComments.style.display = "block";
                    toggleBtn.textContent = "Show less";
                } else {
                    moreComments.style.display = "none";
                    toggleBtn.textContent = "See all comments";
                }
            });
        }
    });


document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggle-comments");
    const moreComments = document.getElementById("more-comments");

    if (toggleBtn && moreComments) {
        toggleBtn.addEventListener("click", function (e) {
            e.preventDefault();
            if (moreComments.style.display === "none") {
                moreComments.style.display = "block";
                toggleBtn.textContent = "Hide comments";
            } else {
                moreComments.style.display = "none";
                toggleBtn.textContent = "See all comments";
            }
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.toggle-replies');
    buttons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const id = btn.getAttribute('data-id');
            const moreReplies = document.getElementById(`more-replies-${id}`);
            if (moreReplies.style.display === "none") {
                moreReplies.style.display = "block";
                btn.textContent = "Hide replies";
            } else {
                moreReplies.style.display = "none";
                btn.textContent = "Show all replies";
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const toggleCommentsBtn = document.getElementById('toggle-comments');
    const moreCommentsDiv = document.getElementById('more-comments');

    if (toggleCommentsBtn && moreCommentsDiv) {
        toggleCommentsBtn.addEventListener('click', function (e) {
            e.preventDefault();
            if (moreCommentsDiv.style.display === 'none') {
                moreCommentsDiv.style.display = 'block';
                toggleCommentsBtn.textContent = 'Hide comments';
            } else {
                moreCommentsDiv.style.display = 'none';
                toggleCommentsBtn.textContent = 'Show all comments';
            }
        });
    }

    // Same for replies toggle
    const replyButtons = document.querySelectorAll('.toggle-replies');
    replyButtons.forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            const commentId = this.dataset.id;
            const repliesDiv = document.getElementById('more-replies-' + commentId);
            if (repliesDiv.style.display === 'none') {
                repliesDiv.style.display = 'block';
                this.textContent = 'Hide replies';
            } else {
                repliesDiv.style.display = 'none';
                this.textContent = 'Show all replies';
            }
        });
    });
});







