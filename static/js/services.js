document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle functionality
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const logoutBtn = document.querySelector('.logout-btn');
    
    if (mobileMenuToggle && logoutBtn) {
        mobileMenuToggle.addEventListener('click', function() {
            const icon = this.querySelector('i');
            
            // Toggle between bars and times icon
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
                
                // Show logout text when menu is open
                const logoutText = logoutBtn.querySelector('.logout-text');
                if (logoutText) {
                    logoutText.style.display = 'inline';
                }
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
                
                // Hide logout text when menu is closed
                const logoutText = logoutBtn.querySelector('.logout-text');
                if (logoutText) {
                    logoutText.style.display = 'none';
                }
            }
        });
    }
    
    // Add any additional interactive elements here
    const dashboardCards = document.querySelectorAll('.dashboard-card');
    dashboardCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't trigger if clicking on a link inside the card
            if (!e.target.closest('a')) {
                const link = this.querySelector('a');
                if (link) {
                    window.location.href = link.href;
                }
            }
        });
    });
});