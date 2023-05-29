
// Add event listeners to social media links
const socialMediaLinks = document.querySelectorAll('.social-media a');
socialMediaLinks.forEach(link => {
  link.addEventListener('click', () => {
     //Open the link in a new tab
    window.open(link.href, '_blank');
  });
});

// Add event listeners to header links
const headerLinks = document.querySelectorAll('header nav ul li a');
headerLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    // Prevent the default link behavior
    event.preventDefault();
    
    // Redirect to the linked page
    window.location.href = link.href;
  });
});