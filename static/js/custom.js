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


console.log('Script loaded');

document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM fully loaded');

    document.querySelectorAll('.toggle-replies').forEach(function (button) {
        console.log('Reply toggle found:', button);
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const commentId = this.dataset.id;
            console.log('Clicked reply toggle for comment ID:', commentId);
            const moreReplies = document.getElementById('more-replies-' + commentId);
            console.log('More replies div:', moreReplies);
            if (moreReplies.style.display === 'none') {
                moreReplies.style.display = 'block';
                this.textContent = 'Hide replies';
            } else {
                moreReplies.style.display = 'none';
                this.textContent = 'Show all replies';
            }
        });
    });

    
});
