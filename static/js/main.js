document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const authLinks = document.querySelector('.auth-links');
    
    if (mobileMenuButton && authLinks) {
      mobileMenuButton.addEventListener('click', function() {
        authLinks.classList.toggle('active');
        const icon = this.querySelector('i');
        if (authLinks.classList.contains('active')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      });
    }
    
    // Set current year in footer
    const yearElement = document.querySelector('.current-year');
    if (yearElement) {
      yearElement.textContent = new Date().getFullYear();
    }
    
    // Close messages when clicked
    const messages = document.querySelector('.messages');
    if (messages) {
      messages.addEventListener('click', function() {
        this.style.display = 'none';
      });
      
      // Auto-hide after 5 seconds
      setTimeout(() => {
        messages.style.display = 'none';
      }, 5000);
    }
  });