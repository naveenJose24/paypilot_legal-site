document.querySelectorAll('[data-year]').forEach((element) => {
  element.textContent = new Date().getFullYear();
});

const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.site-nav');
if (menuButton && navigation) {
  menuButton.addEventListener('click', () => {
    const open = navigation.classList.toggle('is-open');
    menuButton.setAttribute('aria-expanded', String(open));
  });
}

document.querySelectorAll('[data-copy-link]').forEach((button) => {
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      button.textContent = 'Link copied';
      window.setTimeout(() => { button.textContent = 'Copy link'; }, 1800);
    } catch (_) {
      button.textContent = 'Copy unavailable';
    }
  });
});
