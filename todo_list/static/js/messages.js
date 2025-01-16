// Wait until the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {

    const alerts = document.querySelectorAll('.alert');

    alerts.forEach(alert => {
        // Set a timeout to hide the alert after 5 seconds (5000ms)
        setTimeout(() => {
            alert.style.transition = 'opacity 0.7s ease'; // Smooth fade-out effect
            alert.style.opacity = '0'; // Fade-out the alert

            // Remove the alert from the DOM after the fade-out
            setTimeout(() => {
                alert.remove();
            }, 200);
        }, 2000);
    });
});