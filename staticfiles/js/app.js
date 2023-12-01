
/**
 * Takes current page's URL string and copies it to
 * user's clipboard.
*/
function copyMixtapeLink() {
    navigator.clipboard.writeText(window.location.href)
      .then(() => {
        alert("Your mixtape link has been copied");
      })
      .catch(err => {
        alert('Failed to copy your mixtape link. Please try again later.');
      });
  }