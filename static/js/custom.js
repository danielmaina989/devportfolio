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
    // Toggle more replies
    document.querySelectorAll('.toggle-replies').forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const commentId = this.dataset.id;
            const moreReplies = document.getElementById('more-replies-' + commentId);
            if (moreReplies.style.display === 'none') {
                moreReplies.style.display = 'block';
                this.textContent = 'Hide replies';
            } else {
                moreReplies.style.display = 'none';
                this.textContent = 'Show all replies';
            }
        });
    });

    // Toggle all comments
    const toggleCommentsBtn = document.getElementById('toggle-comments');
    const allComments = document.querySelectorAll('.comment-item.depth-1.parent');
    if (toggleCommentsBtn) {
        toggleCommentsBtn.addEventListener('click', function (e) {
            e.preventDefault();
            let showingAll = this.getAttribute('data-showing') === 'true';
            allComments.forEach(function (comment, index) {
                if (index >= 4) {
                    comment.style.display = showingAll ? 'none' : 'block';
                }
            });
            this.textContent = showingAll ? 'Show all comments' : 'Hide comments';
            this.setAttribute('data-showing', (!showingAll).toString());
        });

        // Initially hide comments after the 4th
        allComments.forEach(function (comment, index) {
            if (index >= 4) {
                comment.style.display = 'none';
            }
        });
        toggleCommentsBtn.setAttribute('data-showing', 'false');
    }
});

