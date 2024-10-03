// Add event listener to quick contact button
document.addEventListener("DOMContentLoaded", function () {
    const quickContact = document.querySelector(".quick-contact");
    quickContact.addEventListener("click", function () {
      // Add your contact logic here
    });
  });
  document.getElementById('registrationForm').addEventListener('submit', function(event) {
    var password = document.getElementById('password').value;

    if (password.length < 8) {
        alert('Password must be at least 8 characters long.');
        event.preventDefault();  // Prevent the form from submitting
    }
});
document.addEventListener("DOMContentLoaded", function() {
  console.log("JavaScript linked and ready!");

  // Add interactivity here
  // For example, you could add form validation or button effects
});
