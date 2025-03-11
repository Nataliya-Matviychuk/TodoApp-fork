document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.header');
    const primaryLinks = document.querySelectorAll('.nav-link');
    const logo = document.querySelector('.logo');

    document.addEventListener('scroll', () => {
        if (window.scrollY > 10) {
            header.classList.add('dark-header');
            logo.classList.add('dark-logo');

            primaryLinks.forEach(link => {
                link.classList.add('dark-link');
            });

        } else {
            header.classList.remove('dark-header');
            logo.classList.remove('dark-logo');

            primaryLinks.forEach(link => {
                link.classList.remove('dark-link');
            })
        }
    });
});